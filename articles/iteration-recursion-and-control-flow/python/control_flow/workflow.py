from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json
from statistics import mean

@dataclass(frozen=True)
class ControlFlowCase:
    case_name: str
    problem_context: str
    control_flow_choice: str
    path_clarity: float
    loop_structure: float
    recursion_structure: float
    state_update_discipline: float
    termination_evidence: float
    invariant_evidence: float
    edge_case_coverage: float
    error_handling: float
    traceability: float
    governance_readiness: float

WEIGHTS=[0.12,0.10,0.10,0.10,0.12,0.12,0.10,0.08,0.08,0.08]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def control_flow_quality(case: ControlFlowCase) -> float:
    vals=[case.path_clarity,case.loop_structure,case.recursion_structure,case.state_update_discipline,case.termination_evidence,case.invariant_evidence,case.edge_case_coverage,case.error_handling,case.traceability,case.governance_readiness]
    return clamp(100*sum(v*w for v,w in zip(vals, WEIGHTS)))

def control_flow_risk(case: ControlFlowCase) -> float:
    vals=[case.path_clarity,case.loop_structure,case.state_update_discipline,case.termination_evidence,case.invariant_evidence,case.edge_case_coverage,case.error_handling,case.traceability,case.governance_readiness]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20: return "strong control-flow discipline"
    if q >= 70 and r <= 35: return "usable control-flow discipline with review needs"
    if r >= 55: return "high control-flow risk"
    return "partial control-flow discipline"

def load_cases(path: Path) -> list[ControlFlowCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [ControlFlowCase(r["case_name"],r["problem_context"],r["control_flow_choice"],float(r["path_clarity"]),float(r["loop_structure"]),float(r["recursion_structure"]),float(r["state_update_discipline"]),float(r["termination_evidence"]),float(r["invariant_evidence"]),float(r["edge_case_coverage"]),float(r["error_handling"]),float(r["traceability"]),float(r["governance_readiness"])) for r in rows]

def evaluate(cases: list[ControlFlowCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q,r=control_flow_quality(c),control_flow_risk(c)
        out.append({**asdict(c),"control_flow_quality":round(q,3),"control_flow_risk":round(r,3),"diagnostic":diagnose(q,r)})
    return out

def iterative_sum(values: list[float]) -> dict[str, object]:
    total=0.0; trace=[]
    for index,value in enumerate(values):
        total += value
        trace.append({"index":index,"value":value,"running_total":total})
    return {"total":total,"trace":trace,"invariant":"running_total equals sum of processed prefix"}

def recursive_countdown(n: int) -> list[int]:
    if n <= 0:
        return [0]
    return [n] + recursive_countdown(n-1)

def branch_review(score: float, threshold: float = 80.0) -> dict[str, object]:
    if score < 0 or score > 100:
        return {"path":"validation_error","reason":"score outside 0..100"}
    if score >= threshold:
        return {"path":"human_review","reason":"score exceeds review threshold"}
    return {"path":"ordinary_processing","reason":"score below review threshold"}

def demo_control_flow() -> dict[str, object]:
    return {
        "iterative_sum":iterative_sum([2,4,6]),
        "recursive_countdown":recursive_countdown(4),
        "branch_low_score":branch_review(62),
        "branch_high_score":branch_review(91),
        "branch_invalid_score":branch_review(120)
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
    rows=evaluate(load_cases(root/"data"/"synthetic_control_flow_cases.csv"))
    summary={"case_count":len(rows),"average_control_flow_quality":round(mean(float(r["control_flow_quality"]) for r in rows),3),"average_control_flow_risk":round(mean(float(r["control_flow_risk"]) for r in rows),3),"highest_quality_case":max(rows,key=lambda r:float(r["control_flow_quality"]))["case_name"],"highest_risk_case":max(rows,key=lambda r:float(r["control_flow_risk"]))["case_name"]}
    write_csv(root/"outputs"/"tables"/"control_flow_audit.csv", rows)
    write_csv(root/"outputs"/"tables"/"control_flow_audit_summary.csv", [summary])
    write_json(root/"outputs"/"json"/"control_flow_audit.json", rows)
    write_json(root/"outputs"/"json"/"control_flow_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"control_flow_demos.json", demo_control_flow())

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
