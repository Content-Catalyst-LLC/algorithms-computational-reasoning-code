from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class RepresentationCase:
    case_name: str
    representation_context: str
    representation_choice: str
    structural_fidelity: float
    operation_fit: float
    validation_discipline: float
    information_loss_control: float
    traceability: float
    interpretability: float
    retrieval_support: float
    transformation_readiness: float
    risk_documentation: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def representation_quality(case: RepresentationCase) -> float:
    return clamp(100.0 * (
        0.12 * case.structural_fidelity
        + 0.12 * case.operation_fit
        + 0.10 * case.validation_discipline
        + 0.10 * case.information_loss_control
        + 0.10 * case.traceability
        + 0.10 * case.interpretability
        + 0.08 * case.retrieval_support
        + 0.08 * case.transformation_readiness
        + 0.10 * case.risk_documentation
        + 0.10 * case.governance_readiness
    ))


def representation_risk(case: RepresentationCase) -> float:
    weak_points = [
        1.0 - case.structural_fidelity,
        1.0 - case.operation_fit,
        1.0 - case.validation_discipline,
        1.0 - case.information_loss_control,
        1.0 - case.traceability,
        1.0 - case.interpretability,
        1.0 - case.risk_documentation,
        1.0 - case.governance_readiness,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 82 and risk <= 22:
        return "strong representation posture with clear structure, operation fit, traceability, and governance"
    if quality >= 68 and risk <= 38:
        return "usable representation posture with review needs"
    if risk >= 55:
        return "high representation risk; structure, fit, loss, or traceability may be unclear"
    return "partial representation posture; strengthen validation, interpretability, risk documentation, or governance"


def load_cases(path: Path) -> list[RepresentationCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            RepresentationCase(
                row["case_name"],
                row["representation_context"],
                row["representation_choice"],
                float(row["structural_fidelity"]),
                float(row["operation_fit"]),
                float(row["validation_discipline"]),
                float(row["information_loss_control"]),
                float(row["traceability"]),
                float(row["interpretability"]),
                float(row["retrieval_support"]),
                float(row["transformation_readiness"]),
                float(row["risk_documentation"]),
                float(row["governance_readiness"]),
            )
            for row in reader
        ]


def evaluate_cases(cases: list[RepresentationCase]) -> list[dict[str, object]]:
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
        "interpretation": "Representation quality depends on structural fidelity, operation fit, validation, information-loss control, traceability, interpretability, retrieval support, transformation readiness, risk documentation, and governance.",
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
    rows = evaluate_cases(load_cases(article_root / "data" / "synthetic_representation_cases.csv"))
    summary = summarize(rows)
    write_csv(article_root / "outputs" / "tables" / "representation_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "representation_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "representation_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "representation_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
