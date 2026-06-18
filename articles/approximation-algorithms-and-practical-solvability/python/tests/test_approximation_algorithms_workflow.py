from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from approximation_algorithms.examples import approximation_ratio_minimization, exact_subset_cover_size, greedy_set_cover, relative_gap_minimization, vertex_cover_approx
from calculators.approximation_quality_calculator import compute as quality_compute
from calculators.optimality_gap_calculator import compute as gap_compute

def test_approximation_examples():
    assert approximation_ratio_minimization(12, 8) == 1.5
    assert relative_gap_minimization(12, 10) == 0.2
    assert len(vertex_cover_approx([("A","B"),("B","C")])) > 0
    universe={"a","b","c"}
    sets={"S1":{"a","b"},"S2":{"c"}}
    assert greedy_set_cover(universe,sets) == ["S1","S2"]
    assert exact_subset_cover_size(universe,sets) == 2

def test_calculators():
    assert quality_compute([0.75]*10)["approximation_quality"] > 0
    assert gap_compute("minimization", 12, 10)["relative_gap"] == 0.2
