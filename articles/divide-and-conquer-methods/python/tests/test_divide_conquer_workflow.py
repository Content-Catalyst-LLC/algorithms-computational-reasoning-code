from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from divide_conquer.examples import binary_search, merge_sort, quicksort
from calculators.divide_conquer_quality_calculator import compute as quality_compute
from calculators.recurrence_complexity_calculator import estimate

def test_divide_conquer_examples():
    assert merge_sort([3,1,2]) == [1,2,3]
    assert quicksort([3,1,2,3]) == [1,2,3,3]
    assert binary_search([1,2,3],3) == 2
    assert binary_search([1,2,3],9) == -1

def test_calculators():
    assert quality_compute([0.75]*10)["divide_conquer_quality"] > 0
    assert estimate(1024,2,2,1.0)["estimated_depth"] > 0
