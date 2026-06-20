from __future__ import annotations
from collections import deque
from dataclasses import asdict, dataclass
from heapq import heappop, heappush
from pathlib import Path
from statistics import mean
import csv, json

@dataclass(frozen=True)
class GraphSearchCase:
    case_name: str
    graph_context: str
    routing_goal: str
    graph_definition: float
    node_edge_clarity: float
    weight_documentation: float
    constraint_documentation: float
    traversal_traceability: float
    alternative_path_reporting: float
    failure_handling: float
    update_freshness: float
    distributional_review: float
    governance_review: float
    communication_clarity: float

WEIGHTS=[0.11,0.11,0.10,0.10,0.10,0.09,0.09,0.08,0.08,0.09,0.05]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def graph_search_score(case: GraphSearchCase) -> float:
    vals=[case.graph_definition,case.node_edge_clarity,case.weight_documentation,case.constraint_documentation,case.traversal_traceability,case.alternative_path_reporting,case.failure_handling,case.update_freshness,case.distributional_review,case.governance_review,case.communication_clarity]
    return clamp(100.0*sum(v*w for v,w in zip(vals,WEIGHTS)))

def graph_search_risk(case: GraphSearchCase) -> float:
    vals=[case.graph_definition,case.node_edge_clarity,case.weight_documentation,case.constraint_documentation,case.traversal_traceability,case.alternative_path_reporting,case.failure_handling,case.update_freshness,case.distributional_review,case.governance_review]
    return clamp(100.0*mean(1.0-v for v in vals))

def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong graph-search discipline"
    if score >= 70 and risk <= 35:
        return "usable routing design with review needs"
    if risk >= 55:
        return "high risk; graph definition, edge weights, constraints, traceability, failure handling, or governance may be underdefined"
    return "partial discipline; strengthen graph representation, path-cost documentation, alternatives, failure handling, freshness, and governance"

def load_graph(edge_path: Path) -> dict[str, list[tuple[str,float]]]:
    graph: dict[str, list[tuple[str,float]]] = {}
    with edge_path.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            graph.setdefault(r["source"], []).append((r["target"], float(r["weight"])))
            graph.setdefault(r["target"], [])
    return graph

def bfs_path(graph: dict[str,list[tuple[str,float]]], start: str, goal: str) -> list[str]:
    queue=deque([(start,[start])])
    visited={start}
    while queue:
        node,path=queue.popleft()
        if node==goal:
            return path
        for neighbor,_ in graph.get(node,[]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor,path+[neighbor]))
    return []

def dfs_order(graph: dict[str,list[tuple[str,float]]], start: str) -> list[str]:
    visited=set()
    order=[]
    def visit(node: str) -> None:
        visited.add(node)
        order.append(node)
        for neighbor,_ in graph.get(node,[]):
            if neighbor not in visited:
                visit(neighbor)
    visit(start)
    return order

def dijkstra_path(graph: dict[str,list[tuple[str,float]]], start: str, goal: str) -> dict[str,object]:
    heap=[(0.0,start,[start])]
    best={start:0.0}
    while heap:
        cost,node,path=heappop(heap)
        if node==goal:
            return {"path":path,"cost":round(cost,6)}
        if cost > best.get(node,float("inf")):
            continue
        for neighbor,weight in graph.get(node,[]):
            new_cost=cost+weight
            if new_cost < best.get(neighbor,float("inf")):
                best[neighbor]=new_cost
                heappush(heap,(new_cost,neighbor,path+[neighbor]))
    return {"path":[],"cost":None}

def path_cost(graph: dict[str,list[tuple[str,float]]], path: list[str]) -> float:
    total=0.0
    for left,right in zip(path,path[1:]):
        edge_weights={neighbor: weight for neighbor,weight in graph[left]}
        total += edge_weights[right]
    return round(total,6)

def edge_count(graph: dict[str,list[tuple[str,float]]]) -> int:
    return sum(len(edges) for edges in graph.values())

def graph_density(node_count: int, directed_edge_count: int) -> float:
    possible_edges=node_count*(node_count-1)
    return round(directed_edge_count/possible_edges,6) if possible_edges else 0.0

def load_cases(path: Path) -> list[GraphSearchCase]:
    fields=["graph_definition","node_edge_clarity","weight_documentation","constraint_documentation","traversal_traceability","alternative_path_reporting","failure_handling","update_freshness","distributional_review","governance_review","communication_clarity"]
    with path.open(newline="", encoding="utf-8") as f:
        return [GraphSearchCase(r["case_name"],r["graph_context"],r["routing_goal"],*[float(r[k]) for k in fields]) for r in csv.DictReader(f)]

def evaluate(cases: list[GraphSearchCase]) -> list[dict[str,object]]:
    rows=[]
    for c in cases:
        score=graph_search_score(c)
        risk=graph_search_risk(c)
        rows.append({**asdict(c),"graph_search_score":round(score,3),"graph_search_risk":round(risk,3),"diagnostic":diagnose(score,risk)})
    return rows

def calculator_examples(graph: dict[str,list[tuple[str,float]]]) -> list[dict[str,object]]:
    bfs=bfs_path(graph,"A","E")
    weighted=dijkstra_path(graph,"A","E")
    dfs=dfs_order(graph,"A")
    return [
        {"example":"bfs_path","source":"A","target":"E","path":"->".join(bfs),"edge_count":len(bfs)-1 if bfs else None},
        {"example":"dfs_order","source":"A","visit_order":"->".join(dfs),"visited_count":len(dfs)},
        {"example":"dijkstra_shortest_path","source":"A","target":"E","path":"->".join(weighted["path"]),"path_cost":weighted["cost"]},
        {"example":"graph_density","node_count":len(graph),"edge_count":edge_count(graph),"density":graph_density(len(graph),edge_count(graph))}
    ]

def write_csv(path: Path, rows: list[dict[str,object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    graph=load_graph(root/"data"/"synthetic_graph_edges.csv")
    audit=evaluate(load_cases(root/"data"/"synthetic_graph_search_cases.csv"))
    calc=calculator_examples(graph)
    summary={
        "case_count":len(audit),
        "average_graph_search_score":round(mean(float(r["graph_search_score"]) for r in audit),3),
        "average_graph_search_risk":round(mean(float(r["graph_search_risk"]) for r in audit),3),
        "highest_score_case":max(audit,key=lambda r:float(r["graph_search_score"]))["case_name"],
        "highest_risk_case":max(audit,key=lambda r:float(r["graph_search_risk"]))["case_name"]
    }
    for name, rows in [("graph_search_audit",audit),("graph_search_audit_summary",[summary]),("graph_search_calculator_examples",calc)]:
        write_csv(root/"outputs"/"tables"/f"{name}.csv", rows)
        write_json(root/"outputs"/"json"/f"{name}.json", rows)

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
