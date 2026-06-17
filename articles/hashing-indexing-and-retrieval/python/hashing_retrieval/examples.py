from __future__ import annotations

import csv
import hashlib
from pathlib import Path
from collections import defaultdict


class TinyHashTable:
    def __init__(self, bucket_count: int = 8) -> None:
        if bucket_count <= 0:
            raise ValueError("bucket_count must be positive")
        self.bucket_count = bucket_count
        self.buckets: list[list[tuple[str, str]]] = [[] for _ in range(bucket_count)]

    def _bucket(self, key: str) -> int:
        return sum(ord(ch) for ch in key) % self.bucket_count

    def put(self, key: str, value: str) -> None:
        bucket = self.buckets[self._bucket(key)]
        for idx, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[idx] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: str) -> str | None:
        for existing_key, value in self.buckets[self._bucket(key)]:
            if existing_key == key:
                return value
        return None

    def collision_bucket_lengths(self) -> list[int]:
        return [len(bucket) for bucket in self.buckets]


def stable_fingerprint(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def tokenize(text: str) -> set[str]:
    return {
        token.strip(".,;:!?()[]{}").lower()
        for token in text.split()
        if token.strip(".,;:!?()[]{}")
    }


def build_inverted_index(documents: dict[str, str]) -> dict[str, list[str]]:
    index: dict[str, set[str]] = defaultdict(set)
    for doc_id, text in documents.items():
        for term in tokenize(text):
            index[term].add(doc_id)
    return {term: sorted(doc_ids) for term, doc_ids in sorted(index.items())}


def retrieve(index: dict[str, list[str]], query: str) -> list[str]:
    terms = list(tokenize(query))
    if not terms:
        return []
    result_sets = [set(index.get(term, [])) for term in terms]
    return sorted(set.intersection(*result_sets)) if result_sets else []


def load_documents(path: Path) -> dict[str, str]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return {row["doc_id"]: row["body"] for row in reader}


def demo_retrieval(article_root: Path | None = None) -> dict[str, object]:
    documents = {
        "doc-1": "Hashing supports fast lookup by key.",
        "doc-2": "Indexing supports retrieval across documents and metadata.",
        "doc-3": "Retrieval quality depends on freshness provenance and ranking.",
        "doc-4": "Hashing and indexing support scalable retrieval.",
    }
    if article_root is not None:
        csv_path = article_root / "data" / "synthetic_documents.csv"
        if csv_path.exists():
            documents = load_documents(csv_path)

    table = TinyHashTable(bucket_count=4)
    for doc_id, text in documents.items():
        table.put(doc_id, stable_fingerprint(text)[:16])

    index = build_inverted_index(documents)
    return {
        "fingerprint_doc_1": stable_fingerprint(documents["doc-1"]),
        "hash_table_bucket_lengths": table.collision_bucket_lengths(),
        "hash_table_lookup_doc_1": table.get("doc-1"),
        "inverted_index": index,
        "query_hashing_lookup": retrieve(index, "hashing lookup"),
        "query_indexing_retrieval": retrieve(index, "indexing retrieval"),
        "interpretation": "Hashing creates stable fingerprints and key lookup; an inverted index maps terms to retrievable documents.",
    }
