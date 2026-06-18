from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json
from statistics import mean

@dataclass(frozen=True)
class SearchSortingCase:
    case_name: str
    problem_context: str
    algorithmic_choice: str
    search_space_clarity: float
    predicate_or_key_clarity: float
    ordering_rule_quality: float
    data_structure_fit: float
    complexity_awareness: float
    edge_case_coverage: float
    stability_or_tie_breaking: float
    traceability: float
    robustness: float
    governance_readiness: float

WEIGHTS=[0.12,0.12,0.10,0.10,0.10,0.10,0.10,0.08,0.10,0.08]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def audit_quality(case: SearchSortingCase) -> float:
    vals=[case.search_space_clarity,case.predicate_or_key_clarity,case.ordering_rule_quality,case.data_structure_fit,case.complexity_awareness,case.edge_case_coverage,case.stability_or_tie_breaking,case.traceability,case.robustness,case.governance_readiness]
    return clamp(100*sum(v*w for v,w in zip(vals, WEIGHTS)))

def audit_risk(case: SearchSortingCase) -> float:
    vals=[case.search_space_clarity,case.predicate_or_key_clarity,case.ordering_rule_quality,case.data_structure_fit,case.complexity_awareness,case.edge_case_coverage,case.stability_or_tie_breaking,case.traceability,case.robustness,case.governance_readiness]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20: return "strong search and sorting discipline"
    if q >= 70 and r <= 35: return "usable search and sorting discipline with review needs"
    if r >= 55: return "high search and sorting risk"
    return "partial search and sorting discipline"

def load_cases(path: Path) -> list[SearchSortingCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [SearchSortingCase(r["case_name"],r["problem_context"],r["algorithmic_choice"],float(r["search_space_clarity"]),float(r["predicate_or_key_clarity"]),float(r["ordering_rule_quality"]),float(r["data_structure_fit"]),float(r["complexity_awareness"]),float(r["edge_case_coverage"]),float(r["stability_or_tie_breaking"]),float(r["traceability"]),float(r["robustness"]),float(r["governance_readiness"])) for r in rows]

def evaluate(cases: list[SearchSortingCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q,r=audit_quality(c),audit_risk(c)
        out.append({**asdict(c),"search_sorting_quality":round(q,3),"search_sorting_risk":round(r,3),"diagnostic":diagnose(q,r)})
    return out

def linear_search(values: list[int], target: int) -> int:
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def binary_search(values: list[int], target: int) -> int:
    low, high = 0, len(values)-1
    while low <= high:
        mid=(low+high)//2
        if values[mid] == target:
            return mid
        if values[mid] < target:
            low=mid+1
        else:
            high=mid-1
    return -1

def insertion_sort(values: list[int]) -> list[int]:
    result=list(values)
    for i in range(1,len(result)):
        key=result[i]; j=i-1
        while j >= 0 and result[j] > key:
            result[j+1]=result[j]; j -= 1
        result[j+1]=key
    return result

def is_sorted(values: list[int]) -> bool:
    return all(values[i] <= values[i+1] for i in range(len(values)-1))

def stable_sort_records(records: list[dict[str, object]], primary: str, secondary: str) -> list[dict[str, object]]:
    return sorted(records, key=lambda row: (row[primary], row[secondary]))

def algorithm_demos() -> dict[str, object]:
    values=[7,2,9,1,5]
    sorted_values=insertion_sort(values)
    records=[
        {"name":"A","department":"Research","priority":2},
        {"name":"B","department":"Research","priority":1},
        {"name":"C","department":"Library","priority":1}
    ]
    return {
        "linear_search_target_9":linear_search(values,9),
        "binary_search_target_5":binary_search(sorted_values,5),
        "insertion_sort":sorted_values,
        "is_sorted_after_insertion_sort":is_sorted(sorted_values),
        "stable_multi_key_sort":stable_sort_records(records,"department","priority")
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
    rows=evaluate(load_cases(root/"data"/"synthetic_search_sorting_cases.csv"))
    summary={"case_count":len(rows),"average_search_sorting_quality":round(mean(float(r["search_sorting_quality"]) for r in rows),3),"average_search_sorting_risk":round(mean(float(r["search_sorting_risk"]) for r in rows),3),"highest_quality_case":max(rows,key=lambda r:float(r["search_sorting_quality"]))["case_name"],"highest_risk_case":max(rows,key=lambda r:float(r["search_sorting_risk"]))["case_name"]}
    write_csv(root/"outputs"/"tables"/"search_sorting_audit.csv", rows)
    write_csv(root/"outputs"/"tables"/"search_sorting_audit_summary.csv", [summary])
    write_json(root/"outputs"/"json"/"search_sorting_audit.json", rows)
    write_json(root/"outputs"/"json"/"search_sorting_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"search_sorting_demos.json", algorithm_demos())

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
