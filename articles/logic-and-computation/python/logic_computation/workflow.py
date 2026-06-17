from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class LogicCase:
    case_name: str
    system_context: str
    logical_structure: str
    rule_clarity: float
    predicate_definition: float
    input_validity: float
    contradiction_control: float
    inference_traceability: float
    constraint_coverage: float
    testability: float
    verification_readiness: float
    explainability: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def load_cases(path: Path) -> list[LogicCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            LogicCase(
                case_name=row["case_name"],
                system_context=row["system_context"],
                logical_structure=row["logical_structure"],
                rule_clarity=float(row["rule_clarity"]),
                predicate_definition=float(row["predicate_definition"]),
                input_validity=float(row["input_validity"]),
                contradiction_control=float(row["contradiction_control"]),
                inference_traceability=float(row["inference_traceability"]),
                constraint_coverage=float(row["constraint_coverage"]),
                testability=float(row["testability"]),
                verification_readiness=float(row["verification_readiness"]),
                explainability=float(row["explainability"]),
                governance_readiness=float(row["governance_readiness"]),
            )
            for row in reader
        ]


def logic_quality(case: LogicCase) -> float:
    return clamp(
        100.0 * (
            0.12 * case.rule_clarity
            + 0.12 * case.predicate_definition
            + 0.10 * case.input_validity
            + 0.10 * case.contradiction_control
            + 0.12 * case.inference_traceability
            + 0.10 * case.constraint_coverage
            + 0.10 * case.testability
            + 0.08 * case.verification_readiness
            + 0.08 * case.explainability
            + 0.08 * case.governance_readiness
        )
    )


def logic_risk(case: LogicCase) -> float:
    weak_points = [
        1.0 - case.rule_clarity,
        1.0 - case.predicate_definition,
        1.0 - case.input_validity,
        1.0 - case.contradiction_control,
        1.0 - case.inference_traceability,
        1.0 - case.constraint_coverage,
        1.0 - case.testability,
        1.0 - case.explainability,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 80 and risk <= 25:
        return "strong logical structure with traceable inference and low contradiction risk"
    if quality >= 65 and risk <= 40:
        return "usable logical structure with review needs"
    if risk >= 55:
        return "high logic risk; rules, predicates, or constraints may be unclear or inconsistent"
    return "partial logical structure; improve definitions, traceability, tests, or governance"


def evaluate_cases(cases: list[LogicCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        quality = logic_quality(case)
        risk = logic_risk(case)
        rows.append({
            **asdict(case),
            "logic_quality": round(quality, 3),
            "logic_risk": round(risk, 3),
            "diagnostic": diagnose(quality, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_logic_quality": round(mean(float(row["logic_quality"]) for row in rows), 3),
        "average_logic_risk": round(mean(float(row["logic_risk"]) for row in rows), 3),
        "highest_quality_case": max(rows, key=lambda row: float(row["logic_quality"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["logic_risk"]))["case_name"],
        "interpretation": "Logic quality depends on clear rules, defined predicates, valid inputs, contradiction control, traceable inference, constraint coverage, testability, verification readiness, explainability, and governance."
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
    cases = load_cases(article_root / "data" / "synthetic_logic_computation_cases.csv")
    rows = evaluate_cases(cases)
    summary = summarize(rows)

    write_csv(article_root / "outputs" / "tables" / "logic_computation_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "logic_computation_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "logic_computation_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "logic_computation_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
