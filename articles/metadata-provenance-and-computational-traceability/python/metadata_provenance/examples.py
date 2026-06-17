from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


def checksum(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_edges(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def provenance_demo(article_root: Path | None = None) -> dict[str, object]:
    nodes = [
        {"id": "raw-data-v1", "type": "entity", "label": "Raw data version 1"},
        {"id": "cleaning-script-a", "type": "activity", "label": "Cleaning script A"},
        {"id": "analysis-table-v1", "type": "entity", "label": "Analysis table version 1"},
        {"id": "model-run-42", "type": "activity", "label": "Model run 42"},
        {"id": "published-chart-v1", "type": "entity", "label": "Published chart version 1"},
    ]

    edges = [
        {"from_id": "cleaning-script-a", "to_id": "raw-data-v1", "relation": "used", "actor": "pipeline", "timestamp": "2026-06-17T12:00:00Z"},
        {"from_id": "analysis-table-v1", "to_id": "cleaning-script-a", "relation": "was_generated_by", "actor": "pipeline", "timestamp": "2026-06-17T12:10:00Z"},
        {"from_id": "model-run-42", "to_id": "analysis-table-v1", "relation": "used", "actor": "model-runner", "timestamp": "2026-06-17T12:20:00Z"},
        {"from_id": "published-chart-v1", "to_id": "model-run-42", "relation": "was_generated_by", "actor": "publisher", "timestamp": "2026-06-17T12:30:00Z"},
        {"from_id": "published-chart-v1", "to_id": "raw-data-v1", "relation": "was_derived_from", "actor": "publisher", "timestamp": "2026-06-17T12:30:00Z"},
    ]

    if article_root is not None:
        edge_path = article_root / "data" / "synthetic_provenance_edges.csv"
        if edge_path.exists():
            edges = load_edges(edge_path)

    trace_text = json.dumps({"nodes": nodes, "edges": edges}, sort_keys=True)

    return {
        "nodes": nodes,
        "edges": edges,
        "trace_checksum": checksum(trace_text),
        "interpretation": "A provenance graph links entities and activities so outputs can be traced back to inputs, processes, and evidence.",
    }


def find_upstream(target_id: str, edges: list[dict[str, str]]) -> list[str]:
    upstream: list[str] = []
    for edge in edges:
        if edge["from_id"] == target_id and edge["to_id"] not in upstream:
            upstream.append(edge["to_id"])
    return upstream
