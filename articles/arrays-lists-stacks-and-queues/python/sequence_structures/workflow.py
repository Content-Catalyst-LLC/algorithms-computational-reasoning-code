from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class SequenceStructureCase:
    case_name: str
    problem_context: str
    structure_choice: str
    operation_fit: float
    order_semantics: float
    invariant_clarity: float
    complexity_awareness: float
    memory_behavior: float
    overflow_handling: float
    interpretability: float
    traversal_support: float
    representation_risk_documentation: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def sequence_structure_quality(case: SequenceStructureCase) -> float:
    return clamp(100.0 * (
        0.12 * case.operation_fit
        + 0.12 * case.order_semantics
        + 0.10 * case.invariant_clarity
        + 0.10 * case.complexity_awareness
        + 0.08 * case.memory_behavior
        + 0.08 * case.overflow_handling
        + 0.10 * case.interpretability
        + 0.10 * case.traversal_support
        + 0.10 * case.representation_risk_documentation
        + 0.10 * case.governance_readiness
    ))


def sequence_structure_risk(case: SequenceStructureCase) -> float:
    weak_points = [
        1.0 - case.operation_fit,
        1.0 - case.order_semantics,
        1.0 - case.invariant_clarity,
        1.0 - case.complexity_awareness,
        1.0 - case.overflow_handling,
        1.0 - case.interpretability,
        1.0 - case.representation_risk_documentation,
        1.0 - case.governance_readiness,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 82 and risk <= 22:
        return "strong sequence-structure posture with clear order semantics, invariants, complexity, and governance"
    if quality >= 68 and risk <= 38:
        return "usable sequence-structure posture with review needs"
    if risk >= 55:
        return "high sequence-structure risk; operation fit, order semantics, or overflow handling may be unclear"
    return "partial sequence-structure posture; strengthen invariants, traversal, memory, or governance"


def load_cases(path: Path) -> list[SequenceStructureCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            SequenceStructureCase(
                row["case_name"],
                row["problem_context"],
                row["structure_choice"],
                float(row["operation_fit"]),
                float(row["order_semantics"]),
                float(row["invariant_clarity"]),
                float(row["complexity_awareness"]),
                float(row["memory_behavior"]),
                float(row["overflow_handling"]),
                float(row["interpretability"]),
                float(row["traversal_support"]),
                float(row["representation_risk_documentation"]),
                float(row["governance_readiness"]),
            )
            for row in reader
        ]


def evaluate_cases(cases: list[SequenceStructureCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        quality = sequence_structure_quality(case)
        risk = sequence_structure_risk(case)
        rows.append({
            **asdict(case),
            "sequence_structure_quality": round(quality, 3),
            "sequence_structure_risk": round(risk, 3),
            "diagnostic": diagnose(quality, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_sequence_structure_quality": round(mean(float(row["sequence_structure_quality"]) for row in rows), 3),
        "average_sequence_structure_risk": round(mean(float(row["sequence_structure_risk"]) for row in rows), 3),
        "highest_quality_case": max(rows, key=lambda row: float(row["sequence_structure_quality"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["sequence_structure_risk"]))["case_name"],
        "interpretation": "Sequence-structure quality depends on operation fit, order semantics, invariants, complexity, memory behavior, overflow handling, interpretability, traversal, risk documentation, and governance.",
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
    rows = evaluate_cases(load_cases(article_root / "data" / "synthetic_sequence_structure_cases.csv"))
    summary = summarize(rows)
    write_csv(article_root / "outputs" / "tables" / "sequence_structure_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "sequence_structure_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "sequence_structure_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "sequence_structure_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
