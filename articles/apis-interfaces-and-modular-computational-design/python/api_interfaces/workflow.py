from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json
from statistics import mean

@dataclass(frozen=True)
class InterfaceCase:
    case_name: str
    problem_context: str
    interface_design_choice: str
    contract_clarity: float
    schema_validation: float
    error_behavior: float
    versioning_strategy: float
    documentation_quality: float
    testability: float
    coupling_control: float
    observability: float
    security_boundaries: float
    governance_readiness: float

WEIGHTS=[0.12,0.12,0.10,0.10,0.10,0.10,0.10,0.08,0.10,0.08]
REQUIRED_FIELDS={"case_id","status","score"}

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def interface_quality(case: InterfaceCase) -> float:
    vals=[case.contract_clarity,case.schema_validation,case.error_behavior,case.versioning_strategy,case.documentation_quality,case.testability,case.coupling_control,case.observability,case.security_boundaries,case.governance_readiness]
    return clamp(100*sum(v*w for v,w in zip(vals, WEIGHTS)))

def interface_risk(case: InterfaceCase) -> float:
    vals=[case.contract_clarity,case.schema_validation,case.error_behavior,case.versioning_strategy,case.documentation_quality,case.testability,case.coupling_control,case.security_boundaries]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20: return "strong interface discipline"
    if q >= 70 and r <= 35: return "usable interface discipline with review needs"
    if r >= 55: return "high interface risk"
    return "partial interface discipline"

def validate_record(record: dict[str, object]) -> dict[str, object]:
    missing=sorted(REQUIRED_FIELDS-set(record.keys()))
    errors=[]
    if missing: errors.append({"code":"missing_required_fields","fields":missing})
    if "score" in record and not isinstance(record["score"], (int,float)):
        errors.append({"code":"invalid_score_type","expected":"number"})
    if "status" in record and record["status"] not in {"draft","review","approved","rejected","archived"}:
        errors.append({"code":"invalid_status","allowed":["draft","review","approved","rejected","archived"]})
    return {"valid":len(errors)==0,"errors":errors}

def demo_contract_validation() -> dict[str, object]:
    return {
        "valid_record_result": validate_record({"case_id":"case-001","status":"review","score":72.4}),
        "invalid_record_result": validate_record({"case_id":"case-002","status":"unknown","score":"high"})
    }

def load_cases(path: Path) -> list[InterfaceCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [InterfaceCase(r["case_name"],r["problem_context"],r["interface_design_choice"],float(r["contract_clarity"]),float(r["schema_validation"]),float(r["error_behavior"]),float(r["versioning_strategy"]),float(r["documentation_quality"]),float(r["testability"]),float(r["coupling_control"]),float(r["observability"]),float(r["security_boundaries"]),float(r["governance_readiness"])) for r in rows]

def evaluate(cases: list[InterfaceCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q,r=interface_quality(c),interface_risk(c)
        out.append({**asdict(c),"interface_quality":round(q,3),"interface_risk":round(r,3),"diagnostic":diagnose(q,r)})
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
    rows=evaluate(load_cases(root/"data"/"synthetic_api_interface_cases.csv"))
    summary={"case_count":len(rows),"average_interface_quality":round(mean(float(r["interface_quality"]) for r in rows),3),"average_interface_risk":round(mean(float(r["interface_risk"]) for r in rows),3),"highest_quality_case":max(rows,key=lambda r:float(r["interface_quality"]))["case_name"],"highest_risk_case":max(rows,key=lambda r:float(r["interface_risk"]))["case_name"]}
    write_csv(root/"outputs"/"tables"/"api_interface_audit.csv", rows)
    write_csv(root/"outputs"/"tables"/"api_interface_audit_summary.csv", [summary])
    write_json(root/"outputs"/"json"/"api_interface_audit.json", rows)
    write_json(root/"outputs"/"json"/"api_interface_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"contract_validation_demo.json", demo_contract_validation())

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
