from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv, json

@dataclass(frozen=True)
class OptimizationCase:
    case_name: str
    problem_context: str
    optimization_goal: str
    objective_clarity: float
    constraint_documentation: float
    feasible_set_clarity: float
    data_quality: float
    uncertainty_handling: float
    sensitivity_review: float
    tradeoff_transparency: float
    fairness_review: float
    robustness_review: float
    traceability: float
    governance_review: float
    communication_clarity: float

WEIGHTS=[0.11,0.11,0.10,0.09,0.09,0.08,0.10,0.09,0.08,0.07,0.06,0.02]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def optimization_score(case: OptimizationCase) -> float:
    vals=[case.objective_clarity,case.constraint_documentation,case.feasible_set_clarity,case.data_quality,case.uncertainty_handling,case.sensitivity_review,case.tradeoff_transparency,case.fairness_review,case.robustness_review,case.traceability,case.governance_review,case.communication_clarity]
    return clamp(100.0*sum(v*w for v,w in zip(vals,WEIGHTS)))

def optimization_risk(case: OptimizationCase) -> float:
    vals=[case.objective_clarity,case.constraint_documentation,case.feasible_set_clarity,case.data_quality,case.uncertainty_handling,case.sensitivity_review,case.tradeoff_transparency,case.fairness_review,case.robustness_review,case.traceability,case.governance_review]
    return clamp(100.0*mean(1.0-v for v in vals))

def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong optimization discipline"
    if score >= 70 and risk <= 35:
        return "usable optimization design with review needs"
    if risk >= 55:
        return "high risk; objectives, constraints, feasible set, uncertainty, trade-offs, fairness, or governance may be underdefined"
    return "partial discipline; strengthen objectives, constraints, feasible set, sensitivity, robustness, trade-off transparency, and governance"

def weighted_objective(values: list[float], weights: list[float]) -> float:
    if len(values) != len(weights):
        raise ValueError("values and weights must have the same length")
    return round(sum(v*w for v,w in zip(values, weights)), 6)

def linear_objective(coefficients: list[float], decision_values: list[float]) -> float:
    return weighted_objective(decision_values, coefficients)

def constraint_margin(limit: float, observed_value: float) -> float:
    return round(limit - observed_value, 6)

def penalty_objective(base_objective: float, penalty: float, penalty_weight: float) -> float:
    return round(base_objective + penalty_weight * penalty, 6)

def normalized_tradeoff_score(cost_score: float, quality_score: float, risk_score: float) -> float:
    return round((0.35*(1.0-cost_score)) + (0.40*quality_score) + (0.25*(1.0-risk_score)), 6)

def parse_floats(value: str) -> list[float]:
    return [float(x.strip()) for x in value.split(";") if x.strip()]

def load_cases(path: Path) -> list[OptimizationCase]:
    fields=["objective_clarity","constraint_documentation","feasible_set_clarity","data_quality","uncertainty_handling","sensitivity_review","tradeoff_transparency","fairness_review","robustness_review","traceability","governance_review","communication_clarity"]
    with path.open(newline="", encoding="utf-8") as f:
        return [OptimizationCase(r["case_name"],r["problem_context"],r["optimization_goal"],*[float(r[k]) for k in fields]) for r in csv.DictReader(f)]

def evaluate(cases: list[OptimizationCase]) -> list[dict[str,object]]:
    rows=[]
    for c in cases:
        score=optimization_score(c)
        risk=optimization_risk(c)
        rows.append({**asdict(c),"optimization_score":round(score,3),"optimization_risk":round(risk,3),"diagnostic":diagnose(score,risk)})
    return rows

def calculator_examples() -> list[dict[str,object]]:
    return [
        {"example":"linear_objective","coefficients":[4.0,2.0,1.5],"decision_values":[10.0,20.0,5.0],"objective_value":linear_objective([4.0,2.0,1.5],[10.0,20.0,5.0])},
        {"example":"constraint_margin","limit":100.0,"observed_value":86.5,"margin":constraint_margin(100.0,86.5)},
        {"example":"penalty_objective","base_objective":42.0,"penalty":8.0,"penalty_weight":2.5,"penalty_objective":penalty_objective(42.0,8.0,2.5)},
        {"example":"normalized_tradeoff_score","cost_score":0.30,"quality_score":0.82,"risk_score":0.25,"tradeoff_score":normalized_tradeoff_score(0.30,0.82,0.25)}
    ]

def calculator_input_summary(path: Path) -> list[dict[str,object]]:
    rows=[]
    with path.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            coefficients=parse_floats(r["coefficients"])
            decision_values=parse_floats(r["decision_values"])
            rows.append({
                **r,
                "linear_objective":linear_objective(coefficients, decision_values),
                "constraint_margin":constraint_margin(float(r["limit"]), float(r["observed_value"])),
                "penalty_objective":penalty_objective(float(r["base_objective"]), float(r["penalty"]), float(r["penalty_weight"])),
                "normalized_tradeoff_score":normalized_tradeoff_score(float(r["cost_score"]), float(r["quality_score"]), float(r["risk_score"]))
            })
    return rows

def write_csv(path: Path, rows: list[dict[str,object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    audit=evaluate(load_cases(root/"data"/"synthetic_optimization_cases.csv"))
    calc_summary=calculator_input_summary(root/"data"/"synthetic_optimization_calculator_inputs.csv")
    summary={
        "case_count":len(audit),
        "average_optimization_score":round(mean(float(r["optimization_score"]) for r in audit),3),
        "average_optimization_risk":round(mean(float(r["optimization_risk"]) for r in audit),3),
        "highest_score_case":max(audit,key=lambda r:float(r["optimization_score"]))["case_name"],
        "highest_risk_case":max(audit,key=lambda r:float(r["optimization_risk"]))["case_name"]
    }
    for name, rows in [
        ("optimization_audit",audit),
        ("optimization_audit_summary",[summary]),
        ("optimization_calculator_input_summary",calc_summary),
        ("optimization_calculator_examples",calculator_examples())
    ]:
        write_csv(root/"outputs"/"tables"/f"{name}.csv", rows)
        write_json(root/"outputs"/"json"/f"{name}.json", rows)

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
