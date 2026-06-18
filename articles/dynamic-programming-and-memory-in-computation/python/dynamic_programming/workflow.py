from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json
from statistics import mean

@dataclass(frozen=True)
class DynamicProgrammingCase:
    case_name: str
    problem_context: str
    memory_strategy: str
    state_clarity: float
    recurrence_validity: float
    base_case_clarity: float
    overlapping_subproblem_evidence: float
    optimal_substructure_evidence: float
    transition_clarity: float
    storage_strategy_quality: float
    edge_case_coverage: float
    traceability: float
    governance_readiness: float

WEIGHTS=[0.12,0.12,0.10,0.10,0.10,0.10,0.10,0.10,0.08,0.08]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def dp_quality(case: DynamicProgrammingCase) -> float:
    vals=[case.state_clarity,case.recurrence_validity,case.base_case_clarity,case.overlapping_subproblem_evidence,case.optimal_substructure_evidence,case.transition_clarity,case.storage_strategy_quality,case.edge_case_coverage,case.traceability,case.governance_readiness]
    return clamp(100*sum(v*w for v,w in zip(vals, WEIGHTS)))

def dp_risk(case: DynamicProgrammingCase) -> float:
    vals=[case.state_clarity,case.recurrence_validity,case.base_case_clarity,case.overlapping_subproblem_evidence,case.optimal_substructure_evidence,case.transition_clarity,case.storage_strategy_quality,case.edge_case_coverage,case.traceability,case.governance_readiness]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20: return "strong dynamic-programming discipline"
    if q >= 70 and r <= 35: return "usable dynamic-programming design with review needs"
    if r >= 55: return "high dynamic-programming risk"
    return "partial dynamic-programming discipline"

def load_cases(path: Path) -> list[DynamicProgrammingCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [DynamicProgrammingCase(r["case_name"],r["problem_context"],r["memory_strategy"],float(r["state_clarity"]),float(r["recurrence_validity"]),float(r["base_case_clarity"]),float(r["overlapping_subproblem_evidence"]),float(r["optimal_substructure_evidence"]),float(r["transition_clarity"]),float(r["storage_strategy_quality"]),float(r["edge_case_coverage"]),float(r["traceability"]),float(r["governance_readiness"])) for r in rows]

def evaluate(cases: list[DynamicProgrammingCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q,r=dp_quality(c),dp_risk(c)
        out.append({**asdict(c),"dynamic_programming_quality":round(q,3),"dynamic_programming_risk":round(r,3),"diagnostic":diagnose(q,r)})
    return out

def fibonacci_memo(n: int, memo: dict[int,int] | None = None) -> int:
    if memo is None:
        memo={}
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n]=n
    else:
        memo[n]=fibonacci_memo(n-1,memo)+fibonacci_memo(n-2,memo)
    return memo[n]

def edit_distance(a: str, b: str) -> int:
    rows=len(a)+1; cols=len(b)+1
    dp=[[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows): dp[i][0]=i
    for j in range(cols): dp[0][j]=j
    for i in range(1,rows):
        for j in range(1,cols):
            cost=0 if a[i-1]==b[j-1] else 1
            dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+cost)
    return dp[-1][-1]

def knapsack_01(values: list[int], weights: list[int], capacity: int) -> dict[str, object]:
    n=len(values)
    dp=[[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        value=values[i-1]; weight=weights[i-1]
        for w in range(capacity+1):
            without=dp[i-1][w]
            with_item=value+dp[i-1][w-weight] if weight <= w else without
            dp[i][w]=max(without, with_item)
    selected=[]; w=capacity
    for i in range(n,0,-1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i-1); w -= weights[i-1]
    selected.reverse()
    return {"max_value":dp[n][capacity],"selected_item_indices":selected,"capacity":capacity}

def algorithm_demos() -> dict[str, object]:
    return {"fibonacci_10":fibonacci_memo(10),"edit_distance_kitten_sitting":edit_distance("kitten","sitting"),"knapsack_demo":knapsack_01([6,10,12],[1,2,3],5)}

def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    rows=evaluate(load_cases(root/"data"/"synthetic_dynamic_programming_cases.csv"))
    summary={"case_count":len(rows),"average_dynamic_programming_quality":round(mean(float(r["dynamic_programming_quality"]) for r in rows),3),"average_dynamic_programming_risk":round(mean(float(r["dynamic_programming_risk"]) for r in rows),3),"highest_quality_case":max(rows,key=lambda r:float(r["dynamic_programming_quality"]))["case_name"],"highest_risk_case":max(rows,key=lambda r:float(r["dynamic_programming_risk"]))["case_name"]}
    write_csv(root/"outputs"/"tables"/"dynamic_programming_audit.csv", rows)
    write_csv(root/"outputs"/"tables"/"dynamic_programming_audit_summary.csv", [summary])
    write_json(root/"outputs"/"json"/"dynamic_programming_audit.json", rows)
    write_json(root/"outputs"/"json"/"dynamic_programming_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"dynamic_programming_demos.json", algorithm_demos())

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
