from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from dynamic_programming.examples import edit_distance, fibonacci_memo, knapsack_01, state_space_size
from calculators.dynamic_programming_quality_calculator import compute as quality_compute
from calculators.state_space_memory_calculator import compute as memory_compute

def test_dynamic_programming_examples():
    assert fibonacci_memo(10) == 55
    assert edit_distance("kitten", "sitting") == 3
    assert knapsack_01([6,10,12], [1,2,3], 5) == 22
    assert state_space_size([2,3,4]) == 24

def test_calculators():
    assert quality_compute([0.75]*10)["dynamic_programming_quality"] > 0
    assert memory_compute([10,10], 8, 4)["total_memory_bytes"] == 1200
