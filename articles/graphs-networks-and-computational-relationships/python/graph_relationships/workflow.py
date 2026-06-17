from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class GraphRelationshipCase:
    case_name: str
    problem_context: str
    graph_choice: str
    edge_meaning_clarity: float
    node_definition_clarity: float
    direction_clarity: float
    weight_interpretability: float
    path_validity: float
    connectivity_evidence: float
    metadata_provenance: float
    algorithm_fit: float
    representation_risk_documentation: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def graph_reasoning_quality(case: GraphRelationshipCase) -> float:
    return clamp(100.0 * (
        0.12 * case.edge_meaning_clarity
        + 0.10 * case.node_definition_clarity
        + 0.10 * case.direction_clarity
        + 0.08 * case.weight_interpretability
        + 0.10 * case.path_validity
        + 0.10 * case.connectivity_evidence
        + 0.10 * case.metadata_provenance
        + 0.10 * case.algorithm_fit
        + 0.10 * case.representation_risk_documentation
        + 0.10 * case.governance_readiness
    ))


def relationship_overclaim_risk(case: GraphRelationshipCase) -> float:
    weak_points = [
        1.0 - case.edge_meaning_clarity,
        1.0 - case.node_definition_clarity,
        1.0 - case.direction_clarity,
        1.0 - case.weight_interpretability,
        1.0 - case.path_validity,
        1.0 - case.metadata_provenance,
        1.0 - case.representation_risk_documentation,
        1.0 - case.governance_readiness,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 82 and risk <= 22:
        return "strong graph-reasoning posture with clear edge meaning, paths, metadata, algorithm fit, and governance"
    if quality >= 68 and risk <= 38:
        return "usable graph-reasoning posture with review needs"
    if risk >= 55:
        return "high relationship-overclaim risk; edges or paths may imply more than evidence supports"
    return "partial graph-reasoning posture; strengthen edge definitions, provenance, path interpretation, or governance"


def load_cases(path: Path) -> list[GraphRelationshipCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            GraphRelationshipCase(
                row["case_name"],
                row["problem_context"],
                row["graph_choice"],
                float(row["edge_meaning_clarity"]),
                float(row["node_definition_clarity"]),
                float(row["direction_clarity"]),
                float(row["weight_interpretability"]),
                float(row["path_validity"]),
                float(row["connectivity_evidence"]),
                float(row["metadata_provenance"]),
                float(row["algorithm_fit"]),
                float(row["representation_risk_documentation"]),
                float(row["governance_readiness"]),
            )
            for row in reader
        ]


def evaluate_cases(cases: list[GraphRelationshipCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        quality = graph_reasoning_quality(case)
        risk = relationship_overclaim_risk(case)
        rows.append({
            **asdict(case),
            "graph_reasoning_quality": round(quality, 3),
            "relationship_overclaim_risk": round(risk, 3),
            "diagnostic": diagnose(quality, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_graph_reasoning_quality": round(mean(float(row["graph_reasoning_quality"]) for row in rows), 3),
        "average_relationship_overclaim_risk": round(mean(float(row["relationship_overclaim_risk"]) for row in rows), 3),
        "highest_quality_case": max(rows, key=lambda row: float(row["graph_reasoning_quality"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["relationship_overclaim_risk"]))["case_name"],
        "interpretation": "Graph quality depends on edge meaning, node definition, direction, weights, path validity, connectivity evidence, metadata, algorithm fit, risk documentation, and governance.",
    }


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def run_workflow(article_root: Path) -> None:
    rows = evaluate_cases(load_cases(article_root / "data" / "synthetic_graph_relationship_cases.csv"))
    summary = summarize(rows)
    write_csv(article_root / "outputs" / "tables" / "graph_relationship_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "graph_relationship_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "graph_relationship_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "graph_relationship_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
