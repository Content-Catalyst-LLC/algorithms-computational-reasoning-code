from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from heuristics_metaheuristics.examples import hill_climb, multi_seed_costs, nearest_neighbor_route, route_cost, simulated_annealing
from calculators.heuristic_quality_calculator import compute as quality_compute
from calculators.local_search_risk_calculator import compute as risk_compute

def test_heuristic_examples():
    distance=[[0,2,9],[1,0,6],[15,7,0]]
    route=nearest_neighbor_route(distance)
    assert route[0] == route[-1]
    assert route_cost(route, distance) > 0
    assert abs(hill_climb(10.0) - 2.5) < 1.0
    assert "best_cost" in simulated_annealing()
    assert multi_seed_costs()["stddev"] >= 0

def test_calculators():
    assert quality_compute([0.75]*10)["heuristic_quality"] > 0
    assert risk_compute(0.35,0.25,0.30,0.20)["local_search_risk"] > 0
