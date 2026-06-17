from pathlib import Path
import csv

def load_edges(root: Path) -> list[dict[str, str]]:
    with (root/"data"/"synthetic_architecture_dependency_edges.csv").open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def dependency_density(edges: list[tuple[str, str]]) -> float:
    nodes={n for e in edges for n in e}
    return len(edges)/max(1, len(nodes)*(len(nodes)-1))

def failure_reachability(edges: list[tuple[str, str]], start: str) -> set[str]:
    graph={}
    for source,target in edges:
        graph.setdefault(source,set()).add(target)
    seen=set()
    stack=list(graph.get(start,set()))
    while stack:
        node=stack.pop()
        if node not in seen:
            seen.add(node)
            stack.extend(graph.get(node,set())-seen)
    return seen
