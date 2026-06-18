from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json, math, random
from statistics import mean, pstdev

@dataclass(frozen=True)
class HeuristicCase:
    case_name: str
    problem_context: str
    heuristic_strategy: str
    purpose_clarity: float
    rule_transparency: float
    benchmark_evidence: float
    parameter_documentation: float
    robustness_testing: float
    edge_case_coverage: float
    fairness_review: float
    traceability: float
    monitoring_readiness: float
    governance_readiness: float

WEIGHTS=[0.12,0.12,0.12,0.10,0.10,0.10,0.08,0.08,0.08,0.10]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def heuristic_quality(case: HeuristicCase) -> float:
    vals=[case.purpose_clarity,case.rule_transparency,case.benchmark_evidence,case.parameter_documentation,case.robustness_testing,case.edge_case_coverage,case.fairness_review,case.traceability,case.monitoring_readiness,case.governance_readiness]
    return clamp(100*sum(v*w for v,w in zip(vals,WEIGHTS)))

def heuristic_risk(case: HeuristicCase) -> float:
    vals=[case.purpose_clarity,case.rule_transparency,case.benchmark_evidence,case.parameter_documentation,case.robustness_testing,case.edge_case_coverage,case.fairness_review,case.traceability,case.monitoring_readiness,case.governance_readiness]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20: return "strong heuristic governance discipline"
    if q >= 70 and r <= 35: return "usable heuristic with validation and monitoring needs"
    if r >= 55: return "high heuristic risk"
    return "partial heuristic discipline"

def load_cases(path: Path) -> list[HeuristicCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [HeuristicCase(r["case_name"],r["problem_context"],r["heuristic_strategy"],float(r["purpose_clarity"]),float(r["rule_transparency"]),float(r["benchmark_evidence"]),float(r["parameter_documentation"]),float(r["robustness_testing"]),float(r["edge_case_coverage"]),float(r["fairness_review"]),float(r["traceability"]),float(r["monitoring_readiness"]),float(r["governance_readiness"])) for r in rows]

def evaluate(cases: list[HeuristicCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q,r=heuristic_quality(c),heuristic_risk(c)
        out.append({**asdict(c),"heuristic_quality":round(q,3),"heuristic_risk":round(r,3),"diagnostic":diagnose(q,r)})
    return out

def route_cost(route: list[int], distance: list[list[float]]) -> float:
    return sum(distance[route[i]][route[i+1]] for i in range(len(route)-1))

def nearest_neighbor_route(distance: list[list[float]], start: int=0) -> dict[str, object]:
    n=len(distance)
    unvisited=set(range(n))
    route=[start]
    unvisited.remove(start)
    while unvisited:
        current=route[-1]
        next_node=min(unvisited, key=lambda node: distance[current][node])
        route.append(next_node)
        unvisited.remove(next_node)
    route.append(start)
    return {"route":route,"cost":route_cost(route,distance),"heuristic":"nearest_neighbor"}

def simulated_annealing_demo(seed: int=20260617) -> dict[str, object]:
    rng=random.Random(seed)
    def cost(x: float) -> float:
        return (x-3.0)**2 + 2.0*math.sin(4.0*x)
    current=rng.uniform(-5.0,8.0)
    current_cost=cost(current)
    best=current
    best_cost=current_cost
    temperature=5.0
    accepted_worse=0
    for _ in range(500):
        candidate=current+rng.uniform(-0.5,0.5)
        candidate_cost=cost(candidate)
        delta=candidate_cost-current_cost
        if delta < 0 or rng.random() < math.exp(-delta/max(temperature,1e-9)):
            if delta > 0:
                accepted_worse += 1
            current=candidate
            current_cost=candidate_cost
        if current_cost < best_cost:
            best=current
            best_cost=current_cost
        temperature *= 0.99
    return {"seed":seed,"best_x":best,"best_cost":best_cost,"accepted_worse_moves":accepted_worse}

def multi_seed_stability() -> dict[str, object]:
    costs=[simulated_annealing_demo(seed)["best_cost"] for seed in range(20260610,20260620)]
    return {"runs":len(costs),"mean_best_cost":mean(costs),"stddev_best_cost":pstdev(costs),"min_best_cost":min(costs),"max_best_cost":max(costs)}

def algorithm_demos() -> dict[str, object]:
    distance=[[0,2,9,10],[1,0,6,4],[15,7,0,8],[6,3,12,0]]
    return {"nearest_neighbor_route":nearest_neighbor_route(distance),"simulated_annealing_demo":simulated_annealing_demo(),"multi_seed_stability":multi_seed_stability()}

def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    rows=evaluate(load_cases(root/"data"/"synthetic_heuristic_cases.csv"))
    summary={"case_count":len(rows),"average_heuristic_quality":round(mean(float(r["heuristic_quality"]) for r in rows),3),"average_heuristic_risk":round(mean(float(r["heuristic_risk"]) for r in rows),3),"highest_quality_case":max(rows,key=lambda r:float(r["heuristic_quality"]))["case_name"],"highest_risk_case":max(rows,key=lambda r:float(r["heuristic_risk"]))["case_name"]}
    write_csv(root/"outputs"/"tables"/"heuristic_design_audit.csv", rows)
    write_csv(root/"outputs"/"tables"/"heuristic_design_audit_summary.csv", [summary])
    write_json(root/"outputs"/"json"/"heuristic_design_audit.json", rows)
    write_json(root/"outputs"/"json"/"heuristic_design_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"heuristic_algorithm_demos.json", algorithm_demos())

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
