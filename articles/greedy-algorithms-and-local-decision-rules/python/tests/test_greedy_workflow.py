from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from greedy_algorithms.examples import dijkstra, huffman_merge_order, interval_scheduling, nearest_neighbor_route
from calculators.greedy_quality_calculator import compute as quality_compute
from calculators.local_choice_risk_calculator import compute as risk_compute

def test_greedy_examples():
    assert interval_scheduling([("A",0,6),("B",1,4),("C",5,7)]) == [("B",1,4),("C",5,7)]
    assert dijkstra({"A":[("B",2),("C",5)],"B":[("C",1)],"C":[]}, "A")["C"] == 3
    assert len(huffman_merge_order({"A":5,"B":9,"C":12})) == 2
    assert nearest_neighbor_route(["A","B","C"], {("A","B"):3,("A","C"):5,("B","C"):1}, "A")[0] == "A"

def test_calculators():
    assert quality_compute([0.75]*10)["greedy_quality"] > 0
    assert risk_compute(0.7,0.6,0.7,0.8,0.8,0.6)["local_choice_risk"] >= 0
