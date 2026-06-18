from __future__ import annotations
import heapq

def interval_scheduling(intervals: list[tuple[str,int,int]]) -> list[tuple[str,int,int]]:
    selected=[]; current_finish=-10**9
    for interval in sorted(intervals, key=lambda row: row[2]):
        if interval[1] >= current_finish:
            selected.append(interval); current_finish=interval[2]
    return selected

def dijkstra(graph: dict[str, list[tuple[str,float]]], source: str) -> dict[str,float]:
    nodes=set(graph.keys())
    for edges in graph.values():
        for n,_ in edges: nodes.add(n)
    dist={n:float("inf") for n in nodes}; dist[source]=0.0
    pq=[(0.0,source)]
    while pq:
        d,u=heapq.heappop(pq)
        if d > dist[u]: continue
        for v,w in graph.get(u,[]):
            if w < 0: raise ValueError("nonnegative edge weights required")
            nd=d+w
            if nd < dist[v]:
                dist[v]=nd; heapq.heappush(pq,(nd,v))
    return dist

def huffman_merge_order(frequencies: dict[str,int]) -> list[tuple[int,str]]:
    heap=[(weight,symbol) for symbol,weight in frequencies.items()]
    heapq.heapify(heap); trace=[]
    next_id=0
    while len(heap) > 1:
        w1,s1=heapq.heappop(heap); w2,s2=heapq.heappop(heap)
        merged=f"N{next_id}"; next_id += 1
        trace.append((w1+w2, f"{s1}+{s2}->{merged}"))
        heapq.heappush(heap,(w1+w2,merged))
    return trace

def nearest_neighbor_route(points: list[str], distances: dict[tuple[str,str],float], start: str) -> list[str]:
    remaining=set(points); route=[start]; remaining.discard(start)
    while remaining:
        current=route[-1]
        nxt=min(remaining, key=lambda p: distances.get((current,p), distances.get((p,current), float("inf"))))
        route.append(nxt); remaining.remove(nxt)
    return route
