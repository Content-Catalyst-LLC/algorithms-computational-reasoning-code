from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class EmbeddingSystemCase:
    case_name: str
    problem_context: str
    embedding_structure_choice: str
    representation_fit: float
    model_documentation: float
    vector_compatibility: float
    similarity_interpretability: float
    retrieval_evidence: float
    metadata_provenance: float
    bias_review: float
    drift_monitoring: float
    access_boundary_clarity: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def embedding_quality(case: EmbeddingSystemCase) -> float:
    return clamp(100.0 * (
        0.12 * case.representation_fit
        + 0.10 * case.model_documentation
        + 0.10 * case.vector_compatibility
        + 0.10 * case.similarity_interpretability
        + 0.10 * case.retrieval_evidence
        + 0.10 * case.metadata_provenance
        + 0.10 * case.bias_review
        + 0.08 * case.drift_monitoring
        + 0.10 * case.access_boundary_clarity
        + 0.10 * case.governance_readiness
    ))


def meaning_overclaim_risk(case: EmbeddingSystemCase) -> float:
    weak_points = [
        1.0 - case.representation_fit,
        1.0 - case.model_documentation,
        1.0 - case.similarity_interpretability,
        1.0 - case.retrieval_evidence,
        1.0 - case.metadata_provenance,
        1.0 - case.bias_review,
        1.0 - case.drift_monitoring,
        1.0 - case.governance_readiness,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 82 and risk <= 22:
        return "strong embedding posture with traceable model, interpretable similarity, evidence, bias review, and governance"
    if quality >= 68 and risk <= 38:
        return "usable embedding posture with review needs"
    if risk >= 55:
        return "high meaning-overclaim risk; similarity may be interpreted beyond available evidence"
    return "partial embedding posture; strengthen model documentation, provenance, retrieval evidence, or governance"


def load_cases(path: Path) -> list[EmbeddingSystemCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            EmbeddingSystemCase(
                row["case_name"],
                row["problem_context"],
                row["embedding_structure_choice"],
                float(row["representation_fit"]),
                float(row["model_documentation"]),
                float(row["vector_compatibility"]),
                float(row["similarity_interpretability"]),
                float(row["retrieval_evidence"]),
                float(row["metadata_provenance"]),
                float(row["bias_review"]),
                float(row["drift_monitoring"]),
                float(row["access_boundary_clarity"]),
                float(row["governance_readiness"]),
            )
            for row in reader
        ]


def evaluate_cases(cases: list[EmbeddingSystemCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        quality = embedding_quality(case)
        risk = meaning_overclaim_risk(case)
        rows.append({
            **asdict(case),
            "embedding_quality": round(quality, 3),
            "meaning_overclaim_risk": round(risk, 3),
            "diagnostic": diagnose(quality, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_embedding_quality": round(mean(float(row["embedding_quality"]) for row in rows), 3),
        "average_meaning_overclaim_risk": round(mean(float(row["meaning_overclaim_risk"]) for row in rows), 3),
        "highest_quality_case": max(rows, key=lambda row: float(row["embedding_quality"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["meaning_overclaim_risk"]))["case_name"],
        "interpretation": "Embedding quality depends on representation fit, model documentation, compatibility, similarity interpretation, retrieval evidence, provenance, bias review, drift monitoring, access boundaries, and governance.",
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
    rows = evaluate_cases(load_cases(article_root / "data" / "synthetic_embedding_system_cases.csv"))
    summary = summarize(rows)
    write_csv(article_root / "outputs" / "tables" / "embedding_representation_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "embedding_representation_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "embedding_representation_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "embedding_representation_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
