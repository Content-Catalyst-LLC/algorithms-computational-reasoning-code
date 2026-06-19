from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv, json

@dataclass(frozen=True)
class SearchSpaceCase:
    case_name: str
    problem_context: str
    exploration_goal: str
    state_clarity: float
    transition_clarity: float
    goal_definition: float
    constraint_documentation: float
    heuristic_transparency: float
    pruning_discipline: float
    frontier_discipline: float
    coverage_reporting: float
    stopping_clarity: float
    traceability: float
    governance_review: float
    communication_clarity: float

WEIGHTS=[0.10,0.10,0.10,0.09,0.09,0.08,0.08,0.09,0.09,0.09,0.06,0.03]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def search_space_score(case: SearchSpaceCase) -> float:
    vals=[case.state_clarity,case.transition_clarity,case.goal_definition,case.constraint_documentation,case.heuristic_transparency,case.pruning_discipline,case.frontier_discipline,case.coverage_reporting,case.stopping_clarity,case.traceability,case.governance_review,case.communication_clarity]
    return clamp(100*sum(v*w for v,w in zip(vals,WEIGHTS)))

def search_space_risk(case: SearchSpaceCase) -> float:
    vals=[case.state_clarity,case.transition_clarity,case.goal_definition,case.constraint_documentation,case.heuristic_transparency,case.pruning_discipline,case.coverage_reporting,case.stopping_clarity,case.traceability,case.governance_review]
    return clamp(100*mean(1-v for v in vals))

def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20: return "strong search-space discipline"
    if score >= 70 and risk <= 35: return "usable search-space design with review needs"
    if risk >= 55: return "high risk; unclear states, transitions, goals, constraints, heuristics, pruning, coverage, stopping, or traceability may distort exploration"
    return "partial discipline; strengthen state representation, transitions, goals, constraints, heuristic documentation, pruning records, coverage, stopping criteria, and traceability"

def branching_state_count(branching_factor: int, depth: int) -> int:
    return sum(branching_factor ** i for i in range(depth + 1))

def path_cost(edge_costs: list[float]) -> float:
    return round(sum(edge_costs), 6)

def heuristic_score(known_cost: float, estimated_remaining_cost: float) -> float:
    return round(known_cost + estimated_remaining_cost, 6)

def coverage_ratio(explored_states: float, reachable_states: float) -> float:
    return round(explored_states / reachable_states, 6) if reachable_states else 0.0

def pruning_ratio(pruned_states: float, generated_states: float) -> float:
    return round(pruned_states / generated_states, 6) if generated_states else 0.0

def load_cases(path: Path) -> list[SearchSpaceCase]:
    fields=["state_clarity","transition_clarity","goal_definition","constraint_documentation","heuristic_transparency","pruning_discipline","frontier_discipline","coverage_reporting","stopping_clarity","traceability","governance_review","communication_clarity"]
    with path.open(newline="", encoding="utf-8") as f:
        return [SearchSpaceCase(r["case_name"],r["problem_context"],r["exploration_goal"],*[float(r[k]) for k in fields]) for r in csv.DictReader(f)]

def evaluate(cases: list[SearchSpaceCase]) -> list[dict[str,object]]:
    rows=[]
    for c in cases:
        score=search_space_score(c); risk=search_space_risk(c)
        rows.append({**asdict(c),"search_space_score":round(score,3),"search_space_risk":round(risk,3),"diagnostic":diagnose(score,risk)})
    return rows

def calculator_examples() -> list[dict[str,object]]:
    return [
        {"example":"branching_state_count","branching_factor":3,"depth":5,"state_count":branching_state_count(3,5)},
        {"example":"path_cost","edge_costs":[2.5,3.0,1.25,4.75],"path_cost":path_cost([2.5,3.0,1.25,4.75])},
        {"example":"heuristic_score","known_cost":8.0,"estimated_remaining_cost":5.5,"heuristic_score":heuristic_score(8.0,5.5)},
        {"example":"coverage_ratio","explored_states":850,"reachable_states":5000,"coverage_ratio":coverage_ratio(850,5000)},
        {"example":"pruning_ratio","pruned_states":1200,"generated_states":4200,"pruning_ratio":pruning_ratio(1200,4200)}]

def calculator_input_summary(path: Path) -> list[dict[str,object]]:
    rows=[]
    with path.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            costs=[float(x) for x in r["edge_costs"].split(";") if x.strip()]
            rows.append({**r,"state_count":branching_state_count(int(r["branching_factor"]), int(r["depth"])),"path_cost":path_cost(costs),"heuristic_score":heuristic_score(float(r["known_cost"]), float(r["estimated_remaining_cost"])),"coverage_ratio":coverage_ratio(float(r["explored_states"]), float(r["reachable_states"])),"pruning_ratio":pruning_ratio(float(r["pruned_states"]), float(r["generated_states"]))})
    return rows

def write_csv(path: Path, rows: list[dict[str,object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True); path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    audit=evaluate(load_cases(root/"data"/"synthetic_search_space_cases.csv"))
    calc_summary=calculator_input_summary(root/"data"/"synthetic_search_calculator_inputs.csv")
    summary={"case_count":len(audit),"average_search_space_score":round(mean(float(r["search_space_score"]) for r in audit),3),"average_search_space_risk":round(mean(float(r["search_space_risk"]) for r in audit),3),"highest_score_case":max(audit,key=lambda r:float(r["search_space_score"]))["case_name"],"highest_risk_case":max(audit,key=lambda r:float(r["search_space_risk"]))["case_name"]}
    for name, rows in [("search_space_exploration_audit",audit),("search_space_exploration_audit_summary",[summary]),("search_space_calculator_input_summary",calc_summary),("search_space_calculator_examples",calculator_examples())]:
        write_csv(root/"outputs"/"tables"/f"{name}.csv", rows); write_json(root/"outputs"/"json"/f"{name}.json", rows)

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
