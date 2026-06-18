from __future__ import annotations
import random
from statistics import mean, pstdev

def randomized_quicksort(values: list[int], seed: int = 20260617) -> list[int]:
    rng=random.Random(seed)
    def sort(xs: list[int]) -> list[int]:
        if len(xs) <= 1:
            return list(xs)
        pivot=rng.choice(xs)
        return sort([x for x in xs if x < pivot]) + [x for x in xs if x == pivot] + sort([x for x in xs if x > pivot])
    return sort(values)

def monte_carlo_pi(trials: int = 5000, seed: int = 20260617) -> float:
    rng=random.Random(seed)
    inside=0
    for _ in range(trials):
        x=rng.random(); y=rng.random()
        inside += int(x*x + y*y <= 1.0)
    return 4.0*inside/trials

def amplification_failure_probability(single_trial_failure: float, trials: int) -> float:
    return single_trial_failure ** trials

def sample_mean_summary(population: list[float], sample_size: int, trials: int, seed: int = 20260617) -> dict[str, float]:
    rng=random.Random(seed)
    means=[mean([rng.choice(population) for _ in range(sample_size)]) for _ in range(trials)]
    return {"average_sample_mean":mean(means), "sample_mean_stddev":pstdev(means), "population_mean":mean(population)}
