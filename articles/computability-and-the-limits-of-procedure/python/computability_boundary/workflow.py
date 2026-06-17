from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class ComputabilityBoundaryCase:
    case_name: str
    computational_context: str
    procedural_claim: str
    procedure_definition: float
    input_domain_clarity: float
    decision_status_clarity: float
    termination_guarantee: float
    recognizability_status: float
    reduction_awareness: float
    approximation_honesty: float
    automation_scope_clarity: float
    traceability: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def computability_boundary_quality(case: ComputabilityBoundaryCase) -> float:
    return clamp(100.0 * (
        0.10 * case.procedure_definition
        + 0.10 * case.input_domain_clarity
        + 0.12 * case.decision_status_clarity
        + 0.12 * case.termination_guarantee
        + 0.10 * case.recognizability_status
        + 0.10 * case.reduction_awareness
        + 0.10 * case.approximation_honesty
        + 0.10 * case.automation_scope_clarity
        + 0.08 * case.traceability
        + 0.08 * case.governance_readiness
    ))


def procedural_overclaim_risk(case: ComputabilityBoundaryCase) -> float:
    weak_points = [
        1.0 - case.decision_status_clarity,
        1.0 - case.termination_guarantee,
        1.0 - case.recognizability_status,
        1.0 - case.reduction_awareness,
        1.0 - case.approximation_honesty,
        1.0 - case.automation_scope_clarity,
        1.0 - case.traceability,
        1.0 - case.governance_readiness,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 82 and risk <= 22:
        return "strong computability-boundary posture with clear procedure limits"
    if quality >= 68 and risk <= 38:
        return "usable computability-boundary posture with review needs"
    if risk >= 55:
        return "high procedural overclaim risk; automation limits may be unclear"
    return "partial computability-boundary posture; clarify decidability, termination, approximation, or governance"


def load_cases(path: Path) -> list[ComputabilityBoundaryCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            ComputabilityBoundaryCase(
                row["case_name"],
                row["computational_context"],
                row["procedural_claim"],
                float(row["procedure_definition"]),
                float(row["input_domain_clarity"]),
                float(row["decision_status_clarity"]),
                float(row["termination_guarantee"]),
                float(row["recognizability_status"]),
                float(row["reduction_awareness"]),
                float(row["approximation_honesty"]),
                float(row["automation_scope_clarity"]),
                float(row["traceability"]),
                float(row["governance_readiness"]),
            )
            for row in reader
        ]


def evaluate_cases(cases: list[ComputabilityBoundaryCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        quality = computability_boundary_quality(case)
        risk = procedural_overclaim_risk(case)
        rows.append({
            **asdict(case),
            "computability_boundary_quality": round(quality, 3),
            "procedural_overclaim_risk": round(risk, 3),
            "diagnostic": diagnose(quality, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_computability_boundary_quality": round(mean(float(row["computability_boundary_quality"]) for row in rows), 3),
        "average_procedural_overclaim_risk": round(mean(float(row["procedural_overclaim_risk"]) for row in rows), 3),
        "highest_quality_case": max(rows, key=lambda row: float(row["computability_boundary_quality"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["procedural_overclaim_risk"]))["case_name"],
        "interpretation": "Computability-boundary quality depends on procedure definition, input-domain clarity, decision status, termination guarantees, recognizability, reduction awareness, approximation honesty, automation scope, traceability, and governance.",
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
    rows = evaluate_cases(load_cases(article_root / "data" / "synthetic_computability_boundary_cases.csv"))
    summary = summarize(rows)
    write_csv(article_root / "outputs" / "tables" / "computability_boundary_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "computability_boundary_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "computability_boundary_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "computability_boundary_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
