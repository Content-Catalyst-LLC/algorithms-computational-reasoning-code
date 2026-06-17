from __future__ import annotations

from collections import deque
import heapq
import math


def adjacency_list(edges: list[tuple[str, str]]) -> dict[str, list[str]]:
    graph: dict[str, list[str]] = {}
    for source, target in edges:
        graph.setdefault(source, []).append(target)
        graph.setdefault(target, [])
    return graph


def bfs_distances(graph: dict[str, list[str]], source: str) -> dict[str, int]:
    distances = {source: 0}
    queue = deque([source])
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    return distances


def detect_cycle_dfs(graph: dict[str, list[str]]) -> bool:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for neighbor in graph[node]:
            if visit(neighbor):
                return True
        visiting.remove(node)
        visited.add(node)
        return False

    return any(visit(node) for node in graph)


def dijkstra(graph: dict[str, list[tuple[str, float]]], source: str) -> dict[str, float]:
    distances = {node: math.inf for node in graph}
    distances[source] = 0.0
    heap: list[tuple[float, str]] = [(0.0, source)]

    while heap:
        distance, node = heapq.heappop(heap)
        if distance > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            candidate = distance + weight
            if candidate < distances.get(neighbor, math.inf):
                distances[neighbor] = candidate
                heapq.heappush(heap, (candidate, neighbor))
    return distances


def demo_graph() -> dict[str, object]:
    edges = [
        ("source", "review"),
        ("review", "approval"),
        ("review", "escalation"),
        ("approval", "archive"),
        ("escalation", "archive"),
        ("review", "quality_check"),
        ("quality_check", "approval"),
    ]
    graph = adjacency_list(edges)
    weighted_graph = {
        "source": [("review", 1.0)],
        "review": [("approval", 1.0), ("escalation", 1.5), ("quality_check", 1.0)],
        "quality_check": [("approval", 1.0)],
        "approval": [("archive", 1.0)],
        "escalation": [("archive", 1.0)],
        "archive": [],
    }
    return {
        "adjacency_list": graph,
        "bfs_distances_from_source": bfs_distances(graph, "source"),
        "contains_directed_cycle": detect_cycle_dfs(graph),
        "dijkstra_distances_from_source": dijkstra(weighted_graph, "source"),
        "interpretation": "Adjacency makes relationships traversable; BFS reveals hop distance; cycle checks identify circular dependency; Dijkstra computes low-cost paths.",
    }
