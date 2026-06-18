from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from big_o_growth.workflow import cost, estimate_threshold

def test_growth_examples():
    assert cost(10, "linear") == 10
    assert cost(10, "quadratic") == 100
    assert estimate_threshold(100, "quadratic") == 10
