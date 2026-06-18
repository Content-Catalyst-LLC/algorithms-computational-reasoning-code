from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from search_strategy.examples import backtracking_permutations, exhaustive_subset_search, graph_coloring_backtracking, search_space_growth
from calculators.search_strategy_quality_calculator import compute as quality_compute
from calculators.search_space_growth_calculator import compute as growth_compute

def test_search_examples():
    assert exhaustive_subset_search([3,4,5,9], 10)[0] == 9
    assert len(backtracking_permutations(["A","B","C"])) == 6
    assert graph_coloring_backtracking({"A":["B"],"B":["A"]}, ["red","blue"]) is not None
    assert search_space_growth(2,3) == 15

def test_calculators():
    assert quality_compute([0.75]*10)["search_strategy_quality"] > 0
    assert growth_compute(3,4,"tree")["estimated_candidates"] == 121
