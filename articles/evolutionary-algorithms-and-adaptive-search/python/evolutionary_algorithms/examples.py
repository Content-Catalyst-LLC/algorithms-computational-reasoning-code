from __future__ import annotations
import random
from statistics import mean, pstdev

def binary_fitness(candidate: list[int]) -> int:
    return sum(candidate)

def mutation(candidate: list[int], mutation_rate: float, seed: int = 20260617) -> list[int]:
    rng=random.Random(seed)
    return [1-bit if rng.random() < mutation_rate else bit for bit in candidate]

def crossover(a: list[int], b: list[int], seed: int = 20260617) -> list[int]:
    rng=random.Random(seed)
    point=rng.randint(1, len(a)-1)
    return a[:point]+b[point:]

def diversity(population: list[list[int]]) -> float:
    if len(population) <= 1:
        return 0.0
    distances=[]
    for i in range(len(population)):
        for j in range(i+1, len(population)):
            distances.append(sum(1 for a,b in zip(population[i],population[j]) if a!=b)/len(population[i]))
    return mean(distances)

def simple_ga(seed: int = 20260617, population_size: int = 20, genome_length: int = 12, generations: int = 20, mutation_rate: float = 0.03) -> dict[str, float]:
    rng=random.Random(seed)
    population=[[rng.randint(0,1) for _ in range(genome_length)] for _ in range(population_size)]
    for _ in range(generations):
        population=sorted(population, key=binary_fitness, reverse=True)
        survivors=population[:population_size//2]
        offspring=list(survivors)
        while len(offspring) < population_size:
            point=rng.randint(1, genome_length-1)
            pa=rng.choice(survivors); pb=rng.choice(survivors)
            child=pa[:point]+pb[point:]
            child=[1-bit if rng.random() < mutation_rate else bit for bit in child]
            offspring.append(child)
        population=offspring
    population=sorted(population, key=binary_fitness, reverse=True)
    return {"best_fitness":float(binary_fitness(population[0])),"final_diversity":diversity(population)}

def multi_seed_summary() -> dict[str, float]:
    runs=[simple_ga(seed=s) for s in range(20260610,20260620)]
    scores=[r["best_fitness"] for r in runs]
    divs=[r["final_diversity"] for r in runs]
    return {"mean_best_fitness":mean(scores),"stddev_best_fitness":pstdev(scores),"mean_final_diversity":mean(divs),"stddev_final_diversity":pstdev(divs)}
