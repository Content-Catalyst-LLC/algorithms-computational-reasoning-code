from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class LambdaExpressionCase:
    case_name: str
    computation_context: str
    formal_claim: str
    expression_clarity: float
    binding_safety: float
    substitution_discipline: float
    reduction_traceability: float
    evaluation_strategy_clarity: float
    recursion_awareness: float
    type_discipline_clarity: float
    proof_connection: float
    implementation_relevance: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def lambda_reasoning_quality(case: LambdaExpressionCase) -> float:
    return clamp(100.0 * (
        0.10 * case.expression_clarity
        + 0.12 * case.binding_safety
        + 0.12 * case.substitution_discipline
        + 0.10 * case.reduction_traceability
        + 0.10 * case.evaluation_strategy_clarity
        + 0.08 * case.recursion_awareness
        + 0.12 * case.type_discipline_clarity
        + 0.08 * case.proof_connection
        + 0.08 * case.implementation_relevance
        + 0.10 * case.governance_readiness
    ))


def formalization_risk(case: LambdaExpressionCase) -> float:
    weak_points = [
        1.0 - case.binding_safety,
        1.0 - case.substitution_discipline,
        1.0 - case.reduction_traceability,
        1.0 - case.evaluation_strategy_clarity,
        1.0 - case.recursion_awareness,
        1.0 - case.type_discipline_clarity,
        1.0 - case.proof_connection,
        1.0 - case.governance_readiness,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 82 and risk <= 22:
        return "strong lambda-calculus reasoning posture with clear binding, substitution, typing, and reduction evidence"
    if quality >= 68 and risk <= 38:
        return "usable lambda-calculus reasoning posture with review needs"
    if risk >= 55:
        return "high formalization risk; binding, substitution, typing, or evaluation assumptions may be unclear"
    return "partial lambda-calculus reasoning posture; strengthen expression structure, traces, types, or governance"


def load_cases(path: Path) -> list[LambdaExpressionCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            LambdaExpressionCase(
                row["case_name"],
                row["computation_context"],
                row["formal_claim"],
                float(row["expression_clarity"]),
                float(row["binding_safety"]),
                float(row["substitution_discipline"]),
                float(row["reduction_traceability"]),
                float(row["evaluation_strategy_clarity"]),
                float(row["recursion_awareness"]),
                float(row["type_discipline_clarity"]),
                float(row["proof_connection"]),
                float(row["implementation_relevance"]),
                float(row["governance_readiness"]),
            )
            for row in reader
        ]


def evaluate_cases(cases: list[LambdaExpressionCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        quality = lambda_reasoning_quality(case)
        risk = formalization_risk(case)
        rows.append({
            **asdict(case),
            "lambda_reasoning_quality": round(quality, 3),
            "formalization_risk": round(risk, 3),
            "diagnostic": diagnose(quality, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_lambda_reasoning_quality": round(mean(float(row["lambda_reasoning_quality"]) for row in rows), 3),
        "average_formalization_risk": round(mean(float(row["formalization_risk"]) for row in rows), 3),
        "highest_quality_case": max(rows, key=lambda row: float(row["lambda_reasoning_quality"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["formalization_risk"]))["case_name"],
        "interpretation": "Lambda-calculus reasoning quality depends on expression clarity, binding safety, substitution discipline, reduction traceability, evaluation strategy, recursion awareness, type discipline, proof connection, implementation relevance, and governance.",
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
    rows = evaluate_cases(load_cases(article_root / "data" / "synthetic_lambda_expression_cases.csv"))
    summary = summarize(rows)
    write_csv(article_root / "outputs" / "tables" / "lambda_expression_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "lambda_expression_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "lambda_expression_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "lambda_expression_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
