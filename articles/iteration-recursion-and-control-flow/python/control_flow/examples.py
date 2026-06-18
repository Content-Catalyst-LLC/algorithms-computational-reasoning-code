from __future__ import annotations

def iterative_sum(values: list[float]) -> float:
    total=0.0
    for value in values:
        total += value
    return total

def recursive_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("factorial requires n >= 0")
    if n == 0:
        return 1
    return n * recursive_factorial(n-1)

def nondecreasing(values: list[int]) -> bool:
    return all(values[i] <= values[i+1] for i in range(len(values)-1))

def bounded_retry_outcomes(max_attempts: int, success_at: int | None) -> list[str]:
    outcomes=[]
    for attempt in range(1, max_attempts+1):
        if success_at is not None and attempt >= success_at:
            outcomes.append(f"attempt_{attempt}:success")
            break
        outcomes.append(f"attempt_{attempt}:retry")
    else:
        outcomes.append("exhausted")
    return outcomes
