from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class ParadigmStyleCase:
    case_name: str
    problem_context: str
    style_choice: str
    style_clarity: float
    state_visibility: float
    abstraction_fit: float
    composability: float
    testability: float
    error_handling: float
    traceability: float
    performance_fit: float
    team_readability: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def style_quality(case: ParadigmStyleCase) -> float:
    return clamp(100.0 * (
        0.12 * case.style_clarity
        + 0.10 * case.state_visibility
        + 0.10 * case.abstraction_fit
        + 0.10 * case.composability
        + 0.10 * case.testability
        + 0.10 * case.error_handling
        + 0.10 * case.traceability
        + 0.08 * case.performance_fit
        + 0.10 * case.team_readability
        + 0.10 * case.governance_readiness
    ))


def style_risk(case: ParadigmStyleCase) -> float:
    weak_points = [
        1.0 - case.style_clarity,
        1.0 - case.state_visibility,
        1.0 - case.abstraction_fit,
        1.0 - case.testability,
        1.0 - case.error_handling,
        1.0 - case.traceability,
        1.0 - case.team_readability,
        1.0 - case.governance_readiness,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 84 and risk <= 20:
        return "strong computational style with clear state, abstraction, tests, traceability, and governance"
    if quality >= 70 and risk <= 35:
        return "usable computational style with review needs"
    if risk >= 55:
        return "high style risk; hidden state, weak abstraction, poor tests, or weak governance may be present"
    return "partial computational style; strengthen clarity, state control, testing, traceability, or governance"


def load_cases(path: Path) -> list[ParadigmStyleCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            ParadigmStyleCase(
                row["case_name"],
                row["problem_context"],
                row["style_choice"],
                float(row["style_clarity"]),
                float(row["state_visibility"]),
                float(row["abstraction_fit"]),
                float(row["composability"]),
                float(row["testability"]),
                float(row["error_handling"]),
                float(row["traceability"]),
                float(row["performance_fit"]),
                float(row["team_readability"]),
                float(row["governance_readiness"]),
            )
            for row in reader
        ]


def evaluate_cases(cases: list[ParadigmStyleCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        quality = style_quality(case)
        risk = style_risk(case)
        rows.append({
            **asdict(case),
            "style_quality": round(quality, 3),
            "style_risk": round(risk, 3),
            "diagnostic": diagnose(quality, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_style_quality": round(mean(float(row["style_quality"]) for row in rows), 3),
        "average_style_risk": round(mean(float(row["style_risk"]) for row in rows), 3),
        "highest_quality_case": max(rows, key=lambda row: float(row["style_quality"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["style_risk"]))["case_name"],
        "interpretation": "Programming style quality depends on clarity, state visibility, abstraction fit, composition, testability, error handling, traceability, performance fit, readability, and governance.",
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
    rows = evaluate_cases(load_cases(article_root / "data" / "synthetic_programming_style_cases.csv"))
    summary = summarize(rows)
    write_csv(article_root / "outputs" / "tables" / "programming_paradigm_style_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "programming_paradigm_style_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "programming_paradigm_style_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "programming_paradigm_style_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
