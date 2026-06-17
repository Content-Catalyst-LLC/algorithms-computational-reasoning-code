from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class AbstractionCase:
    case_name: str
    real_system: str
    abstraction: str
    representation_clarity: float
    scope_definition: float
    detail_preservation: float
    assumption_documentation: float
    testability: float
    interpretability: float
    reuse_safety: float
    uncertainty_visibility: float
    governance_readiness: float
    risk_awareness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def load_cases(path: Path) -> list[AbstractionCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            AbstractionCase(
                case_name=row["case_name"],
                real_system=row["real_system"],
                abstraction=row["abstraction"],
                representation_clarity=float(row["representation_clarity"]),
                scope_definition=float(row["scope_definition"]),
                detail_preservation=float(row["detail_preservation"]),
                assumption_documentation=float(row["assumption_documentation"]),
                testability=float(row["testability"]),
                interpretability=float(row["interpretability"]),
                reuse_safety=float(row["reuse_safety"]),
                uncertainty_visibility=float(row["uncertainty_visibility"]),
                governance_readiness=float(row["governance_readiness"]),
                risk_awareness=float(row["risk_awareness"]),
            )
            for row in reader
        ]


def abstraction_score(case: AbstractionCase) -> float:
    return clamp(
        100.0 * (
            0.12 * case.representation_clarity
            + 0.10 * case.scope_definition
            + 0.12 * case.detail_preservation
            + 0.12 * case.assumption_documentation
            + 0.10 * case.testability
            + 0.12 * case.interpretability
            + 0.08 * case.reuse_safety
            + 0.08 * case.uncertainty_visibility
            + 0.08 * case.governance_readiness
            + 0.08 * case.risk_awareness
        )
    )


def abstraction_risk(case: AbstractionCase) -> float:
    weak_points = [
        1.0 - case.scope_definition,
        1.0 - case.detail_preservation,
        1.0 - case.assumption_documentation,
        1.0 - case.interpretability,
        1.0 - case.reuse_safety,
        1.0 - case.uncertainty_visibility,
        1.0 - case.governance_readiness,
        1.0 - case.risk_awareness,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(score: float, risk: float) -> str:
    if score >= 80 and risk <= 25:
        return "strong abstraction with clear scope and interpretation"
    if score >= 65 and risk <= 40:
        return "usable abstraction with review needs"
    if risk >= 55:
        return "high abstraction risk; representation may hide important context"
    return "partial abstraction; scope, assumptions, or interpretation need strengthening"


def evaluate_cases(cases: list[AbstractionCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        score = abstraction_score(case)
        risk = abstraction_risk(case)
        rows.append({
            **asdict(case),
            "abstraction_score": round(score, 3),
            "abstraction_risk": round(risk, 3),
            "diagnostic": diagnose(score, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_abstraction_score": round(mean(float(row["abstraction_score"]) for row in rows), 3),
        "average_abstraction_risk": round(mean(float(row["abstraction_risk"]) for row in rows), 3),
        "highest_score_case": max(rows, key=lambda row: float(row["abstraction_score"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["abstraction_risk"]))["case_name"],
        "interpretation": "Abstraction quality depends on clear representation, scope, preserved detail, assumptions, testability, interpretation, reuse safety, uncertainty visibility, governance, and risk awareness."
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
    cases = load_cases(article_root / "data" / "synthetic_abstraction_cases.csv")
    rows = evaluate_cases(cases)
    summary = summarize(rows)

    write_csv(article_root / "outputs" / "tables" / "abstraction_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "abstraction_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "abstraction_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "abstraction_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
