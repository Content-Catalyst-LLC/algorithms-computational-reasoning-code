from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class TraceabilityCase:
    case_name: str
    problem_context: str
    traceability_structure_choice: str
    metadata_completeness: float
    source_clarity: float
    lineage_coverage: float
    version_control: float
    timestamp_quality: float
    schema_clarity: float
    integrity_checks: float
    access_governance: float
    reproducibility_support: float
    stewardship_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def traceability_quality(case: TraceabilityCase) -> float:
    return clamp(100.0 * (
        0.12 * case.metadata_completeness
        + 0.10 * case.source_clarity
        + 0.12 * case.lineage_coverage
        + 0.10 * case.version_control
        + 0.08 * case.timestamp_quality
        + 0.10 * case.schema_clarity
        + 0.10 * case.integrity_checks
        + 0.10 * case.access_governance
        + 0.10 * case.reproducibility_support
        + 0.08 * case.stewardship_readiness
    ))


def traceability_risk(case: TraceabilityCase) -> float:
    weak_points = [
        1.0 - case.metadata_completeness,
        1.0 - case.source_clarity,
        1.0 - case.lineage_coverage,
        1.0 - case.version_control,
        1.0 - case.schema_clarity,
        1.0 - case.integrity_checks,
        1.0 - case.access_governance,
        1.0 - case.reproducibility_support,
        1.0 - case.stewardship_readiness,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 84 and risk <= 20:
        return "strong traceability posture with metadata, provenance, lineage, integrity checks, reproducibility, and stewardship"
    if quality >= 70 and risk <= 35:
        return "usable traceability posture with review needs"
    if risk >= 55:
        return "high traceability risk; source, lineage, versioning, integrity, or governance may be weak"
    return "partial traceability posture; strengthen metadata quality, provenance links, versioning, or stewardship"


def load_cases(path: Path) -> list[TraceabilityCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            TraceabilityCase(
                row["case_name"],
                row["problem_context"],
                row["traceability_structure_choice"],
                float(row["metadata_completeness"]),
                float(row["source_clarity"]),
                float(row["lineage_coverage"]),
                float(row["version_control"]),
                float(row["timestamp_quality"]),
                float(row["schema_clarity"]),
                float(row["integrity_checks"]),
                float(row["access_governance"]),
                float(row["reproducibility_support"]),
                float(row["stewardship_readiness"]),
            )
            for row in reader
        ]


def evaluate_cases(cases: list[TraceabilityCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        quality = traceability_quality(case)
        risk = traceability_risk(case)
        rows.append({
            **asdict(case),
            "traceability_quality": round(quality, 3),
            "traceability_risk": round(risk, 3),
            "diagnostic": diagnose(quality, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_traceability_quality": round(mean(float(row["traceability_quality"]) for row in rows), 3),
        "average_traceability_risk": round(mean(float(row["traceability_risk"]) for row in rows), 3),
        "highest_quality_case": max(rows, key=lambda row: float(row["traceability_quality"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["traceability_risk"]))["case_name"],
        "interpretation": "Traceability quality depends on metadata completeness, source clarity, lineage coverage, version control, timestamps, schema clarity, integrity checks, access governance, reproducibility, and stewardship.",
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
    rows = evaluate_cases(load_cases(article_root / "data" / "synthetic_metadata_provenance_cases.csv"))
    summary = summarize(rows)
    write_csv(article_root / "outputs" / "tables" / "metadata_provenance_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "metadata_provenance_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "metadata_provenance_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "metadata_provenance_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
