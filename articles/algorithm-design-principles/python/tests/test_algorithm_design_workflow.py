from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from algorithm_design.examples import binary_search, sorted_invariant, validate_nonnegative_weights
from calculators.design_quality_calculator import compute as quality_compute
from calculators.complexity_tradeoff_calculator import compute as tradeoff_compute

def test_design_examples():
    assert sorted_invariant([1,2,2,3]) is True
    assert sorted_invariant([1,3,2]) is False
    assert binary_search([1,3,5,8], 5) == 2
    assert validate_nonnegative_weights([("a","b",1.0)]) is True
    assert validate_nonnegative_weights([("a","b",-1.0)]) is False

def test_calculators():
    assert quality_compute([0.75]*10)["design_quality"] > 0
    assert tradeoff_compute(100, "nlogn", 0.4, 0.6)["tradeoff_score"] >= 0
