from pathlib import Path
import json
from heuristics_metaheuristics.workflow import run_workflow
from heuristics_metaheuristics.examples import hill_climb, multi_seed_costs, nearest_neighbor_route, route_cost, simulated_annealing

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    distance=[[0,2,9,10],[1,0,6,4],[15,7,0,8],[6,3,12,0]]
    route=nearest_neighbor_route(distance)
    demos={
        "nearest_neighbor_route": route,
        "nearest_neighbor_cost": route_cost(route, distance),
        "hill_climb_final_x": hill_climb(10.0),
        "simulated_annealing": simulated_annealing(),
        "multi_seed_costs": multi_seed_costs()
    }
    (root/"outputs"/"json"/"heuristic_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Heuristic and metaheuristic workflow complete.")
