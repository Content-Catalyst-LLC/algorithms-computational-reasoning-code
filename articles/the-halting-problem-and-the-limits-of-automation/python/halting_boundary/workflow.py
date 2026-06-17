from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class HaltingBoundaryCase:
    case_name: str
    automation_context: str
    automation_claim: str
    program_scope_clarity: float
    termination_claim_clarity: float
    undecidability_awareness: float
    bounded_analysis_honesty: float
    unknown_status_handling: float
    timeout_policy: float
    false_certainty_risk_control: float
    human_review_pathway: float
    traceability: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def halting_boundary_quality(case: HaltingBoundaryCase) -> float:
    return clamp(100.0 * (
        0.10 * case.program_scope_clarity
        + 0.12 * case.termination_claim_clarity
        + 0.12 * case.undecidability_awareness
        + 0.10 * case.bounded_analysis_honesty
        + 0.10 * case.unknown_status_handling
        + 0.08 * case.timeout_policy
        + 0.12 * case.false_certainty_risk_control
        + 0.10 * case.human_review_pathway
        + 0.08 * case.traceability
        + 0.08 * case.governance_readiness
    ))


def automation_overclaim_risk(case: HaltingBoundaryCase) -> float:
    weak_points = [
        1.0 - case.termination_claim_clarity,
        1.0 - case.undecidability_awareness,
        1.0 - case.bounded_analysis_honesty,
        1.0 - case.unknown_status_handling,
        1.0 - case.false_certainty_risk_control,
        1.0 - case.human_review_pathway,
        1.0 - case.traceability,
        1.0 - case.governance_readiness,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 82 and risk <= 22:
        return "strong halting-boundary posture with clear automation limits"
    if quality >= 68 and risk <= 38:
        return "usable halting-boundary posture with review needs"
    if risk >= 55:
        return "high automation-overclaim risk; halting and unknown-status limits may be unclear"
    return "partial halting-boundary posture; strengthen boundedness, unknown handling, review, or governance"


def load_cases(path: Path) -> list[HaltingBoundaryCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            HaltingBoundaryCase(
                row["case_name"],
                row["automation_context"],
                row["automation_claim"],
                float(row["program_scope_clarity"]),
                float(row["termination_claim_clarity"]),
                float(row["undecidability_awareness"]),
                float(row["bounded_analysis_honesty"]),
                float(row["unknown_status_handling"]),
                float(row["timeout_policy"]),
                float(row["false_certainty_risk_control"]),
                float(row["human_review_pathway"]),
                float(row["traceability"]),
                float(row["governance_readiness"]),
            )
            for row in reader
        ]


def evaluate_cases(cases: list[HaltingBoundaryCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        quality = halting_boundary_quality(case)
        risk = automation_overclaim_risk(case)
        rows.append({
            **asdict(case),
            "halting_boundary_quality": round(quality, 3),
            "automation_overclaim_risk": round(risk, 3),
            "diagnostic": diagnose(quality, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_halting_boundary_quality": round(mean(float(row["halting_boundary_quality"]) for row in rows), 3),
        "average_automation_overclaim_risk": round(mean(float(row["automation_overclaim_risk"]) for row in rows), 3),
        "highest_quality_case": max(rows, key=lambda row: float(row["halting_boundary_quality"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["automation_overclaim_risk"]))["case_name"],
        "interpretation": "Halting-boundary quality depends on scope clarity, termination claims, undecidability awareness, bounded-analysis honesty, unknown-status handling, timeout policy, false-certainty control, human review, traceability, and governance.",
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
    rows = evaluate_cases(load_cases(article_root / "data" / "synthetic_halting_boundary_cases.csv"))
    summary = summarize(rows)
    write_csv(article_root / "outputs" / "tables" / "halting_boundary_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "halting_boundary_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "halting_boundary_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "halting_boundary_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
