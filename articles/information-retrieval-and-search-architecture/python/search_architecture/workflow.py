from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
from collections import Counter, defaultdict
from statistics import mean
import csv, json, math

@dataclass(frozen=True)
class SearchArchitectureCase:
    case_name: str
    system_context: str
    retrieval_goal: str
    collection_coverage: float
    metadata_quality: float
    indexing_completeness: float
    query_interpretation: float
    ranking_clarity: float
    filter_quality: float
    freshness_management: float
    evaluation_discipline: float
    feedback_governance: float
    provenance_support: float
    accessibility_support: float
    communication_clarity: float

WEIGHTS=[0.10,0.10,0.10,0.09,0.09,0.08,0.08,0.09,0.07,0.08,0.06,0.06]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def search_architecture_score(case: SearchArchitectureCase) -> float:
    vals=[case.collection_coverage,case.metadata_quality,case.indexing_completeness,case.query_interpretation,case.ranking_clarity,case.filter_quality,case.freshness_management,case.evaluation_discipline,case.feedback_governance,case.provenance_support,case.accessibility_support,case.communication_clarity]
    return clamp(100*sum(v*w for v,w in zip(vals, WEIGHTS)))

def retrieval_risk(case: SearchArchitectureCase) -> float:
    vals=[case.collection_coverage,case.metadata_quality,case.indexing_completeness,case.ranking_clarity,case.freshness_management,case.evaluation_discipline,case.feedback_governance,case.provenance_support,case.communication_clarity]
    return clamp(100*mean(1-v for v in vals))

def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong information retrieval architecture"
    if score >= 70 and risk <= 35:
        return "usable search architecture with review needs"
    if risk >= 55:
        return "high risk; search may hide weak coverage, metadata, ranking, freshness, evaluation, or provenance"
    return "partial discipline; strengthen collection coverage, metadata, indexing, evaluation, provenance, and communication"

def load_cases(path: Path) -> list[SearchArchitectureCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [
            SearchArchitectureCase(
                r["case_name"], r["system_context"], r["retrieval_goal"],
                float(r["collection_coverage"]), float(r["metadata_quality"]),
                float(r["indexing_completeness"]), float(r["query_interpretation"]),
                float(r["ranking_clarity"]), float(r["filter_quality"]),
                float(r["freshness_management"]), float(r["evaluation_discipline"]),
                float(r["feedback_governance"]), float(r["provenance_support"]),
                float(r["accessibility_support"]), float(r["communication_clarity"])
            ) for r in rows
        ]

def tokenize(text: str) -> list[str]:
    cleaned="".join(ch.lower() if ch.isalnum() else " " for ch in text)
    return [token for token in cleaned.split() if token]

def build_inverted_index(documents: dict[str, str]) -> dict[str, list[str]]:
    index: dict[str, set[str]] = defaultdict(set)
    for doc_id, text in documents.items():
        for token in set(tokenize(text)):
            index[token].add(doc_id)
    return {term: sorted(ids) for term, ids in sorted(index.items())}

def tfidf_scores(query: str, documents: dict[str, str]) -> list[dict[str, object]]:
    query_terms=tokenize(query)
    doc_tokens={doc_id: tokenize(text) for doc_id, text in documents.items()}
    total_docs=len(documents)
    df=Counter()
    for tokens in doc_tokens.values():
        for token in set(tokens):
            df[token]+=1
    rows=[]
    for doc_id, tokens in doc_tokens.items():
        counts=Counter(tokens)
        score=0.0
        for term in query_terms:
            if df[term] == 0:
                continue
            tf=counts[term]
            idf=math.log((1+total_docs)/(1+df[term]))+1
            score += tf*idf
        rows.append({"doc_id": doc_id, "score": round(score, 4)})
    return sorted(rows, key=lambda row: row["score"], reverse=True)

def precision_recall(relevant: set[str], retrieved: list[str]) -> dict[str, float]:
    retrieved_set=set(retrieved)
    tp=len(relevant & retrieved_set)
    return {"precision": round(tp/len(retrieved),4) if retrieved else 0.0, "recall": round(tp/len(relevant),4) if relevant else 0.0}

def search_architecture_calculator(collection: float, metadata: float, indexing: float, ranking: float, evaluation: float, provenance: float) -> dict[str, object]:
    score=100*(0.18*collection+0.18*metadata+0.18*indexing+0.16*ranking+0.15*evaluation+0.15*provenance)
    return {"search_architecture_core_score": round(score,3), "diagnostic": "strong search architecture core" if score >= 84 else "review collection coverage, metadata, indexing, ranking, evaluation, and provenance"}

def sample_documents() -> dict[str, str]:
    return {
        "doc_1":"Information retrieval uses indexing ranking and evaluation to support search.",
        "doc_2":"Database optimization uses query plans indexes joins and cardinality estimates.",
        "doc_3":"Metadata provenance and traceability improve knowledge system governance.",
        "doc_4":"Search architecture combines documents metadata inverted indexes ranking filters and logs.",
        "doc_5":"Vector embeddings support semantic similarity search and retrieval augmented systems.",
    }

def evaluate(cases: list[SearchArchitectureCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        score=search_architecture_score(c)
        risk=retrieval_risk(c)
        out.append({**asdict(c), "search_architecture_score": round(score,3), "retrieval_risk": round(risk,3), "diagnostic": diagnose(score,risk)})
    return out

def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    rows=evaluate(load_cases(root/"data"/"synthetic_search_architecture_cases.csv"))
    summary={
        "case_count": len(rows),
        "average_search_architecture_score": round(mean(float(r["search_architecture_score"]) for r in rows),3),
        "average_retrieval_risk": round(mean(float(r["retrieval_risk"]) for r in rows),3),
        "highest_score_case": max(rows, key=lambda r: float(r["search_architecture_score"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda r: float(r["retrieval_risk"]))["case_name"]
    }
    documents=sample_documents()
    index=build_inverted_index(documents)
    ranking=tfidf_scores("search indexing metadata", documents)
    metrics=precision_recall({"doc_1","doc_4"}, [row["doc_id"] for row in ranking[:3]])
    write_csv(root/"outputs"/"tables"/"search_architecture_audit.csv", rows)
    write_csv(root/"outputs"/"tables"/"search_architecture_audit_summary.csv", [summary])
    write_csv(root/"outputs"/"tables"/"tfidf_search_results.csv", ranking)
    write_csv(root/"outputs"/"tables"/"precision_recall_example.csv", [metrics])
    write_json(root/"outputs"/"json"/"search_architecture_audit.json", rows)
    write_json(root/"outputs"/"json"/"search_architecture_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"inverted_index_example.json", index)
    write_json(root/"outputs"/"json"/"tfidf_search_results.json", ranking)
    write_json(root/"outputs"/"json"/"precision_recall_example.json", metrics)
    write_json(root/"outputs"/"json"/"search_architecture_core_score.json", search_architecture_calculator(.88,.90,.84,.76,.74,.86))

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
