#!/usr/bin/env python3
import argparse, csv, json
from collections import deque
from heapq import heappop, heappush
from pathlib import Path

def load_graph(path):
    graph={}
    with Path(path).open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            graph.setdefault(r["source"], []).append((r["target"], float(r["weight"])))
            graph.setdefault(r["target"], [])
    return graph

def bfs_path(graph,start,goal):
    queue=deque([(start,[start])]); visited={start}
    while queue:
        node,path=queue.popleft()
        if node==goal: return path
        for neighbor,_ in graph.get(node,[]):
            if neighbor not in visited:
                visited.add(neighbor); queue.append((neighbor,path+[neighbor]))
    return []

def dijkstra_path(graph,start,goal):
    heap=[(0.0,start,[start])]; best={start:0.0}
    while heap:
        cost,node,path=heappop(heap)
        if node==goal: return {"path":path,"cost":round(cost,6)}
        if cost > best.get(node,float("inf")): continue
        for neighbor,weight in graph.get(node,[]):
            new_cost=cost+weight
            if new_cost < best.get(neighbor,float("inf")):
                best[neighbor]=new_cost; heappush(heap,(new_cost,neighbor,path+[neighbor]))
    return {"path":[],"cost":None}

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--edge-csv",default="data/synthetic_graph_edges.csv")
    p.add_argument("--source",default="A")
    p.add_argument("--target",default="E")
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    graph=load_graph(a.edge_csv)
    result={"source":a.source,"target":a.target,"bfs_path":bfs_path(graph,a.source,a.target),"dijkstra":dijkstra_path(graph,a.source,a.target)}
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"graph_search_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
