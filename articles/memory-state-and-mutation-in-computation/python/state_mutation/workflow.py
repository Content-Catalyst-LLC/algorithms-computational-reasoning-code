from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json
from statistics import mean

@dataclass(frozen=True)
class StateMutationCase:
    case_name: str
    problem_context: str
    state_design_choice: str
    state_visibility: float
    mutation_control: float
    aliasing_risk_control: float
    side_effect_boundaries: float
    lifecycle_clarity: float
    concurrency_safety: float
    reproducibility_support: float
    auditability: float
    rollback_support: float
    governance_readiness: float

WEIGHTS = [0.12,0.12,0.10,0.10,0.10,0.10,0.10,0.10,0.08,0.08]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def state_quality(case: StateMutationCase) -> float:
    values = [case.state_visibility, case.mutation_control, case.aliasing_risk_control, case.side_effect_boundaries, case.lifecycle_clarity, case.concurrency_safety, case.reproducibility_support, case.auditability, case.rollback_support, case.governance_readiness]
    return clamp(100 * sum(v*w for v,w in zip(values, WEIGHTS)))

def mutation_risk(case: StateMutationCase) -> float:
    values = [case.state_visibility, case.mutation_control, case.aliasing_risk_control, case.side_effect_boundaries, case.lifecycle_clarity, case.concurrency_safety, case.reproducibility_support, case.auditability]
    return clamp(100 * mean(1-v for v in values))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20: return "strong state discipline"
    if q >= 70 and r <= 35: return "usable state discipline with review needs"
    if r >= 55: return "high mutation risk"
    return "partial state discipline"

def load_cases(path: Path) -> list[StateMutationCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows = csv.DictReader(f)
        return [StateMutationCase(r["case_name"], r["problem_context"], r["state_design_choice"], float(r["state_visibility"]), float(r["mutation_control"]), float(r["aliasing_risk_control"]), float(r["side_effect_boundaries"]), float(r["lifecycle_clarity"]), float(r["concurrency_safety"]), float(r["reproducibility_support"]), float(r["auditability"]), float(r["rollback_support"]), float(r["governance_readiness"])) for r in rows]

def evaluate(cases: list[StateMutationCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q, r = state_quality(c), mutation_risk(c)
        out.append({**asdict(c), "state_quality": round(q,3), "mutation_risk": round(r,3), "diagnostic": diagnose(q,r)})
    return out

def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    rows = evaluate(load_cases(root/"data"/"synthetic_state_mutation_cases.csv"))
    summary = {"case_count": len(rows), "average_state_quality": round(mean(float(r["state_quality"]) for r in rows),3), "average_mutation_risk": round(mean(float(r["mutation_risk"]) for r in rows),3), "highest_quality_case": max(rows,key=lambda r:float(r["state_quality"]))["case_name"], "highest_risk_case": max(rows,key=lambda r:float(r["mutation_risk"]))["case_name"]}
    write_csv(root/"outputs"/"tables"/"state_mutation_audit.csv", rows)
    write_csv(root/"outputs"/"tables"/"state_mutation_audit_summary.csv", [summary])
    write_json(root/"outputs"/"json"/"state_mutation_audit.json", rows)
    write_json(root/"outputs"/"json"/"state_mutation_audit_summary.json", summary)

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
