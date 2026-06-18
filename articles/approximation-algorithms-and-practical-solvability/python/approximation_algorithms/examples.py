from __future__ import annotations
import itertools

def approximation_ratio_minimization(algorithm_value: float, optimum_or_bound: float) -> float:
    if optimum_or_bound <= 0:
        raise ValueError("optimum_or_bound must be positive")
    return algorithm_value / optimum_or_bound

def relative_gap_minimization(algorithm_value: float, lower_bound: float) -> float:
    if lower_bound <= 0:
        raise ValueError("lower_bound must be positive")
    return (algorithm_value - lower_bound) / lower_bound

def vertex_cover_approx(edges: list[tuple[str,str]]) -> set[str]:
    uncovered=set(tuple(sorted(edge)) for edge in edges)
    cover=set()
    while uncovered:
        u,v=next(iter(uncovered))
        cover.update([u,v])
        uncovered={edge for edge in uncovered if u not in edge and v not in edge}
    return cover

def greedy_set_cover(universe: set[str], sets: dict[str,set[str]]) -> list[str]:
    uncovered=set(universe)
    chosen=[]
    while uncovered:
        best=max(sets, key=lambda name: len(sets[name] & uncovered))
        if not (sets[best] & uncovered):
            raise ValueError("Universe cannot be covered")
        chosen.append(best)
        uncovered -= sets[best]
    return chosen

def exact_subset_cover_size(universe: set[str], sets: dict[str,set[str]]) -> int | None:
    names=list(sets)
    for r in range(1, len(names)+1):
        for combo in itertools.combinations(names, r):
            covered=set()
            for name in combo:
                covered |= sets[name]
            if covered >= universe:
                return r
    return None
