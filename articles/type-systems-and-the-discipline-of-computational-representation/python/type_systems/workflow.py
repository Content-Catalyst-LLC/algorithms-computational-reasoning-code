from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class TypeRepresentationCase:
    case_name: str
    problem_context: str
    type_design_choice: str
    representation_clarity: float
    constraint_strength: float
    missingness_handling: float
    boundary_validation: float
    domain_fidelity: float
    error_specificity: float
    type_coverage: float
    interoperability: float
    testability: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def type_quality(case: TypeRepresentationCase) -> float:
    return clamp(100.0 * (
        0.12 * case.representation_clarity
        + 0.12 * case.constraint_strength
        + 0.10 * case.missingness_handling
        + 0.10 * case.boundary_validation
        + 0.10 * case.domain_fidelity
        + 0.10 * case.error_specificity
        + 0.10 * case.type_coverage
        + 0.08 * case.interoperability
        + 0.10 * case.testability
        + 0.08 * case.governance_readiness
    ))


def type_risk(case: TypeRepresentationCase) -> float:
    weak_points = [
        1.0 - case.representation_clarity,
        1.0 - case.constraint_strength,
        1.0 - case.missingness_handling,
        1.0 - case.boundary_validation,
        1.0 - case.domain_fidelity,
        1.0 - case.error_specificity,
        1.0 - case.type_coverage,
        1.0 - case.governance_readiness,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 84 and risk <= 20:
        return "strong type discipline with clear representation, constraints, boundaries, missingness, tests, and governance"
    if quality >= 70 and risk <= 35:
        return "usable type discipline with review needs"
    if risk >= 55:
        return "high representation risk; weak constraints, missingness handling, validation, or governance may be present"
    return "partial type discipline; strengthen representation, constraints, validation, or governance"


def load_cases(path: Path) -> list[TypeRepresentationCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            TypeRepresentationCase(
                row["case_name"],
                row["problem_context"],
                row["type_design_choice"],
                float(row["representation_clarity"]),
                float(row["constraint_strength"]),
                float(row["missingness_handling"]),
                float(row["boundary_validation"]),
                float(row["domain_fidelity"]),
                float(row["error_specificity"]),
                float(row["type_coverage"]),
                float(row["interoperability"]),
                float(row["testability"]),
                float(row["governance_readiness"]),
            )
            for row in reader
        ]


def evaluate_cases(cases: list[TypeRepresentationCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        quality = type_quality(case)
        risk = type_risk(case)
        rows.append({
            **asdict(case),
            "type_quality": round(quality, 3),
            "type_risk": round(risk, 3),
            "diagnostic": diagnose(quality, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_type_quality": round(mean(float(row["type_quality"]) for row in rows), 3),
        "average_type_risk": round(mean(float(row["type_risk"]) for row in rows), 3),
        "highest_quality_case": max(rows, key=lambda row: float(row["type_quality"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["type_risk"]))["case_name"],
        "interpretation": "Type discipline depends on representation clarity, constraints, missingness handling, boundary validation, domain fidelity, error specificity, coverage, interoperability, testability, and governance.",
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
    rows = evaluate_cases(load_cases(article_root / "data" / "synthetic_type_representation_cases.csv"))
    summary = summarize(rows)
    write_csv(article_root / "outputs" / "tables" / "type_representation_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "type_representation_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "type_representation_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "type_representation_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
