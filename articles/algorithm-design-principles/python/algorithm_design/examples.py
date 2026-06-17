from __future__ import annotations

def sorted_invariant(values: list[int]) -> bool:
    return all(values[i] <= values[i+1] for i in range(len(values)-1))

def binary_search(values: list[int], target: int) -> int:
    lo, hi = 0, len(values)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if values[mid] == target:
            return mid
        if values[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def validate_nonnegative_weights(edges: list[tuple[str, str, float]]) -> bool:
    return all(weight >= 0 for _, _, weight in edges)

def simple_complexity_estimate(n: int, strategy: str) -> dict[str, object]:
    if strategy == "linear":
        steps = n
    elif strategy == "quadratic":
        steps = n*n
    elif strategy == "nlogn":
        steps = n * max(1, n.bit_length())
    else:
        steps = n
    return {"n":n,"strategy":strategy,"estimated_steps":steps}
