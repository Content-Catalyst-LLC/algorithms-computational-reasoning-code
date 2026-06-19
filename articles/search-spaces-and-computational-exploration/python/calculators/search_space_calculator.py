#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def branching_state_count(branching_factor, depth): return sum(branching_factor ** i for i in range(depth + 1))
def path_cost(edge_costs): return sum(edge_costs)
def heuristic_score(known_cost, estimated_remaining_cost): return known_cost + estimated_remaining_cost

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--branching-factor",type=int,default=3); p.add_argument("--depth",type=int,default=5)
    p.add_argument("--edge-costs",default="2.5,3.0,1.25,4.75"); p.add_argument("--known-cost",type=float,default=8.0); p.add_argument("--estimated-remaining-cost",type=float,default=5.5)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json")); a=p.parse_args()
    costs=[float(x) for x in a.edge_costs.split(",") if x.strip()]
    result={"branching_factor":a.branching_factor,"depth":a.depth,"state_count":branching_state_count(a.branching_factor,a.depth),"edge_costs":costs,"path_cost":round(path_cost(costs),6),"known_cost":a.known_cost,"estimated_remaining_cost":a.estimated_remaining_cost,"heuristic_score":round(heuristic_score(a.known_cost,a.estimated_remaining_cost),6)}
    a.output_dir.mkdir(parents=True,exist_ok=True); (a.output_dir/"search_space_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8"); print(json.dumps(result,indent=2))
