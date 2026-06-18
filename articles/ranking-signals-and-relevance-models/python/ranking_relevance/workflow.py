from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
from collections import Counter
from statistics import mean
import csv, json, math

@dataclass(frozen=True)
class RankingSignalCase:
    case_name: str
    system_context: str
    ranking_goal: str
    lexical_evidence: float
    field_weighting: float
    metadata_quality: float
    freshness_logic: float
    authority_evidence: float
    semantic_similarity: float
    evaluation_discipline: float
    diversity_handling: float
    feedback_governance: float
    provenance_support: float
    explainability: float
    communication_clarity: float

WEIGHTS=[0.10,0.09,0.09,0.08,0.08,0.09,0.10,0.08,0.07,0.08,0.08,0.06]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def ranking_quality_score(case: RankingSignalCase) -> float:
    vals=[case.lexical_evidence,case.field_weighting,case.metadata_quality,case.freshness_logic,case.authority_evidence,case.semantic_similarity,case.evaluation_discipline,case.diversity_handling,case.feedback_governance,case.provenance_support,case.explainability,case.communication_clarity]
    return clamp(100*sum(v*w for v,w in zip(vals, WEIGHTS)))

def ranking_risk(case: RankingSignalCase) -> float:
    vals=[case.lexical_evidence,case.metadata_quality,case.freshness_logic,case.authority_evidence,case.evaluation_discipline,case.feedback_governance,case.provenance_support,case.explainability,case.communication_clarity]
    return clamp(100*mean(1-v for v in vals))

def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong ranking and relevance-model discipline"
    if score >= 70 and risk <= 35:
        return "usable ranking model with review needs"
    if risk >= 55:
        return "high risk; ranking may hide weak metadata, stale results, popularity bias, or poor explainability"
    return "partial discipline; strengthen evidence, metadata, evaluation, provenance, diversity, and explanation"

