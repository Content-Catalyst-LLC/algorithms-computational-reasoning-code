from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json
from statistics import mean

@dataclass(frozen=True)
class ReliabilityCase:
    case_name: str
    problem_context: str
    reliability_strategy: str
    specification_clarity: float
    test_coverage_rationale: float
    oracle_quality: float
    edge_case_testing: float
    regression_discipline: float
    property_checks: float
    reproducibility_evidence: float
    observability: float
    security_testing: float
    governance_readiness: float

WEIGHTS=[0.12,0.10,0.12,0.10,0.10,0.10,0.10,0.10,0.08,0.08]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def reliability_quality(case: ReliabilityCase) -> float:
    vals=[case.specification_clarity,case.test_coverage_rationale,case.oracle_quality,case.edge_case_testing,case.regression_discipline,case.property_checks,case.reproducibility_evidence,case.observability,case.security_testing,case.governance_readiness]
    return clamp(100*sum(v*w for v,w in zip(vals, WEIGHTS)))

def reliability_risk(case: ReliabilityCase) -> float:
    vals=[case.specification_clarity,case.test_coverage_rationale,case.oracle_quality,case.edge_case_testing,case.regression_discipline,case.property_checks,case.reproducibility_evidence,case.observability,case.security_testing]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20: return "strong reliability discipline"
    if q >= 70 and r <= 35: return "usable reliability discipline with review needs"
    if r >= 55: return "high reliability risk"
    return "partial reliability discipline"

def check_score_invariant(score: float) -> dict[str, object]:
    return {"score":score,"valid":0.0 <= score <= 100.0,"property":"score must remain between 0 and 100"}

def check_sorted_invariant(values: list[float]) -> dict[str, object]:
    return {"values":values,"valid":all(values[i] <= values[i+1] for i in range(len(values)-1)),"property":"values must be nondecreasing"}

def check_idempotency(first_result: object, second_result: object) -> dict[str, object]:
    return {"first_result":first_result,"second_result":second_result,"valid":first_result==second_result,"property":"repeating operation should preserve result"}

def property_demos() -> dict[str, object]:
    return {
        "score_invariant_valid":check_score_invariant(72.5),
        "score_invariant_invalid":check_score_invariant(112.0),
        "sorted_invariant_valid":check_sorted_invariant([1,2,2,4,9]),
        "sorted_invariant_invalid":check_sorted_invariant([1,5,3,9]),
        "idempotency_demo":check_idempotency({"status":"approved"},{"status":"approved"})
    }

def load_cases(path: Path) -> list[ReliabilityCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [ReliabilityCase(r["case_name"],r["problem_context"],r["reliability_strategy"],float(r["specification_clarity"]),float(r["test_coverage_rationale"]),float(r["oracle_quality"]),float(r["edge_case_testing"]),float(r["regression_discipline"]),float(r["property_checks"]),float(r["reproducibility_evidence"]),float(r["observability"]),float(r["security_testing"]),float(r["governance_readiness"])) for r in rows]

def evaluate(cases: list[ReliabilityCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q,r=reliability_quality(c),reliability_risk(c)
        out.append({**asdict(c),"reliability_quality":round(q,3),"reliability_risk":round(r,3),"diagnostic":diagnose(q,r)})
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
    rows=evaluate(load_cases(root/"data"/"synthetic_reliability_cases.csv"))
    summary={"case_count":len(rows),"average_reliability_quality":round(mean(float(r["reliability_quality"]) for r in rows),3),"average_reliability_risk":round(mean(float(r["reliability_risk"]) for r in rows),3),"highest_quality_case":max(rows,key=lambda r:float(r["reliability_quality"]))["case_name"],"highest_risk_case":max(rows,key=lambda r:float(r["reliability_risk"]))["case_name"]}
    write_csv(root/"outputs"/"tables"/"testing_verification_reliability_audit.csv", rows)
    write_csv(root/"outputs"/"tables"/"testing_verification_reliability_audit_summary.csv", [summary])
    write_json(root/"outputs"/"json"/"testing_verification_reliability_audit.json", rows)
    write_json(root/"outputs"/"json"/"testing_verification_reliability_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"property_check_demos.json", property_demos())

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
