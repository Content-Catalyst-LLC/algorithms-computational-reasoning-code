from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json
from statistics import mean

@dataclass(frozen=True)
class DivideConquerCase:
    case_name: str
    problem_context: str
    design_choice: str
    decomposition_clarity: float
    base_case_clarity: float
    subproblem_validity: float
    progress_toward_termination: float
    combination_correctness: float
    recurrence_awareness: float
    edge_case_coverage: float
    boundary_handling: float
    traceability: float
    governance_readiness: float

WEIGHTS=[0.12,0.10,0.10,0.12,0.12,0.10,0.10,0.08,0.08,0.08]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def design_quality(case: DivideConquerCase) -> float:
    vals=[case.decomposition_clarity,case.base_case_clarity,case.subproblem_validity,case.progress_toward_termination,case.combination_correctness,case.recurrence_awareness,case.edge_case_coverage,case.boundary_handling,case.traceability,case.governance_readiness]
    return clamp(100*sum(v*w for v,w in zip(vals, WEIGHTS)))

def design_risk(case: DivideConquerCase) -> float:
    vals=[case.decomposition_clarity,case.base_case_clarity,case.subproblem_validity,case.progress_toward_termination,case.combination_correctness,case.recurrence_awareness,case.edge_case_coverage,case.boundary_handling,case.traceability,case.governance_readiness]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20: return "strong divide-and-conquer discipline"
    if q >= 70 and r <= 35: return "usable divide-and-conquer discipline with review needs"
    if r >= 55: return "high divide-and-conquer risk"
    return "partial divide-and-conquer discipline"

def load_cases(path: Path) -> list[DivideConquerCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [DivideConquerCase(r["case_name"],r["problem_context"],r["design_choice"],float(r["decomposition_clarity"]),float(r["base_case_clarity"]),float(r["subproblem_validity"]),float(r["progress_toward_termination"]),float(r["combination_correctness"]),float(r["recurrence_awareness"]),float(r["edge_case_coverage"]),float(r["boundary_handling"]),float(r["traceability"]),float(r["governance_readiness"])) for r in rows]

def evaluate(cases: list[DivideConquerCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q,r=design_quality(c),design_risk(c)
        out.append({**asdict(c),"divide_conquer_quality":round(q,3),"divide_conquer_risk":round(r,3),"diagnostic":diagnose(q,r)})
    return out

def merge(left: list[int], right: list[int]) -> list[int]:
    result=[]; i=j=0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]

def merge_sort(values: list[int]) -> list[int]:
    if len(values) <= 1:
        return list(values)
    mid=len(values)//2
    return merge(merge_sort(values[:mid]), merge_sort(values[mid:]))

def binary_search(values: list[int], target: int) -> int:
    low, high=0, len(values)-1
    while low <= high:
        mid=(low+high)//2
        if values[mid] == target: return mid
        if values[mid] < target: low=mid+1
        else: high=mid-1
    return -1

def recurrence_estimate(n: int, branches: int = 2, shrink: int = 2, combine_power: float = 1.0) -> dict[str, float]:
    depth=0; size=max(1,n)
    while size > 1:
        size=max(1,size//shrink); depth += 1
    leaves=branches**depth
    combine_work=sum((n/(shrink**level))**combine_power*(branches**level) for level in range(depth+1))
    return {"n":float(n),"recursion_depth":float(depth),"estimated_leaf_count":float(leaves),"estimated_combine_work":round(float(combine_work),3)}

def demos() -> dict[str, object]:
    values=[9,3,7,1,4,8]
    sorted_values=merge_sort(values)
    return {"original_values":values,"merge_sort_result":sorted_values,"binary_search_for_7":binary_search(sorted_values,7),"binary_search_for_missing_10":binary_search(sorted_values,10),"merge_sort_recurrence_estimate":recurrence_estimate(1024,2,2,1.0),"binary_search_recurrence_estimate":recurrence_estimate(1024,1,2,0.0)}

def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    rows=evaluate(load_cases(root/"data"/"synthetic_divide_conquer_cases.csv"))
    summary={"case_count":len(rows),"average_divide_conquer_quality":round(mean(float(r["divide_conquer_quality"]) for r in rows),3),"average_divide_conquer_risk":round(mean(float(r["divide_conquer_risk"]) for r in rows),3),"highest_quality_case":max(rows,key=lambda r:float(r["divide_conquer_quality"]))["case_name"],"highest_risk_case":max(rows,key=lambda r:float(r["divide_conquer_risk"]))["case_name"]}
    write_csv(root/"outputs"/"tables"/"divide_conquer_audit.csv", rows)
    write_csv(root/"outputs"/"tables"/"divide_conquer_audit_summary.csv", [summary])
    write_json(root/"outputs"/"json"/"divide_conquer_audit.json", rows)
    write_json(root/"outputs"/"json"/"divide_conquer_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"divide_conquer_demos.json", demos())

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
