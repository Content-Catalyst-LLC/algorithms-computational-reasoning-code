from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, itertools, json
from statistics import mean

@dataclass(frozen=True)
class ApproximationCase:
    case_name: str
    problem_context: str
    approximation_strategy: str
    objective_clarity: float
    feasibility_preservation: float
    guarantee_clarity: float
    assumption_validity: float
    bound_evidence: float
    runtime_practicality: float
    gap_reporting: float
    edge_case_coverage: float
    traceability: float
    governance_readiness: float

WEIGHTS=[0.12,0.12,0.12,0.10,0.10,0.10,0.08,0.08,0.08,0.10]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def approximation_quality(case: ApproximationCase) -> float:
    vals=[case.objective_clarity,case.feasibility_preservation,case.guarantee_clarity,case.assumption_validity,case.bound_evidence,case.runtime_practicality,case.gap_reporting,case.edge_case_coverage,case.traceability,case.governance_readiness]
    return clamp(100*sum(v*w for v,w in zip(vals,WEIGHTS)))

def approximation_risk(case: ApproximationCase) -> float:
    vals=[case.objective_clarity,case.feasibility_preservation,case.guarantee_clarity,case.assumption_validity,case.bound_evidence,case.runtime_practicality,case.gap_reporting,case.edge_case_coverage,case.traceability,case.governance_readiness]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20: return "strong approximation discipline"
    if q >= 70 and r <= 35: return "usable approximation design with review needs"
    if r >= 55: return "high approximation risk"
    return "partial approximation discipline"

def load_cases(path: Path) -> list[ApproximationCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [ApproximationCase(r["case_name"],r["problem_context"],r["approximation_strategy"],float(r["objective_clarity"]),float(r["feasibility_preservation"]),float(r["guarantee_clarity"]),float(r["assumption_validity"]),float(r["bound_evidence"]),float(r["runtime_practicality"]),float(r["gap_reporting"]),float(r["edge_case_coverage"]),float(r["traceability"]),float(r["governance_readiness"])) for r in rows]

def evaluate(cases: list[ApproximationCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q,r=approximation_quality(c),approximation_risk(c)
        out.append({**asdict(c),"approximation_quality":round(q,3),"approximation_risk":round(r,3),"diagnostic":diagnose(q,r)})
    return out

def vertex_cover_approx(edges: list[tuple[str,str]]) -> dict[str, object]:
    uncovered=set(tuple(sorted(edge)) for edge in edges)
    cover=set()
    selected=[]
    while uncovered:
        u,v=next(iter(uncovered))
        cover.update([u,v])
        selected.append((u,v))
        uncovered={edge for edge in uncovered if u not in edge and v not in edge}
    return {"cover":sorted(cover),"cover_size":len(cover),"selected_edges":selected,"approximation_factor":2}

def greedy_set_cover(universe: set[str], sets: dict[str,set[str]]) -> dict[str, object]:
    uncovered=set(universe)
    chosen=[]
    while uncovered:
        best=max(sets, key=lambda name: len(sets[name] & uncovered))
        if not (sets[best] & uncovered):
            raise ValueError("Universe cannot be covered by provided sets.")
        chosen.append(best)
        uncovered -= sets[best]
    return {"chosen_sets":chosen,"chosen_count":len(chosen)}

def exact_subset_cover_size(universe: set[str], sets: dict[str,set[str]]) -> int | None:
    names=list(sets)
    for r in range(1,len(names)+1):
        for combo in itertools.combinations(names,r):
            covered=set()
            for name in combo:
                covered |= sets[name]
            if covered >= universe:
                return r
    return None

def demos() -> dict[str, object]:
    edges=[("A","B"),("B","C"),("C","D"),("D","E")]
    universe={"a","b","c","d","e","f"}
    sets={"S1":{"a","b","c"},"S2":{"c","d"},"S3":{"d","e","f"},"S4":{"a","f"}}
    greedy=greedy_set_cover(universe,sets)
    exact=exact_subset_cover_size(universe,sets)
    return {"vertex_cover_approx":vertex_cover_approx(edges),"greedy_set_cover":greedy,"exact_set_cover_size_for_demo":exact,"greedy_to_exact_cover_ratio":greedy["chosen_count"]/exact if exact else None}

def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    rows=evaluate(load_cases(root/"data"/"synthetic_approximation_algorithm_cases.csv"))
    summary={"case_count":len(rows),"average_approximation_quality":round(mean(float(r["approximation_quality"]) for r in rows),3),"average_approximation_risk":round(mean(float(r["approximation_risk"]) for r in rows),3),"highest_quality_case":max(rows,key=lambda r:float(r["approximation_quality"]))["case_name"],"highest_risk_case":max(rows,key=lambda r:float(r["approximation_risk"]))["case_name"]}
    write_csv(root/"outputs"/"tables"/"approximation_algorithm_audit.csv", rows)
    write_csv(root/"outputs"/"tables"/"approximation_algorithm_audit_summary.csv", [summary])
    write_json(root/"outputs"/"json"/"approximation_algorithm_audit.json", rows)
    write_json(root/"outputs"/"json"/"approximation_algorithm_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"approximation_algorithm_demos.json", demos())

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
