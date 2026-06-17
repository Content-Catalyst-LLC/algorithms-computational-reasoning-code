from __future__ import annotations

from collections import deque
import heapq


def stack_order(items: list[str]) -> list[str]:
    stack: list[str] = []
    for item in items:
        stack.append(item)
    return [stack.pop() for _ in range(len(stack))]


def queue_order(items: list[str]) -> list[str]:
    q = deque(items)
    return [q.popleft() for _ in range(len(q))]


def priority_order(tasks: list[tuple[int, str]]) -> list[str]:
    heap = [(priority, label) for priority, label in tasks]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(len(heap))]


def adjacency_neighbors(edges: list[tuple[str, str]]) -> dict[str, list[str]]:
    graph: dict[str, list[str]] = {}
    for source, target in edges:
        graph.setdefault(source, []).append(target)
        graph.setdefault(target, [])
    return graph


def demo_structures() -> dict[str, object]:
    return {
        "stack_order": stack_order(["first", "second", "third"]),
        "queue_order": queue_order(["first", "second", "third"]),
        "priority_order": priority_order([(3, "routine"), (1, "urgent"), (2, "soon")]),
        "graph_neighbors": adjacency_neighbors([("A", "B"), ("A", "C"), ("B", "D")]),
        "interpretation": "Each structure changes the natural reasoning pattern: recency, service order, priority, or relationship traversal.",
    }
