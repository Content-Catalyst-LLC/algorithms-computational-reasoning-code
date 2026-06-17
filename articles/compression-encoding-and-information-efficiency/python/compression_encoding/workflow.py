from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class CompressionEncodingCase:
    case_name: str
    problem_context: str
    representation_choice: str
    fidelity_requirement: float
    encoding_clarity: float
    compression_suitability: float
    metadata_preservation: float
    interoperability: float
    integrity_checks: float
    storage_efficiency: float
    transmission_efficiency: float
    accessibility_preservation: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def representation_quality(case: CompressionEncodingCase) -> float:
    return clamp(100.0 * (
        0.12 * case.fidelity_requirement
        + 0.10 * case.encoding_clarity
        + 0.10 * case.compression_suitability
        + 0.10 * case.metadata_preservation
        + 0.10 * case.interoperability
        + 0.10 * case.integrity_checks
        + 0.10 * case.storage_efficiency
        + 0.08 * case.transmission_efficiency
        + 0.10 * case.accessibility_preservation
        + 0.10 * case.governance_readiness
    ))


def representation_risk(case: CompressionEncodingCase) -> float:
    weak_points = [
        1.0 - case.fidelity_requirement,
        1.0 - case.encoding_clarity,
        1.0 - case.metadata_preservation,
        1.0 - case.interoperability,
        1.0 - case.integrity_checks,
        1.0 - case.accessibility_preservation,
        1.0 - case.governance_readiness,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 82 and risk <= 22:
        return "strong representation posture with fidelity, metadata, interoperability, integrity checks, and governance"
    if quality >= 68 and risk <= 38:
        return "usable representation posture with review needs"
    if risk >= 55:
        return "high representation risk; encoding, fidelity, metadata, or governance may be weak"
    return "partial representation posture; strengthen fidelity, metadata, interoperability, integrity checks, or governance"


def load_cases(path: Path) -> list[CompressionEncodingCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            CompressionEncodingCase(
                row["case_name"],
                row["problem_context"],
                row["representation_choice"],
                float(row["fidelity_requirement"]),
                float(row["encoding_clarity"]),
                float(row["compression_suitability"]),
                float(row["metadata_preservation"]),
                float(row["interoperability"]),
                float(row["integrity_checks"]),
                float(row["storage_efficiency"]),
                float(row["transmission_efficiency"]),
                float(row["accessibility_preservation"]),
                float(row["governance_readiness"]),
            )
            for row in reader
        ]


def evaluate_cases(cases: list[CompressionEncodingCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        quality = representation_quality(case)
        risk = representation_risk(case)
        rows.append({
            **asdict(case),
            "representation_quality": round(quality, 3),
            "representation_risk": round(risk, 3),
            "diagnostic": diagnose(quality, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_representation_quality": round(mean(float(row["representation_quality"]) for row in rows), 3),
        "average_representation_risk": round(mean(float(row["representation_risk"]) for row in rows), 3),
        "highest_quality_case": max(rows, key=lambda row: float(row["representation_quality"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["representation_risk"]))["case_name"],
        "interpretation": "Compression and encoding quality depends on fidelity, encoding clarity, compression suitability, metadata, interoperability, integrity checks, efficiency, accessibility, and governance.",
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
    rows = evaluate_cases(load_cases(article_root / "data" / "synthetic_compression_encoding_cases.csv"))
    summary = summarize(rows)
    write_csv(article_root / "outputs" / "tables" / "compression_encoding_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "compression_encoding_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "compression_encoding_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "compression_encoding_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
