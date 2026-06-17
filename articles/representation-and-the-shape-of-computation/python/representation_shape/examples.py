from __future__ import annotations

from dataclasses import dataclass
from collections import deque


@dataclass(frozen=True)
class Graph:
    edges: dict[str, list[tuple[str, float]]]


def shortest_neighbor_demo(graph: Graph, start: str) -> tuple[str, float] | None:
    neighbors = graph.edges.get(start, [])
    if not neighbors:
        return None
    return min(neighbors, key=lambda item: item[1])


def stack_demo(items: list[str]) -> list[str]:
    stack: list[str] = []
    for item in items:
        stack.append(item)
    return [stack.pop() for _ in range(len(stack))]


def queue_demo(items: list[str]) -> list[str]:
    q = deque(items)
    return [q.popleft() for _ in range(len(q))]


def demo_shapes() -> dict[str, object]:
    graph = Graph({"A": [("B", 3.0), ("C", 1.5)]})
    return {
        "graph_shortest_neighbor": shortest_neighbor_demo(graph, "A"),
        "stack_order": stack_demo(["first", "second", "third"]),
        "queue_order": queue_demo(["first", "second", "third"]),
        "interpretation": "Representation shape changes natural operations: graph traversal, last-in-first-out stack behavior, and first-in-first-out queue behavior.",
    }
