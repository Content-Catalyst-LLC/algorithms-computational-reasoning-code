from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class DataStructureCase:
    case_name: str
    problem_context: str
    data_structure_choice: str
    operation_fit: float
    structural_fidelity: float
    invariant_clarity: float
    complexity_awareness: float
    memory_awareness: float
    interpretability: float
    retrieval_support: float
    transformation_support: float
    representation_risk_documentation: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def structure_reasoning_quality(case: DataStructureCase) -> float:
    return clamp(100.0 * (
        0.12 * case.operation_fit
        + 0.12 * case.structural_fidelity
        + 0.10 * case.invariant_clarity
        + 0.10 * case.complexity_awareness
        + 0.08 * case.memory_awareness
        + 0.10 * case.interpretability
        + 0.10 * case.retrieval_support
        + 0.08 * case.transformation_support
        + 0.10 * case.representation_risk_documentation
        + 0.10 * case.governance_readiness
    ))


def structure_mismatch_risk(case: DataStructureCase) -> float:
    weak_points = [
        1.0 - case.operation_fit,
        1.0 - case.structural_fidelity,
        1.0 - case.invariant_clarity,
        1.0 - case.complexity_awareness,
        1.0 - case.interpretability,
        1.0 - case.retrieval_support,
        1.0 - case.representation_risk_documentation,
        1.0 - case.governance_readiness,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 82 and risk <= 22:
        return "strong data-structure reasoning posture with clear operation fit, invariants, complexity, and governance"
    if quality >= 68 and risk <= 38:
        return "usable data-structure reasoning posture with review needs"
    if risk >= 55:
        return "high structure-mismatch risk; operation fit, invariants, or representation assumptions may be unclear"
    return "partial data-structure reasoning posture; strengthen structure choice, invariants, complexity, or governance"


def load_cases(path: Path) -> list[DataStructureCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            DataStructureCase(
                row["case_name"],
                row["problem_context"],
                row["data_structure_choice"],
                float(row["operation_fit"]),
                float(row["structural_fidelity"]),
                float(row["invariant_clarity"]),
                float(row["complexity_awareness"]),
                float(row["memory_awareness"]),
                float(row["interpretability"]),
                float(row["retrieval_support"]),
                float(row["transformation_support"]),
                float(row["representation_risk_documentation"]),
                float(row["governance_readiness"]),
            )
            for row in reader
        ]


def evaluate_cases(cases: list[DataStructureCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        quality = structure_reasoning_quality(case)
        risk = structure_mismatch_risk(case)
        rows.append({
            **asdict(case),
            "structure_reasoning_quality": round(quality, 3),
            "structure_mismatch_risk": round(risk, 3),
            "diagnostic": diagnose(quality, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_structure_reasoning_quality": round(mean(float(row["structure_reasoning_quality"]) for row in rows), 3),
        "average_structure_mismatch_risk": round(mean(float(row["structure_mismatch_risk"]) for row in rows), 3),
        "highest_quality_case": max(rows, key=lambda row: float(row["structure_reasoning_quality"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["structure_mismatch_risk"]))["case_name"],
        "interpretation": "Data-structure reasoning quality depends on operation fit, structural fidelity, invariants, complexity, memory, interpretability, retrieval, transformation support, representation-risk documentation, and governance.",
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
    rows = evaluate_cases(load_cases(article_root / "data" / "synthetic_data_structure_cases.csv"))
    summary = summarize(rows)
    write_csv(article_root / "outputs" / "tables" / "data_structure_reasoning_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "data_structure_reasoning_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "data_structure_reasoning_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "data_structure_reasoning_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
