from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from search_sorting.examples import bfs_reachable, binary_search, linear_search, merge_sort
from calculators.search_sorting_quality_calculator import compute as quality_compute
from calculators.search_complexity_calculator import compute as complexity_compute

def test_search_sorting_examples():
    assert linear_search([1,2,3],2) == 1
    assert binary_search([1,2,3],3) == 2
    assert merge_sort([3,1,2]) == [1,2,3]
    assert bfs_reachable({"a":["b"],"b":["c"],"c":[]}, "a") == ["a","b","c"]

def test_calculators():
    assert quality_compute([0.75]*10)["search_sorting_quality"] > 0
    assert complexity_compute(1000,"binary_search",100)["estimated_steps"] > 0