def load_cases(path: Path) -> list[RankingSignalCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [
            RankingSignalCase(
                r["case_name"], r["system_context"], r["ranking_goal"],
                float(r["lexical_evidence"]), float(r["field_weighting"]),
                float(r["metadata_quality"]), float(r["freshness_logic"]),
                float(r["authority_evidence"]), float(r["semantic_similarity"]),
                float(r["evaluation_discipline"]), float(r["diversity_handling"]),
                float(r["feedback_governance"]), float(r["provenance_support"]),
                float(r["explainability"]), float(r["communication_clarity"])
            ) for r in rows
        ]

def tokenize(text: str) -> list[str]:
    cleaned="".join(ch.lower() if ch.isalnum() else " " for ch in text)
    return [token for token in cleaned.split() if token]

def tfidf_score(query: str, document: str, corpus: list[str]) -> float:
    query_terms=tokenize(query)
    document_terms=tokenize(document)
    counts=Counter(document_terms)
    corpus_tokens=[set(tokenize(doc)) for doc in corpus]
    n=len(corpus)
    score=0.0
    for term in query_terms:
        df=sum(1 for tokens in corpus_tokens if term in tokens)
        if df == 0:
            continue
        idf=math.log(n/df)
        score += counts[term]*idf
    return round(score,4)

def bm25_score(query: str, document: str, corpus: list[str], k1: float = 1.5, b: float = 0.75) -> float:
    query_terms=tokenize(query)
    doc_terms=tokenize(document)
    doc_len=len(doc_terms) or 1
    avgdl=mean(len(tokenize(doc)) for doc in corpus) or 1
    counts=Counter(doc_terms)
    corpus_sets=[set(tokenize(doc)) for doc in corpus]
    n=len(corpus)
    score=0.0
    for term in query_terms:
        df=sum(1 for tokens in corpus_sets if term in tokens)
        if df == 0:
            continue
        idf=math.log(1 + (n - df + 0.5)/(df + 0.5))
        tf=counts[term]
        denom=tf + k1*(1 - b + b*(doc_len/avgdl))
        score += idf * ((tf*(k1+1))/denom) if denom else 0.0
    return round(score,4)

def weighted_signal_score(signals: dict[str, float], weights: dict[str, float]) -> float:
    return round(100.0 * sum(signals[k] * weights.get(k, 0.0) for k in signals), 3)

def freshness_boost(days_since_update: int, decay: float = 0.015) -> float:
    return round(math.exp(-decay * days_since_update), 4)

def precision_at_k(relevant: set[str], ranked: list[str], k: int) -> float:
    top_k=ranked[:k]
    return round(len(set(top_k) & relevant)/len(top_k),4) if top_k else 0.0

def ranking_signal_calculator(lexical: float, metadata: float, freshness: float, authority: float, semantic: float, provenance: float) -> dict[str, object]:
    weights={"lexical":0.22,"metadata":0.18,"freshness":0.12,"authority":0.16,"semantic":0.17,"provenance":0.15}
    signals={"lexical":lexical,"metadata":metadata,"freshness":freshness,"authority":authority,"semantic":semantic,"provenance":provenance}
    score=weighted_signal_score(signals, weights)
    return {"ranking_signal_score": score, "diagnostic": "strong ranking signal balance" if score >= 84 else "review lexical, metadata, freshness, authority, semantic, and provenance balance"}

def sample_corpus() -> dict[str, str]:
    return {
        "doc_1":"Ranking signals combine lexical evidence metadata freshness authority and feedback.",
        "doc_2":"Information retrieval systems use indexes query processing and evaluation.",
        "doc_3":"Semantic embeddings support similarity search and retrieval augmented AI systems.",
        "doc_4":"Search governance reviews ranking explanations provenance and source quality.",
        "doc_5":"Database optimization uses query plans indexes joins and cardinality estimates.",
    }

def evaluate(cases: list[RankingSignalCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        score=ranking_quality_score(c)
        risk=ranking_risk(c)
        out.append({**asdict(c), "ranking_quality_score": round(score,3), "ranking_risk": round(risk,3), "diagnostic": diagnose(score,risk)})
    return out

def ranking_examples() -> list[dict[str, object]]:
    corpus=sample_corpus()
    docs=list(corpus.values())
    query="ranking metadata search governance"
    rows=[]
    for doc_id, text in corpus.items():
        rows.append({
            "doc_id": doc_id,
            "tfidf_score": tfidf_score(query, text, docs),
            "bm25_score": bm25_score(query, text, docs)
        })
    rows=sorted(rows, key=lambda row: row["bm25_score"], reverse=True)
    ranked_ids=[row["doc_id"] for row in rows]
    p_at_3=precision_at_k({"doc_1","doc_4"}, ranked_ids, 3)
    for row in rows:
        row["precision_at_3_for_example"] = p_at_3
    return rows

def signal_score_examples() -> list[dict[str, object]]:
    return [
        {"example":"balanced_signal_score", **ranking_signal_calculator(.84,.88,.76,.82,.78,.86)},
        {"example":"freshness_7_days", "score": freshness_boost(7)},
        {"example":"freshness_90_days", "score": freshness_boost(90)},
    ]

def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    rows=evaluate(load_cases(root/"data"/"synthetic_ranking_signal_cases.csv"))
    summary={
        "case_count": len(rows),
        "average_ranking_quality_score": round(mean(float(r["ranking_quality_score"]) for r in rows),3),
        "average_ranking_risk": round(mean(float(r["ranking_risk"]) for r in rows),3),
        "highest_score_case": max(rows, key=lambda r: float(r["ranking_quality_score"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda r: float(r["ranking_risk"]))["case_name"]
    }
    write_csv(root/"outputs"/"tables"/"ranking_signal_audit.csv", rows)
    write_csv(root/"outputs"/"tables"/"ranking_signal_audit_summary.csv", [summary])
    write_csv(root/"outputs"/"tables"/"ranking_examples.csv", ranking_examples())
    write_csv(root/"outputs"/"tables"/"signal_score_examples.csv", signal_score_examples())
    write_json(root/"outputs"/"json"/"ranking_signal_audit.json", rows)
    write_json(root/"outputs"/"json"/"ranking_signal_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"ranking_examples.json", ranking_examples())
    write_json(root/"outputs"/"json"/"signal_score_examples.json", signal_score_examples())

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
