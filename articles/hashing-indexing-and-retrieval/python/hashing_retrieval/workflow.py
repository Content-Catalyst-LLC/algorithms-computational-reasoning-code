from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class RetrievalSystemCase:
    case_name: str
    problem_context: str
    retrieval_structure_choice: str
    key_clarity: float
    hash_suitability: float
    collision_handling: float
    index_coverage: float
    retrieval_speed_fit: float
    freshness_control: float
    ranking_transparency: float
    metadata_provenance: float
    security_boundary_clarity: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def retrieval_quality(case: RetrievalSystemCase) -> float:
    return clamp(100.0 * (
        0.12 * case.key_clarity
        + 0.08 * case.hash_suitability
        + 0.10 * case.collision_handling
        + 0.12 * case.index_coverage
        + 0.10 * case.retrieval_speed_fit
        + 0.10 * case.freshness_control
        + 0.10 * case.ranking_transparency
        + 0.10 * case.metadata_provenance
        + 0.08 * case.security_boundary_clarity
        + 0.10 * case.governance_readiness
    ))


def retrieval_risk(case: RetrievalSystemCase) -> float:
    weak_points = [
        1.0 - case.key_clarity,
        1.0 - case.collision_handling,
        1.0 - case.index_coverage,
        1.0 - case.freshness_control,
        1.0 - case.ranking_transparency,
        1.0 - case.metadata_provenance,
        1.0 - case.security_boundary_clarity,
        1.0 - case.governance_readiness,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 82 and risk <= 22:
        return "strong retrieval posture with clear keys, index coverage, freshness, provenance, and governance"
    if quality >= 68 and risk <= 38:
        return "usable retrieval posture with review needs"
    if risk >= 55:
        return "high retrieval risk; keys, index coverage, freshness, ranking, or provenance may be weak"
    return "partial retrieval posture; strengthen key design, collision handling, index coverage, or governance"


def load_cases(path: Path) -> list[RetrievalSystemCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            RetrievalSystemCase(
                row["case_name"],
                row["problem_context"],
                row["retrieval_structure_choice"],
                float(row["key_clarity"]),
                float(row["hash_suitability"]),
                float(row["collision_handling"]),
                float(row["index_coverage"]),
                float(row["retrieval_speed_fit"]),
                float(row["freshness_control"]),
                float(row["ranking_transparency"]),
                float(row["metadata_provenance"]),
                float(row["security_boundary_clarity"]),
                float(row["governance_readiness"]),
            )
            for row in reader
        ]


def evaluate_cases(cases: list[RetrievalSystemCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        quality = retrieval_quality(case)
        risk = retrieval_risk(case)
        rows.append({
            **asdict(case),
            "retrieval_quality": round(quality, 3),
            "retrieval_risk": round(risk, 3),
            "diagnostic": diagnose(quality, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_retrieval_quality": round(mean(float(row["retrieval_quality"]) for row in rows), 3),
        "average_retrieval_risk": round(mean(float(row["retrieval_risk"]) for row in rows), 3),
        "highest_quality_case": max(rows, key=lambda row: float(row["retrieval_quality"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["retrieval_risk"]))["case_name"],
        "interpretation": "Retrieval quality depends on key clarity, hash suitability, collision handling, index coverage, speed fit, freshness, ranking transparency, provenance, security boundaries, and governance.",
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
    rows = evaluate_cases(load_cases(article_root / "data" / "synthetic_hashing_retrieval_cases.csv"))
    summary = summarize(rows)
    write_csv(article_root / "outputs" / "tables" / "hashing_retrieval_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "hashing_retrieval_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "hashing_retrieval_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "hashing_retrieval_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
