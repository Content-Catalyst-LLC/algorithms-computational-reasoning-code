from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json, math
from statistics import mean

@dataclass(frozen=True)
class TractabilityCase:
    case_name: str
    problem_context: str
    problem_form: str
    expected_difficulty: str
    input_definition_clarity: float
    complexity_evidence: float
    structure_exploitation: float
    exact_method_feasibility: float
    approximation_readiness: float
    heuristic_validation: float
    benchmark_evidence: float
    timeout_handling: float
    governance_readiness: float
    communication_clarity: float

WEIGHTS=[0.10,0.12,0.10,0.10,0.10,0.10,0.12,0.08,0.10,0.08]

def clamp(x: float) -> float: return max(0.0, min(100.0, x))

def tractability_quality(case: TractabilityCase) -> float:
    vals=[case.input_definition_clarity,case.complexity_evidence,case.structure_exploitation,case.exact_method_feasibility,case.approximation_readiness,case.heuristic_validation,case.benchmark_evidence,case.timeout_handling,case.governance_readiness,case.communication_clarity]
    return clamp(100*sum(v*w for v,w in zip(vals,WEIGHTS)))

def tractability_risk(case: TractabilityCase) -> float:
    vals=[case.input_definition_clarity,case.complexity_evidence,case.structure_exploitation,case.exact_method_feasibility,case.approximation_readiness,case.heuristic_validation,case.benchmark_evidence,case.timeout_handling,case.governance_readiness,case.communication_clarity]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20: return "strong tractability discipline"
    if q >= 70 and r <= 35: return "usable tractability evidence with review needs"
    if r >= 55: return "high risk; hard-problem limits may be unclear or unmanaged"
    return "partial tractability discipline"

def load_cases(path: Path) -> list[TractabilityCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [TractabilityCase(r["case_name"],r["problem_context"],r["problem_form"],r["expected_difficulty"],float(r["input_definition_clarity"]),float(r["complexity_evidence"]),float(r["structure_exploitation"]),float(r["exact_method_feasibility"]),float(r["approximation_readiness"]),float(r["heuristic_validation"]),float(r["benchmark_evidence"]),float(r["timeout_handling"]),float(r["governance_readiness"]),float(r["communication_clarity"])) for r in rows]

def subset_count(n: int): return 2**n if n <= 60 else "too_large"
def permutation_count(n: int): return math.factorial(n) if n <= 20 else "too_large"

def search_space_table(values: list[int]) -> list[dict[str, object]]:
    return [{"n":n,"subsets_2_to_n":subset_count(n),"permutations_n_factorial":permutation_count(n),"quadratic_pairs":n*(n-1)//2} for n in values]

def feasibility_label(cost: float, budget: float) -> str:
    if cost <= 0.25*budget: return "comfortable"
    if cost <= budget: return "near budget"
    return "exceeds budget"

def feasibility_table(budget: float = 1_000_000) -> list[dict[str, object]]:
    rows=[]
    for n in [10,20,30,50,100,1000]:
        linear=n
        quadratic=n*n
        exponential=2**n if n <= 30 else float("inf")
        rows.append({"n":n,"linear_cost":linear,"linear_feasibility":feasibility_label(linear,budget),"quadratic_cost":quadratic,"quadratic_feasibility":feasibility_label(quadratic,budget),"exponential_cost":exponential if exponential != float("inf") else "too_large","exponential_feasibility":"exceeds budget" if exponential > budget else feasibility_label(exponential,budget)})
    return rows

def evaluate(cases: list[TractabilityCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q,r=tractability_quality(c),tractability_risk(c)
        out.append({**asdict(c),"tractability_quality":round(q,3),"tractability_risk":round(r,3),"diagnostic":diagnose(q,r)})
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
    audit=evaluate(load_cases(root/"data"/"synthetic_tractability_cases.csv"))
    search=search_space_table([5,10,15,20,30,50])
    feasible=feasibility_table()
    summary={"case_count":len(audit),"average_tractability_quality":round(mean(float(r["tractability_quality"]) for r in audit),3),"average_tractability_risk":round(mean(float(r["tractability_risk"]) for r in audit),3),"highest_quality_case":max(audit,key=lambda r:float(r["tractability_quality"]))["case_name"],"highest_risk_case":max(audit,key=lambda r:float(r["tractability_risk"]))["case_name"]}
    write_csv(root/"outputs"/"tables"/"tractability_audit.csv", audit)
    write_csv(root/"outputs"/"tables"/"tractability_audit_summary.csv", [summary])
    write_csv(root/"outputs"/"tables"/"search_space_growth.csv", search)
    write_csv(root/"outputs"/"tables"/"feasibility_budget_table.csv", feasible)
    write_json(root/"outputs"/"json"/"tractability_audit.json", audit)
    write_json(root/"outputs"/"json"/"tractability_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"search_space_growth.json", search)
    write_json(root/"outputs"/"json"/"feasibility_budget_table.json", feasible)

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
