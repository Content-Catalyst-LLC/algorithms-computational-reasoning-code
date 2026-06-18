from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from evolutionary_algorithms.examples import binary_fitness, crossover, diversity, multi_seed_summary, mutation, simple_ga
from calculators.evolutionary_search_quality_calculator import compute as quality_compute
from calculators.population_diversity_calculator import compute as diversity_compute

def test_evolutionary_examples():
    assert binary_fitness([1,0,1]) == 2
    assert len(mutation([1,0,1], 0.25)) == 3
    assert len(crossover([1,1,1],[0,0,0])) == 3
    assert diversity([[1,0],[0,1]]) == 1.0
    assert simple_ga()["best_fitness"] >= 0
    assert multi_seed_summary()["stddev_best_fitness"] >= 0

def test_calculators():
    assert quality_compute([0.75]*10)["evolutionary_search_quality"] > 0
    assert diversity_compute(10, 6, 20260617)["average_pairwise_hamming_diversity"] >= 0
