from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json, os, platform, sys
from statistics import mean

@dataclass(frozen=True)
class RuntimeContextCase:
    case_name: str
    problem_context: str
    runtime_design_choice: str
    runtime_documentation: float
    dependency_control: float
    configuration_validation: float
    resource_visibility: float
    portability_support: float
    reproducibility_support: float
    security_boundaries: float
    observability: float
    external_service_discipline: float
    governance_readiness: float

WEIGHTS=[0.10,0.12,0.10,0.10,0.08,0.12,0.12,0.10,0.08,0.08]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def runtime_quality(case: RuntimeContextCase) -> float:
    vals=[case.runtime_documentation,case.dependency_control,case.configuration_validation,case.resource_visibility,case.portability_support,case.reproducibility_support,case.security_boundaries,case.observability,case.external_service_discipline,case.governance_readiness]
    return clamp(100*sum(v*w for v,w in zip(vals, WEIGHTS)))

def runtime_risk(case: RuntimeContextCase) -> float:
    vals=[case.runtime_documentation,case.dependency_control,case.configuration_validation,case.resource_visibility,case.reproducibility_support,case.security_boundaries,case.observability,case.external_service_discipline]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20: return "strong runtime discipline"
    if q >= 70 and r <= 35: return "usable runtime discipline with review needs"
    if r >= 55: return "high runtime-context risk"
    return "partial runtime discipline"

def load_cases(path: Path) -> list[RuntimeContextCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [RuntimeContextCase(r["case_name"],r["problem_context"],r["runtime_design_choice"],float(r["runtime_documentation"]),float(r["dependency_control"]),float(r["configuration_validation"]),float(r["resource_visibility"]),float(r["portability_support"]),float(r["reproducibility_support"]),float(r["security_boundaries"]),float(r["observability"]),float(r["external_service_discipline"]),float(r["governance_readiness"])) for r in rows]

def evaluate(cases: list[RuntimeContextCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q,r=runtime_quality(c),runtime_risk(c)
        out.append({**asdict(c),"runtime_quality":round(q,3),"runtime_risk":round(r,3),"diagnostic":diagnose(q,r)})
    return out

def capture_runtime_manifest() -> dict[str, object]:
    return {
        "python_version": sys.version,
        "executable": sys.executable,
        "platform": platform.platform(),
        "machine": platform.machine(),
        "system": platform.system(),
        "release": platform.release(),
        "working_directory": os.getcwd(),
        "environment_variables_recorded": sorted([k for k in os.environ if k in {"PATH","HOME","SHELL","LANG","TZ","PYTHONPATH"}]),
        "interpretation": "Runtime manifests document where and how a workflow executed."
    }

def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    rows=evaluate(load_cases(root/"data"/"synthetic_runtime_context_cases.csv"))
    summary={"case_count":len(rows),"average_runtime_quality":round(mean(float(r["runtime_quality"]) for r in rows),3),"average_runtime_risk":round(mean(float(r["runtime_risk"]) for r in rows),3),"highest_quality_case":max(rows,key=lambda r:float(r["runtime_quality"]))["case_name"],"highest_risk_case":max(rows,key=lambda r:float(r["runtime_risk"]))["case_name"]}
    write_csv(root/"outputs"/"tables"/"runtime_context_audit.csv", rows)
    write_csv(root/"outputs"/"tables"/"runtime_context_audit_summary.csv", [summary])
    write_json(root/"outputs"/"json"/"runtime_context_audit.json", rows)
    write_json(root/"outputs"/"json"/"runtime_context_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"runtime_manifest.json", capture_runtime_manifest())

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
