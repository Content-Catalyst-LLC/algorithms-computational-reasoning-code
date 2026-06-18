from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
from collections import defaultdict, deque
from statistics import mean
import csv, json

@dataclass(frozen=True)
class KnowledgeGraphCase:
    case_name: str
    system_context: str
    retrieval_goal: str
    graph_schema_clarity: float
    entity_resolution: float
    relationship_quality: float
    ontology_discipline: float
    semantic_indexing: float
    path_retrieval: float
    hybrid_retrieval: float
    provenance_support: float
    evaluation_discipline: float
    governance_process: float
    explainability: float
    communication_clarity: float

WEIGHTS=[0.10,0.09,0.10,0.09,0.08,0.08,0.08,0.10,0.09,0.08,0.06,0.05]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def knowledge_graph_score(case: KnowledgeGraphCase) -> float:
    vals=[case.graph_schema_clarity,case.entity_resolution,case.relationship_quality,case.ontology_discipline,case.semantic_indexing,case.path_retrieval,case.hybrid_retrieval,case.provenance_support,case.evaluation_discipline,case.governance_process,case.explainability,case.communication_clarity]
    return clamp(100*sum(v*w for v,w in zip(vals, WEIGHTS)))

def semantic_retrieval_risk(case: KnowledgeGraphCase) -> float:
    vals=[case.graph_schema_clarity,case.entity_resolution,case.relationship_quality,case.ontology_discipline,case.provenance_support,case.evaluation_discipline,case.governance_process,case.explainability,case.communication_clarity]
    return clamp(100*mean(1-v for v in vals))

def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong knowledge graph retrieval discipline"
    if score >= 70 and risk <= 35:
        return "usable semantic retrieval with review needs"
    if risk >= 55:
        return "high risk; graph retrieval may hide weak identity, unsupported edges, ontology drift, or poor provenance"
    return "partial discipline; strengthen schema, identity, relationships, ontology, provenance, evaluation, and explanation"

def load_cases(path: Path) -> list[KnowledgeGraphCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [
            KnowledgeGraphCase(
                r["case_name"], r["system_context"], r["retrieval_goal"],
                float(r["graph_schema_clarity"]), float(r["entity_resolution"]),
                float(r["relationship_quality"]), float(r["ontology_discipline"]),
                float(r["semantic_indexing"]), float(r["path_retrieval"]),
                float(r["hybrid_retrieval"]), float(r["provenance_support"]),
                float(r["evaluation_discipline"]), float(r["governance_process"]),
                float(r["explainability"]), float(r["communication_clarity"])
            ) for r in rows
        ]

def load_edges(path: Path) -> list[tuple[str,str,str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return [(r["subject"], r["predicate"], r["object"]) for r in csv.DictReader(f)]

def build_adjacency(edges: list[tuple[str,str,str]]) -> dict[str, list[tuple[str,str]]]:
    graph: dict[str, list[tuple[str,str]]] = defaultdict(list)
    for s,p,o in edges:
        graph[s].append((p,o))
    return dict(graph)

def shortest_path(edges: list[tuple[str,str,str]], start: str, goal: str) -> list[str]:
    graph=build_adjacency(edges)
    queue: deque[tuple[str,list[str]]] = deque([(start,[start])])
    visited={start}
    while queue:
        node,path=queue.popleft()
        if node == goal:
            return path
        for _,neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor,path+[neighbor]))
    return []

def neighborhood(edges: list[tuple[str,str,str]], node: str, radius: int = 1) -> list[dict[str,str]]:
    graph=build_adjacency(edges)
    rows=[]
    queue: deque[tuple[str,int]] = deque([(node,0)])
    visited={node}
    while queue:
        current, depth=queue.popleft()
        if depth == radius:
            continue
        for predicate, neighbor in graph.get(current, []):
            rows.append({"source":current,"relationship":predicate,"target":neighbor,"depth":str(depth+1)})
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, depth+1))
    return rows

