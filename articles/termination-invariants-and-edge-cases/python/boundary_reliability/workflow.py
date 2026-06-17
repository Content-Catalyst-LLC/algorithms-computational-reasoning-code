from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class BoundaryReliabilityCase:
    case_name: str
    computational_context: str
    reliability_claim: str
    stopping_condition_clarity: float
    progress_measure_definition: float
    invariant_coverage: float
    boundary_case_coverage: float
    invalid_input_handling: float
    recursion_safety: float
    numerical_edge_handling: float
    concurrency_edge_awareness: float
    counterexample_traceability: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def reliability_quality(case: BoundaryReliabilityCase) -> float:
    return clamp(100.0 * (
        0.12 * case.stopping_condition_clarity
        + 0.12 * case.progress_measure_definition
        + 0.12 * case.invariant_coverage
        + 0.10 * case.boundary_case_coverage
        + 0.10 * case.invalid_input_handling
        + 0.08 * case.recursion_safety
        + 0.08 * case.numerical_edge_handling
        + 0.08 * case.concurrency_edge_awareness
        + 0.10 * case.counterexample_traceability
        + 0.10 * case.governance_readiness
    ))


def reliability_risk(case: BoundaryReliabilityCase) -> float:
    weak_points = [
        1.0 - case.stopping_condition_clarity,
        1.0 - case.progress_measure_definition,
        1.0 - case.invariant_coverage,
        1.0 - case.boundary_case_coverage,
        1.0 - case.invalid_input_handling,
        1.0 - case.recursion_safety,
        1.0 - case.numerical_edge_handling,
        1.0 - case.counterexample_traceability,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 82 and risk <= 22:
        return "strong boundary reliability posture with clear termination, invariants, and edge-case handling"
    if quality >= 68 and risk <= 38:
        return "usable reliability posture with review needs"
    if risk >= 55:
        return "high boundary risk; termination, invariants, or edge cases may be weakly handled"
    return "partial reliability posture; strengthen stopping conditions, invariants, boundary tests, or governance"


def load_cases(path: Path) -> list[BoundaryReliabilityCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            BoundaryReliabilityCase(
                row["case_name"],
                row["computational_context"],
                row["reliability_claim"],
                float(row["stopping_condition_clarity"]),
                float(row["progress_measure_definition"]),
                float(row["invariant_coverage"]),
                float(row["boundary_case_coverage"]),
                float(row["invalid_input_handling"]),
                float(row["recursion_safety"]),
                float(row["numerical_edge_handling"]),
                float(row["concurrency_edge_awareness"]),
                float(row["counterexample_traceability"]),
                float(row["governance_readiness"]),
            )
            for row in reader
        ]


def evaluate_cases(cases: list[BoundaryReliabilityCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        quality = reliability_quality(case)
        risk = reliability_risk(case)
        rows.append({
            **asdict(case),
            "reliability_quality": round(quality, 3),
            "reliability_risk": round(risk, 3),
            "diagnostic": diagnose(quality, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_reliability_quality": round(mean(float(row["reliability_quality"]) for row in rows), 3),
        "average_reliability_risk": round(mean(float(row["reliability_risk"]) for row in rows), 3),
        "highest_quality_case": max(rows, key=lambda row: float(row["reliability_quality"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["reliability_risk"]))["case_name"],
        "interpretation": "Boundary reliability depends on stopping conditions, progress measures, invariants, boundary cases, invalid-input handling, recursion safety, numerical edges, concurrency edges, counterexamples, and governance.",
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
    rows = evaluate_cases(load_cases(article_root / "data" / "synthetic_boundary_reliability_cases.csv"))
    summary = summarize(rows)
    write_csv(article_root / "outputs" / "tables" / "termination_invariant_edge_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "termination_invariant_edge_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "termination_invariant_edge_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "termination_invariant_edge_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
