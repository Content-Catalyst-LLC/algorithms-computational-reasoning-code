from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json
from statistics import mean

@dataclass(frozen=True)
class AlgorithmDesignCase:
    case_name: str
    problem_context: str
    design_choice: str
    problem_formulation: float
    input_output_clarity: float
    correctness_rationale: float
    termination_argument: float
    complexity_analysis: float
    data_structure_fit: float
    edge_case_coverage: float
    robustness: float
    interpretability: float
    governance_readiness: float

WEIGHTS=[0.12,0.10,0.12,0.10,0.10,0.10,0.10,0.10,0.08,0.08]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def design_quality(case: AlgorithmDesignCase) -> float:
    vals=[case.problem_formulation,case.input_output_clarity,case.correctness_rationale,case.termination_argument,case.complexity_analysis,case.data_structure_fit,case.edge_case_coverage,case.robustness,case.interpretability,case.governance_readiness]
    return clamp(100*sum(v*w for v,w in zip(vals, WEIGHTS)))

def design_risk(case: AlgorithmDesignCase) -> float:
    vals=[case.problem_formulation,case.input_output_clarity,case.correctness_rationale,case.termination_argument,case.complexity_analysis,case.edge_case_coverage,case.robustness,case.governance_readiness]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20: return "strong algorithm design discipline"
    if q >= 70 and r <= 35: return "usable algorithm design with review needs"
    if r >= 55: return "high design risk"
    return "partial design discipline"

def load_cases(path: Path) -> list[AlgorithmDesignCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [AlgorithmDesignCase(r["case_name"],r["problem_context"],r["design_choice"],float(r["problem_formulation"]),float(r["input_output_clarity"]),float(r["correctness_rationale"]),float(r["termination_argument"]),float(r["complexity_analysis"]),float(r["data_structure_fit"]),float(r["edge_case_coverage"]),float(r["robustness"]),float(r["interpretability"]),float(r["governance_readiness"])) for r in rows]

def evaluate(cases: list[AlgorithmDesignCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q,r=design_quality(c),design_risk(c)
        out.append({**asdict(c),"design_quality":round(q,3),"design_risk":round(r,3),"diagnostic":diagnose(q,r)})
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
    rows=evaluate(load_cases(root/"data"/"synthetic_algorithm_design_cases.csv"))
    summary={"case_count":len(rows),"average_design_quality":round(mean(float(r["design_quality"]) for r in rows),3),"average_design_risk":round(mean(float(r["design_risk"]) for r in rows),3),"highest_quality_case":max(rows,key=lambda r:float(r["design_quality"]))["case_name"],"highest_risk_case":max(rows,key=lambda r:float(r["design_risk"]))["case_name"]}
    write_csv(root/"outputs"/"tables"/"algorithm_design_audit.csv", rows)
    write_csv(root/"outputs"/"tables"/"algorithm_design_audit_summary.csv", [summary])
    write_json(root/"outputs"/"json"/"algorithm_design_audit.json", rows)
    write_json(root/"outputs"/"json"/"algorithm_design_audit_summary.json", summary)

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
