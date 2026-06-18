from __future__ import annotations
import math, random
from statistics import mean, pstdev

def route_cost(route: list[int], distance: list[list[float]]) -> float:
    return sum(distance[route[i]][route[i+1]] for i in range(len(route)-1))

def nearest_neighbor_route(distance: list[list[float]], start: int=0) -> list[int]:
    unvisited=set(range(len(distance)))
    route=[start]
    unvisited.remove(start)
    while unvisited:
        current=route[-1]
        next_node=min(unvisited, key=lambda node: distance[current][node])
        route.append(next_node)
        unvisited.remove(next_node)
    route.append(start)
    return route

def hill_climb(start: float, steps: int=200, step_size: float=0.05) -> float:
    def cost(x: float) -> float:
        return (x - 2.5) ** 2
    current=start
    for _ in range(steps):
        candidates=[current-step_size, current+step_size]
        best=min(candidates+[current], key=cost)
        if cost(best) < cost(current):
            current=best
    return current

def simulated_annealing(seed: int=20260617, iterations: int=500) -> dict[str, float]:
    rng=random.Random(seed)
    def cost(x: float) -> float:
        return (x-3.0)**2 + 2.0*math.sin(4.0*x)
    current=rng.uniform(-5.0,8.0)
    current_cost=cost(current)
    best=current
    best_cost=current_cost
    temperature=5.0
    for _ in range(iterations):
        candidate=current+rng.uniform(-0.5,0.5)
        candidate_cost=cost(candidate)
        delta=candidate_cost-current_cost
        if delta < 0 or rng.random() < math.exp(-delta/max(temperature,1e-9)):
            current=candidate
            current_cost=candidate_cost
        if current_cost < best_cost:
            best=current
            best_cost=current_cost
        temperature *= 0.99
    return {"best_x":best,"best_cost":best_cost}

def multi_seed_costs() -> dict[str, float]:
    costs=[simulated_annealing(seed)["best_cost"] for seed in range(20260610,20260620)]
    return {"mean":mean(costs),"stddev":pstdev(costs),"min":min(costs),"max":max(costs)}
