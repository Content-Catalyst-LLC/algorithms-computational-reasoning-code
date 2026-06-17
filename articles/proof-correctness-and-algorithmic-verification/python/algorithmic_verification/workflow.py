from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class VerificationCase:
    case_name: str
    computational_context: str
    correctness_claim: str
    specification_clarity: float
    precondition_definition: float
    postcondition_definition: float
    invariant_coverage: float
    termination_evidence: float
    test_coverage: float
    counterexample_handling: float
    static_check_support: float
    traceability: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def verification_quality(case: VerificationCase) -> float:
    return clamp(100.0 * (
        0.12 * case.specification_clarity
        + 0.10 * case.precondition_definition
        + 0.10 * case.postcondition_definition
        + 0.12 * case.invariant_coverage
        + 0.10 * case.termination_evidence
        + 0.10 * case.test_coverage
        + 0.10 * case.counterexample_handling
        + 0.08 * case.static_check_support
        + 0.10 * case.traceability
        + 0.08 * case.governance_readiness
    ))


def verification_risk(case: VerificationCase) -> float:
    weak_points = [
        1.0 - case.specification_clarity,
        1.0 - case.precondition_definition,
        1.0 - case.postcondition_definition,
        1.0 - case.invariant_coverage,
        1.0 - case.termination_evidence,
        1.0 - case.test_coverage,
        1.0 - case.counterexample_handling,
        1.0 - case.traceability,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 82 and risk <= 22:
        return "strong verification posture with clear specification, evidence, and traceability"
    if quality >= 68 and risk <= 38:
        return "usable verification posture with review needs"
    if risk >= 55:
        return "high verification risk; correctness claims may be underspecified or weakly evidenced"
    return "partial verification posture; strengthen specifications, invariants, tests, proofs, or governance"


def load_cases(path: Path) -> list[VerificationCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            VerificationCase(
                row["case_name"],
                row["computational_context"],
                row["correctness_claim"],
                float(row["specification_clarity"]),
                float(row["precondition_definition"]),
                float(row["postcondition_definition"]),
                float(row["invariant_coverage"]),
                float(row["termination_evidence"]),
                float(row["test_coverage"]),
                float(row["counterexample_handling"]),
                float(row["static_check_support"]),
                float(row["traceability"]),
                float(row["governance_readiness"]),
            )
            for row in reader
        ]


def evaluate_cases(cases: list[VerificationCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        quality = verification_quality(case)
        risk = verification_risk(case)
        rows.append({
            **asdict(case),
            "verification_quality": round(quality, 3),
            "verification_risk": round(risk, 3),
            "diagnostic": diagnose(quality, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_verification_quality": round(mean(float(row["verification_quality"]) for row in rows), 3),
        "average_verification_risk": round(mean(float(row["verification_risk"]) for row in rows), 3),
        "highest_quality_case": max(rows, key=lambda row: float(row["verification_quality"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["verification_risk"]))["case_name"],
        "interpretation": "Verification quality depends on specification clarity, preconditions, postconditions, invariants, termination evidence, tests, counterexamples, static checks, traceability, and governance.",
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
    rows = evaluate_cases(load_cases(article_root / "data" / "synthetic_verification_cases.csv"))
    summary = summarize(rows)
    write_csv(article_root / "outputs" / "tables" / "algorithmic_verification_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "algorithmic_verification_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "algorithmic_verification_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "algorithmic_verification_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
