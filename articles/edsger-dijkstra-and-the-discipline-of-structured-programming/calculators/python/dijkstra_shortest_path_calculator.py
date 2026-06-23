from __future__ import annotations

import argparse
import heapq
from collections import defaultdict

parser = argparse.ArgumentParser(description="Run Dijkstra shortest path on edges like A,B,4;A,C,2.")
parser.add_argument("--edges", type=str, required=True)
parser.add_argument("--source", type=str, required=True)
args = parser.parse_args()

graph: dict[str, list[tuple[str, float]]] = defaultdict(list)
nodes: set[str] = set()
for edge in args.edges.split(";"):
    src, dst, weight = [part.strip() for part in edge.split(",")]
    w = float(weight)
    if w < 0:
        raise SystemExit("Dijkstra's algorithm requires nonnegative weights.")
    graph[src].append((dst, w))
    nodes.add(src)
    nodes.add(dst)
for node in nodes:
    graph.setdefault(node, [])

dist = {node: float("inf") for node in nodes}
dist[args.source] = 0.0
heap = [(0.0, args.source)]
settled = set()

while heap:
    d, node = heapq.heappop(heap)
    if node in settled:
        continue
    settled.add(node)
    for neighbor, weight in graph[node]:
        if d + weight < dist[neighbor]:
            dist[neighbor] = d + weight
            heapq.heappush(heap, (dist[neighbor], neighbor))

for node in sorted(dist):
    print(f"{node}={dist[node]:.6f}")
