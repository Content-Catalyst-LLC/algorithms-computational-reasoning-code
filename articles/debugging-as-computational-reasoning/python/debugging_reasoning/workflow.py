from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class DebugCase:
    case_name: str
    system_context: str
    failure_description: str
    expected_behavior: str
    observed_behavior: str
    reproducibility: float
    expected_behavior_clarity: float
    trace_quality: float
    hypothesis_strength: float
    isolation_quality: float
    edge_case_awareness: float
    fix_verification: float
    regression_testing: float
    documentation_quality: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def load_cases(path: Path) -> list[DebugCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            DebugCase(
                case_name=row["case_name"],
                system_context=row["system_context"],
                failure_description=row["failure_description"],
                expected_behavior=row["expected_behavior"],
                observed_behavior=row["observed_behavior"],
                reproducibility=float(row["reproducibility"]),
                expected_behavior_clarity=float(row["expected_behavior_clarity"]),
                trace_quality=float(row["trace_quality"]),
                hypothesis_strength=float(row["hypothesis_strength"]),
                isolation_quality=float(row["isolation_quality"]),
                edge_case_awareness=float(row["edge_case_awareness"]),
                fix_verification=float(row["fix_verification"]),
                regression_testing=float(row["regression_testing"]),
                documentation_quality=float(row["documentation_quality"]),
                governance_readiness=float(row["governance_readiness"]),
            )
            for row in reader
        ]


def debugging_quality(case: DebugCase) -> float:
    return clamp(
        100.0 * (
            0.12 * case.reproducibility
            + 0.10 * case.expected_behavior_clarity
            + 0.10 * case.trace_quality
            + 0.10 * case.hypothesis_strength
            + 0.10 * case.isolation_quality
            + 0.10 * case.edge_case_awareness
            + 0.12 * case.fix_verification
            + 0.10 * case.regression_testing
            + 0.08 * case.documentation_quality
            + 0.08 * case.governance_readiness
        )
    )


def recurrence_risk(case: DebugCase) -> float:
    weak_points = [
        1.0 - case.reproducibility,
        1.0 - case.expected_behavior_clarity,
        1.0 - case.trace_quality,
        1.0 - case.isolation_quality,
        1.0 - case.edge_case_awareness,
        1.0 - case.fix_verification,
        1.0 - case.regression_testing,
        1.0 - case.documentation_quality,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 80 and risk <= 25:
        return "strong debugging process with evidence, verification, and regression coverage"
    if quality >= 65 and risk <= 40:
        return "usable debugging process with review needs"
    if risk >= 55:
        return "high recurrence risk; failure may return or remain poorly understood"
    return "partial debugging process; improve reproduction, tracing, verification, or documentation"


def evaluate_cases(cases: list[DebugCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        quality = debugging_quality(case)
        risk = recurrence_risk(case)
        rows.append({
            **asdict(case),
            "debugging_quality": round(quality, 3),
            "recurrence_risk": round(risk, 3),
            "diagnostic": diagnose(quality, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_debugging_quality": round(mean(float(row["debugging_quality"]) for row in rows), 3),
        "average_recurrence_risk": round(mean(float(row["recurrence_risk"]) for row in rows), 3),
        "highest_quality_case": max(rows, key=lambda row: float(row["debugging_quality"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["recurrence_risk"]))["case_name"],
        "interpretation": "Debugging quality depends on reproduction, expected-behavior clarity, traces, hypotheses, isolation, edge cases, fix verification, regression tests, documentation, and governance."
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
    cases = load_cases(article_root / "data" / "synthetic_debugging_reasoning_cases.csv")
    rows = evaluate_cases(cases)
    summary = summarize(rows)

    write_csv(article_root / "outputs" / "tables" / "debugging_reasoning_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "debugging_reasoning_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "debugging_reasoning_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "debugging_reasoning_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
