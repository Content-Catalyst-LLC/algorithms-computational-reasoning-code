from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, heapq, json
from statistics import mean

@dataclass(frozen=True)
class GreedyCase:
    case_name: str
    problem_context: str
    local_decision_rule: str
    local_rule_clarity: float
    global_objective_clarity: float
    greedy_choice_evidence: float
    optimal_substructure_evidence: float
    feasibility_check_quality: float
    edge_case_coverage: float
    counterexample_testing: float
    traceability: float
    robustness: float
    governance_readiness: float

WEIGHTS=[0.12,0.12,0.12,0.10,0.10,0.10,0.10,0.08,0.08,0.08]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def greedy_quality(case: GreedyCase) -> float:
    vals=[case.local_rule_clarity,case.global_objective_clarity,case.greedy_choice_evidence,case.optimal_substructure_evidence,case.feasibility_check_quality,case.edge_case_coverage,case.counterexample_testing,case.traceability,case.robustness,case.governance_readiness]
    return clamp(100*sum(v*w for v,w in zip(vals, WEIGHTS)))

def greedy_risk(case: GreedyCase) -> float:
    vals=[case.local_rule_clarity,case.global_objective_clarity,case.greedy_choice_evidence,case.optimal_substructure_evidence,case.feasibility_check_quality,case.edge_case_coverage,case.counterexample_testing,case.traceability,case.robustness,case.governance_readiness]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20: return "strong greedy-algorithm discipline"
    if q >= 70 and r <= 35: return "usable greedy design with review needs"
    if r >= 55: return "high greedy-design risk"
    return "partial greedy discipline"

def load_cases(path: Path) -> list[GreedyCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [GreedyCase(r["case_name"],r["problem_context"],r["local_decision_rule"],float(r["local_rule_clarity"]),float(r["global_objective_clarity"]),float(r["greedy_choice_evidence"]),float(r["optimal_substructure_evidence"]),float(r["feasibility_check_quality"]),float(r["edge_case_coverage"]),float(r["counterexample_testing"]),float(r["traceability"]),float(r["robustness"]),float(r["governance_readiness"])) for r in rows]

def evaluate(cases: list[GreedyCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q,r=greedy_quality(c),greedy_risk(c)
        out.append({**asdict(c),"greedy_quality":round(q,3),"greedy_risk":round(r,3),"diagnostic":diagnose(q,r)})
    return out

def interval_scheduling(intervals: list[tuple[str,int,int]]) -> list[tuple[str,int,int]]:
    ordered=sorted(intervals, key=lambda row: row[2])
    selected=[]; current_finish=-10**9
    for interval in ordered:
        name,start,finish=interval
        if start >= current_finish:
            selected.append(interval); current_finish=finish
    return selected

def dijkstra(graph: dict[str, list[tuple[str,float]]], source: str) -> dict[str,float]:
    nodes=set(graph.keys())
    for edges in graph.values():
        for neighbor,_ in edges:
            nodes.add(neighbor)
    distances={node:float("inf") for node in nodes}
    distances[source]=0.0
    queue=[(0.0, source)]
    while queue:
        distance,node=heapq.heappop(queue)
        if distance > distances[node]: continue
        for neighbor,weight in graph.get(node, []):
            if weight < 0:
                raise ValueError("Dijkstra requires nonnegative edge weights.")
            candidate=distance+weight
            if candidate < distances[neighbor]:
                distances[neighbor]=candidate
                heapq.heappush(queue, (candidate, neighbor))
    return distances

def greedy_risk_queue(cases: list[dict[str, object]]) -> list[dict[str, object]]:
    return sorted(cases, key=lambda row: (-float(row["risk_score"]), str(row["case_id"])))

def algorithm_demos() -> dict[str, object]:
    intervals=[("A",0,6),("B",1,4),("C",3,5),("D",5,7),("E",6,10),("F",8,11)]
    graph={"A":[("B",2),("C",5)],"B":[("C",1),("D",4)],"C":[("D",1)],"D":[]}
    review_cases=[{"case_id":"R-001","risk_score":84},{"case_id":"R-002","risk_score":92},{"case_id":"R-003","risk_score":92},{"case_id":"R-004","risk_score":71}]
    return {"interval_scheduling_result":interval_scheduling(intervals),"dijkstra_distances":dijkstra(graph,"A"),"risk_queue_order":greedy_risk_queue(review_cases)}

def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    rows=evaluate(load_cases(root/"data"/"synthetic_greedy_cases.csv"))
    summary={"case_count":len(rows),"average_greedy_quality":round(mean(float(r["greedy_quality"]) for r in rows),3),"average_greedy_risk":round(mean(float(r["greedy_risk"]) for r in rows),3),"highest_quality_case":max(rows,key=lambda r:float(r["greedy_quality"]))["case_name"],"highest_risk_case":max(rows,key=lambda r:float(r["greedy_risk"]))["case_name"]}
    write_csv(root/"outputs"/"tables"/"greedy_algorithm_audit.csv", rows)
    write_csv(root/"outputs"/"tables"/"greedy_algorithm_audit_summary.csv", [summary])
    write_json(root/"outputs"/"json"/"greedy_algorithm_audit.json", rows)
    write_json(root/"outputs"/"json"/"greedy_algorithm_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"greedy_algorithm_demos.json", algorithm_demos())

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
