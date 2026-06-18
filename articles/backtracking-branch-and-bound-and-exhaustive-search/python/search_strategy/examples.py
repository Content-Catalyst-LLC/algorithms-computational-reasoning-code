from __future__ import annotations
import itertools

def exhaustive_subset_search(values: list[int], capacity: int) -> tuple[int, tuple[int, ...]]:
    best_value=-1
    best_subset=()
    for size in range(len(values)+1):
        for indices in itertools.combinations(range(len(values)), size):
            total=sum(values[i] for i in indices)
            if total <= capacity and total > best_value:
                best_value=total
                best_subset=indices
    return best_value, best_subset

def backtracking_permutations(items: list[str]) -> list[list[str]]:
    if not items:
        return [[]]
    out=[]
    for i,item in enumerate(items):
        for rest in backtracking_permutations(items[:i]+items[i+1:]):
            out.append([item]+rest)
    return out

def graph_coloring_backtracking(graph: dict[str, list[str]], colors: list[str]) -> dict[str, str] | None:
    nodes=list(graph.keys())
    assignment: dict[str,str]={}
    def valid(node: str, color: str) -> bool:
        return all(assignment.get(neighbor) != color for neighbor in graph.get(node, []))
    def search(index: int) -> bool:
        if index == len(nodes):
            return True
        node=nodes[index]
        for color in colors:
            if valid(node,color):
                assignment[node]=color
                if search(index+1):
                    return True
                assignment.pop(node,None)
        return False
    return assignment if search(0) else None

def search_space_growth(branching_factor: int, depth: int) -> int:
    return sum(branching_factor ** level for level in range(depth + 1))
