from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from complexity_scalability.workflow import estimate_threshold, growth_cost

def test_growth_examples():
    assert growth_cost(10, "linear") == 10
    assert growth_cost(10, "quadratic") == 100
    assert estimate_threshold(100, "quadratic") == 10