def hybrid_score(lexical: float, vector: float, graph: float, provenance: float) -> dict[str, float]:
    score=100*(0.25*lexical+0.25*vector+0.25*graph+0.25*provenance)
    return {"lexical":lexical,"vector":vector,"graph":graph,"provenance":provenance,"hybrid_score":round(score,3)}

def graph_path_score(path_length: int, relationship_confidence: float, provenance_strength: float, review_status: float) -> dict[str, float | str]:
    length_factor=1/(1+max(path_length-1,0))
    score=100*(0.25*length_factor+0.30*relationship_confidence+0.30*provenance_strength+0.15*review_status)
    return {"path_length": path_length, "relationship_confidence": relationship_confidence, "provenance_strength": provenance_strength, "review_status": review_status, "graph_path_score": round(score,3), "diagnostic": "strong source-backed path" if score >= 84 else "review path length, confidence, provenance, and review status"}

def evaluate(cases: list[KnowledgeGraphCase]) -> list[dict[str,object]]:
    out=[]
    for c in cases:
        score=knowledge_graph_score(c)
        risk=semantic_retrieval_risk(c)
        out.append({**asdict(c), "knowledge_graph_score":round(score,3), "semantic_retrieval_risk":round(risk,3), "diagnostic":diagnose(score,risk)})
    return out

def graph_examples(edges: list[tuple[str,str,str]]) -> list[dict[str,str]]:
    path=shortest_path(edges, "Knowledge Graphs", "Traceability")
    return [
        {"example":"shortest_path_knowledge_graphs_to_traceability", "value":" -> ".join(path)},
        {"example":"semantic_retrieval_neighborhood_radius_2", "value":str(len(neighborhood(edges, "Semantic Retrieval", radius=2)))},
        {"example":"graph_path_score_example", "value":str(graph_path_score(3, .90, .92, .95)["graph_path_score"])},
    ]

def hybrid_examples() -> list[dict[str,float]]:
    return [hybrid_score(.82,.78,.88,.90), hybrid_score(.60,.86,.42,.30)]

def write_csv(path: Path, rows: list[dict[str,object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    cases=evaluate(load_cases(root/"data"/"synthetic_knowledge_graph_cases.csv"))
    edges=load_edges(root/"data"/"synthetic_graph_edges.csv")
    summary={
        "case_count": len(cases),
        "average_knowledge_graph_score": round(mean(float(r["knowledge_graph_score"]) for r in cases),3),
        "average_semantic_retrieval_risk": round(mean(float(r["semantic_retrieval_risk"]) for r in cases),3),
        "highest_score_case": max(cases, key=lambda r: float(r["knowledge_graph_score"]))["case_name"],
        "highest_risk_case": max(cases, key=lambda r: float(r["semantic_retrieval_risk"]))["case_name"]
    }
    write_csv(root/"outputs"/"tables"/"knowledge_graph_retrieval_audit.csv", cases)
    write_csv(root/"outputs"/"tables"/"knowledge_graph_retrieval_audit_summary.csv", [summary])
    write_csv(root/"outputs"/"tables"/"graph_edges.csv", [{"subject":s,"predicate":p,"object":o} for s,p,o in edges])
    write_csv(root/"outputs"/"tables"/"graph_examples.csv", graph_examples(edges))
    write_csv(root/"outputs"/"tables"/"hybrid_retrieval_examples.csv", hybrid_examples())
    write_json(root/"outputs"/"json"/"knowledge_graph_retrieval_audit.json", cases)
    write_json(root/"outputs"/"json"/"knowledge_graph_retrieval_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"graph_adjacency.json", build_adjacency(edges))
    write_json(root/"outputs"/"json"/"graph_examples.json", graph_examples(edges))
    write_json(root/"outputs"/"json"/"hybrid_retrieval_examples.json", hybrid_examples())

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
