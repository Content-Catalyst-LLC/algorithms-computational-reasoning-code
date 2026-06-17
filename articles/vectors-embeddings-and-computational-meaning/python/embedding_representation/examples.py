from __future__ import annotations

import csv
import math
from pathlib import Path


def dot(x: list[float], y: list[float]) -> float:
    return sum(a * b for a, b in zip(x, y))


def norm(x: list[float]) -> float:
    return math.sqrt(sum(a * a for a in x))


def cosine_similarity(x: list[float], y: list[float]) -> float:
    denominator = norm(x) * norm(y)
    if denominator == 0:
        return 0.0
    return dot(x, y) / denominator


def euclidean_distance(x: list[float], y: list[float]) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(x, y)))


def load_vectors(path: Path) -> dict[str, list[float]]:
    vectors: dict[str, list[float]] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            vectors[row["item_id"]] = [
                float(row["dimension_1"]),
                float(row["dimension_2"]),
                float(row["dimension_3"]),
                float(row["dimension_4"]),
            ]
    return vectors


def nearest_neighbors(query: list[float], vectors: dict[str, list[float]]) -> list[dict[str, object]]:
    rows = []
    for item_id, vector in vectors.items():
        rows.append({
            "item_id": item_id,
            "cosine_similarity": round(cosine_similarity(query, vector), 4),
            "euclidean_distance": round(euclidean_distance(query, vector), 4),
        })
    return sorted(rows, key=lambda row: row["cosine_similarity"], reverse=True)


def demo_embedding_space(article_root: Path | None = None) -> dict[str, object]:
    vectors = {
        "article-search": [0.92, 0.12, 0.18, 0.08],
        "document-index": [0.84, 0.20, 0.24, 0.10],
        "image-retrieval": [0.20, 0.86, 0.22, 0.18],
        "policy-review": [0.36, 0.18, 0.82, 0.34],
    }
    if article_root is not None:
        vector_path = article_root / "data" / "synthetic_vectors.csv"
        if vector_path.exists():
            vectors = load_vectors(vector_path)

    query = [0.88, 0.16, 0.20, 0.12]
    return {
        "query_vector": query,
        "nearest_neighbors": nearest_neighbors(query, vectors),
        "interpretation": "Nearest-neighbor search ranks vectors by similarity, but the similarity score is a computational signal rather than final semantic truth.",
    }
