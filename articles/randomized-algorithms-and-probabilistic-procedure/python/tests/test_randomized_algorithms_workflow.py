from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from randomized_algorithms.examples import amplification_failure_probability, monte_carlo_pi, randomized_quicksort, sample_mean_summary
from calculators.randomized_algorithm_quality_calculator import compute as quality_compute
from calculators.monte_carlo_sample_size_calculator import compute as sample_size_compute

def test_randomized_examples():
    assert randomized_quicksort([3,1,2]) == [1,2,3]
    assert abs(monte_carlo_pi(1000) - 3.14) < 0.3
    assert amplification_failure_probability(0.1, 3) == 0.0010000000000000002
    assert sample_mean_summary([1,2,3], 2, 10)["population_mean"] == 2

def test_calculators():
    assert quality_compute([0.75]*10)["randomized_algorithm_quality"] > 0
    assert sample_size_compute(0.05, 1.96, 0.5)["recommended_sample_size"] > 0
