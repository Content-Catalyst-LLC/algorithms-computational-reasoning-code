from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class FormalizationCase:
    case_name: str
    real_world_concern: str
    formal_task: str
    input_clarity: float
    output_clarity: float
    constraint_clarity: float
    state_definition: float
    objective_alignment: float
    assumption_documentation: float
    edge_case_handling: float
    stopping_condition_clarity: float
    evaluation_quality: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def load_cases(path: Path) -> list[FormalizationCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            FormalizationCase(
                case_name=row["case_name"],
                real_world_concern=row["real_world_concern"],
                formal_task=row["formal_task"],
                input_clarity=float(row["input_clarity"]),
                output_clarity=float(row["output_clarity"]),
                constraint_clarity=float(row["constraint_clarity"]),
                state_definition=float(row["state_definition"]),
                objective_alignment=float(row["objective_alignment"]),
                assumption_documentation=float(row["assumption_documentation"]),
                edge_case_handling=float(row["edge_case_handling"]),
                stopping_condition_clarity=float(row["stopping_condition_clarity"]),
                evaluation_quality=float(row["evaluation_quality"]),
                governance_readiness=float(row["governance_readiness"]),
            )
            for row in reader
        ]


def formalization_score(case: FormalizationCase) -> float:
    return clamp(
        100.0 * (
            0.10 * case.input_clarity
            + 0.10 * case.output_clarity
            + 0.10 * case.constraint_clarity
            + 0.08 * case.state_definition
            + 0.14 * case.objective_alignment
            + 0.12 * case.assumption_documentation
            + 0.10 * case.edge_case_handling
            + 0.08 * case.stopping_condition_clarity
            + 0.10 * case.evaluation_quality
            + 0.08 * case.governance_readiness
        )
    )


def formalization_risk(case: FormalizationCase) -> float:
    weak_points = [
        1.0 - case.input_clarity,
        1.0 - case.output_clarity,
        1.0 - case.constraint_clarity,
        1.0 - case.objective_alignment,
        1.0 - case.assumption_documentation,
        1.0 - case.edge_case_handling,
        1.0 - case.evaluation_quality,
        1.0 - case.governance_readiness,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(score: float, risk: float) -> str:
    if score >= 80 and risk <= 25:
        return "strong formalization with clear procedure boundaries"
    if score >= 65 and risk <= 40:
        return "usable formalization with review needs"
    if risk >= 55:
        return "high formalization risk; reframe before automation"
    return "partial formalization; assumptions and evaluation need strengthening"


def evaluate_cases(cases: list[FormalizationCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        score = formalization_score(case)
        risk = formalization_risk(case)
        rows.append({
            **asdict(case),
            "formalization_score": round(score, 3),
            "formalization_risk": round(risk, 3),
            "diagnostic": diagnose(score, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_formalization_score": round(mean(float(row["formalization_score"]) for row in rows), 3),
        "average_formalization_risk": round(mean(float(row["formalization_risk"]) for row in rows), 3),
        "highest_score_case": max(rows, key=lambda row: float(row["formalization_score"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["formalization_risk"]))["case_name"],
        "interpretation": "Formalization quality depends on clear inputs, outputs, constraints, states, objectives, assumptions, edge cases, stopping conditions, evaluation, and governance."
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
    cases = load_cases(article_root / "data" / "synthetic_formalization_cases.csv")
    rows = evaluate_cases(cases)
    summary = summarize(rows)

    write_csv(article_root / "outputs" / "tables" / "formalization_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "formalization_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "formalization_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "formalization_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
