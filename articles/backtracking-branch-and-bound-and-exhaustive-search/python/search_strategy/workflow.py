from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, itertools, json
from statistics import mean

@dataclass(frozen=True)
class SearchStrategyCase:
    case_name: str
    problem_context: str
    search_strategy: str
    search_space_clarity: float
    candidate_generation_completeness: float
    constraint_quality: float
    pruning_soundness: float
    bound_validity: float
    objective_clarity: float
    edge_case_coverage: float
    traceability: float
    complexity_awareness: float
    governance_readiness: float

WEIGHTS=[0.12,0.12,0.10,0.10,0.10,0.10,0.10,0.08,0.10,0.08]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def search_quality(case: SearchStrategyCase) -> float:
    vals=[case.search_space_clarity,case.candidate_generation_completeness,case.constraint_quality,case.pruning_soundness,case.bound_validity,case.objective_clarity,case.edge_case_coverage,case.traceability,case.complexity_awareness,case.governance_readiness]
    return clamp(100*sum(v*w for v,w in zip(vals, WEIGHTS)))

def search_risk(case: SearchStrategyCase) -> float:
    vals=[case.search_space_clarity,case.candidate_generation_completeness,case.constraint_quality,case.pruning_soundness,case.bound_validity,case.objective_clarity,case.edge_case_coverage,case.traceability,case.complexity_awareness,case.governance_readiness]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20: return "strong search-strategy discipline"
    if q >= 70 and r <= 35: return "usable search strategy with review needs"
    if r >= 55: return "high search-strategy risk"
    return "partial search discipline"

def load_cases(path: Path) -> list[SearchStrategyCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [SearchStrategyCase(r["case_name"],r["problem_context"],r["search_strategy"],float(r["search_space_clarity"]),float(r["candidate_generation_completeness"]),float(r["constraint_quality"]),float(r["pruning_soundness"]),float(r["bound_validity"]),float(r["objective_clarity"]),float(r["edge_case_coverage"]),float(r["traceability"]),float(r["complexity_awareness"]),float(r["governance_readiness"])) for r in rows]

def evaluate(cases: list[SearchStrategyCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q,r=search_quality(c),search_risk(c)
        out.append({**asdict(c),"search_strategy_quality":round(q,3),"search_strategy_risk":round(r,3),"diagnostic":diagnose(q,r)})
    return out

def exhaustive_subset_search(values: list[int], capacity: int) -> dict[str, object]:
    best_subset=()
    best_value=-1
    checked=0
    for size in range(len(values)+1):
        for indices in itertools.combinations(range(len(values)), size):
            checked += 1
            total=sum(values[i] for i in indices)
            if total <= capacity and total > best_value:
                best_value=total
                best_subset=indices
    return {"best_value":best_value,"best_subset_indices":list(best_subset),"checked_candidates":checked}

def backtracking_permutations(items: list[str], prefix: list[str] | None = None) -> list[list[str]]:
    if prefix is None:
        prefix=[]
    if not items:
        return [prefix]
    out=[]
    for i,item in enumerate(items):
        out.extend(backtracking_permutations(items[:i]+items[i+1:], prefix+[item]))
    return out

def branch_and_bound_knapsack(values: list[int], weights: list[int], capacity: int) -> dict[str, object]:
    n=len(values)
    best_value=0
    best_items=[]
    explored=0
    pruned=0
    def upper_bound(index: int, current_value: int, current_weight: int) -> float:
        remaining=capacity-current_weight
        bound=float(current_value)
        for j in range(index,n):
            if weights[j] <= remaining:
                bound += values[j]
                remaining -= weights[j]
            else:
                bound += values[j] * (remaining / weights[j])
                break
        return bound
    def search(index: int, current_value: int, current_weight: int, chosen: list[int]) -> None:
        nonlocal best_value, best_items, explored, pruned
        explored += 1
        if current_weight > capacity:
            pruned += 1
            return
        if current_value > best_value:
            best_value=current_value
            best_items=chosen[:]
        if index == n:
            return
        if upper_bound(index,current_value,current_weight) <= best_value:
            pruned += 1
            return
        search(index+1,current_value+values[index],current_weight+weights[index],chosen+[index])
        search(index+1,current_value,current_weight,chosen)
    search(0,0,0,[])
    return {"best_value":best_value,"best_item_indices":best_items,"explored_nodes":explored,"pruned_nodes":pruned}

def demos() -> dict[str, object]:
    return {"exhaustive_subset_search":exhaustive_subset_search([3,4,5,9],10),"backtracking_permutations_count":len(backtracking_permutations(["A","B","C"])),"branch_and_bound_knapsack":branch_and_bound_knapsack([6,10,12],[1,2,3],5)}

def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    rows=evaluate(load_cases(root/"data"/"synthetic_search_strategy_cases.csv"))
    summary={"case_count":len(rows),"average_search_strategy_quality":round(mean(float(r["search_strategy_quality"]) for r in rows),3),"average_search_strategy_risk":round(mean(float(r["search_strategy_risk"]) for r in rows),3),"highest_quality_case":max(rows,key=lambda r:float(r["search_strategy_quality"]))["case_name"],"highest_risk_case":max(rows,key=lambda r:float(r["search_strategy_risk"]))["case_name"]}
    write_csv(root/"outputs"/"tables"/"search_strategy_audit.csv", rows)
    write_csv(root/"outputs"/"tables"/"search_strategy_audit_summary.csv", [summary])
    write_json(root/"outputs"/"json"/"search_strategy_audit.json", rows)
    write_json(root/"outputs"/"json"/"search_strategy_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"search_strategy_demos.json", demos())

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
