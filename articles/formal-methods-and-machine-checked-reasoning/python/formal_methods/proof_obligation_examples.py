from __future__ import annotations


def sortedness_obligation(values: list[int]) -> bool:
    return all(values[index] <= values[index + 1] for index in range(len(values) - 1))


def permutation_obligation(original: list[int], candidate: list[int]) -> bool:
    return sorted(original) == sorted(candidate)


def verified_sort_demo(values: list[int]) -> dict[str, object]:
    output = sorted(values)
    return {
        "input": values,
        "output": output,
        "sortedness_obligation": sortedness_obligation(output),
        "permutation_obligation": permutation_obligation(values, output),
        "interpretation": "This is an executable teaching check, not a machine-checked proof assistant artifact.",
    }
