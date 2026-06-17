from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class BoundaryCase:
    case_name: str
    procedure_type: str
    input_description: str
    output_description: str
    state_description: str
    stopping_condition: str
    input_clarity: float
    output_clarity: float
    state_definition: float
    transition_clarity: float
    stopping_condition_clarity: float
    validation_quality: float
    edge_case_handling: float
    failure_reporting: float
    interpretability: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def load_cases(path: Path) -> list[BoundaryCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            BoundaryCase(
                case_name=row["case_name"],
                procedure_type=row["procedure_type"],
                input_description=row["input_description"],
                output_description=row["output_description"],
                state_description=row["state_description"],
                stopping_condition=row["stopping_condition"],
                input_clarity=float(row["input_clarity"]),
                output_clarity=float(row["output_clarity"]),
                state_definition=float(row["state_definition"]),
                transition_clarity=float(row["transition_clarity"]),
                stopping_condition_clarity=float(row["stopping_condition_clarity"]),
                validation_quality=float(row["validation_quality"]),
                edge_case_handling=float(row["edge_case_handling"]),
                failure_reporting=float(row["failure_reporting"]),
                interpretability=float(row["interpretability"]),
                governance_readiness=float(row["governance_readiness"]),
            )
            for row in reader
        ]


def boundary_score(case: BoundaryCase) -> float:
    return clamp(
        100.0 * (
            0.12 * case.input_clarity
            + 0.12 * case.output_clarity
            + 0.12 * case.state_definition
            + 0.10 * case.transition_clarity
            + 0.12 * case.stopping_condition_clarity
            + 0.10 * case.validation_quality
            + 0.08 * case.edge_case_handling
            + 0.08 * case.failure_reporting
            + 0.08 * case.interpretability
            + 0.08 * case.governance_readiness
        )
    )


def boundary_risk(case: BoundaryCase) -> float:
    weak_points = [
        1.0 - case.input_clarity,
        1.0 - case.output_clarity,
        1.0 - case.state_definition,
        1.0 - case.stopping_condition_clarity,
        1.0 - case.edge_case_handling,
        1.0 - case.failure_reporting,
        1.0 - case.interpretability,
        1.0 - case.governance_readiness,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(score: float, risk: float) -> str:
    if score >= 80 and risk <= 25:
        return "strong boundary specification with clear state and stopping rules"
    if score >= 65 and risk <= 40:
        return "usable boundary specification with review needs"
    if risk >= 55:
        return "high procedural-boundary risk; clarify inputs, outputs, states, or stopping rules"
    return "partial boundary specification; validation, failure reporting, or interpretation need strengthening"


def evaluate_cases(cases: list[BoundaryCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        score = boundary_score(case)
        risk = boundary_risk(case)
        rows.append({
            **asdict(case),
            "boundary_score": round(score, 3),
            "boundary_risk": round(risk, 3),
            "diagnostic": diagnose(score, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_boundary_score": round(mean(float(row["boundary_score"]) for row in rows), 3),
        "average_boundary_risk": round(mean(float(row["boundary_risk"]) for row in rows), 3),
        "highest_score_case": max(rows, key=lambda row: float(row["boundary_score"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["boundary_risk"]))["case_name"],
        "interpretation": "Procedural boundary quality depends on clear inputs, outputs, states, transitions, stopping conditions, validation, edge cases, failure reporting, interpretation, and governance."
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
    cases = load_cases(article_root / "data" / "synthetic_boundary_state_cases.csv")
    rows = evaluate_cases(cases)
    summary = summarize(rows)

    write_csv(article_root / "outputs" / "tables" / "boundary_state_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "boundary_state_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "boundary_state_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "boundary_state_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
