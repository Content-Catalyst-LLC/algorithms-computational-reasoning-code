from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class FormalMethodsCase:
    case_name: str
    verification_context: str
    formal_claim: str
    specification_clarity: float
    assumption_documentation: float
    invariant_strength: float
    proof_obligation_traceability: float
    machine_check_status: float
    counterexample_handling: float
    model_scope_clarity: float
    refinement_evidence: float
    unknown_status_handling: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def formal_methods_quality(case: FormalMethodsCase) -> float:
    return clamp(100.0 * (
        0.12 * case.specification_clarity
        + 0.10 * case.assumption_documentation
        + 0.10 * case.invariant_strength
        + 0.12 * case.proof_obligation_traceability
        + 0.12 * case.machine_check_status
        + 0.10 * case.counterexample_handling
        + 0.10 * case.model_scope_clarity
        + 0.08 * case.refinement_evidence
        + 0.08 * case.unknown_status_handling
        + 0.08 * case.governance_readiness
    ))


def verification_overclaim_risk(case: FormalMethodsCase) -> float:
    weak_points = [
        1.0 - case.specification_clarity,
        1.0 - case.assumption_documentation,
        1.0 - case.proof_obligation_traceability,
        1.0 - case.machine_check_status,
        1.0 - case.model_scope_clarity,
        1.0 - case.refinement_evidence,
        1.0 - case.unknown_status_handling,
        1.0 - case.governance_readiness,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 82 and risk <= 22:
        return "strong formal-methods posture with clear machine-checked evidence and interpretation boundaries"
    if quality >= 68 and risk <= 38:
        return "usable formal-methods posture with review needs"
    if risk >= 55:
        return "high verification-overclaim risk; formal evidence or scope may be unclear"
    return "partial formal-methods posture; strengthen specification, obligations, machine checks, scope, or governance"


def load_cases(path: Path) -> list[FormalMethodsCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            FormalMethodsCase(
                row["case_name"],
                row["verification_context"],
                row["formal_claim"],
                float(row["specification_clarity"]),
                float(row["assumption_documentation"]),
                float(row["invariant_strength"]),
                float(row["proof_obligation_traceability"]),
                float(row["machine_check_status"]),
                float(row["counterexample_handling"]),
                float(row["model_scope_clarity"]),
                float(row["refinement_evidence"]),
                float(row["unknown_status_handling"]),
                float(row["governance_readiness"]),
            )
            for row in reader
        ]


def evaluate_cases(cases: list[FormalMethodsCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        quality = formal_methods_quality(case)
        risk = verification_overclaim_risk(case)
        rows.append({
            **asdict(case),
            "formal_methods_quality": round(quality, 3),
            "verification_overclaim_risk": round(risk, 3),
            "diagnostic": diagnose(quality, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_formal_methods_quality": round(mean(float(row["formal_methods_quality"]) for row in rows), 3),
        "average_verification_overclaim_risk": round(mean(float(row["verification_overclaim_risk"]) for row in rows), 3),
        "highest_quality_case": max(rows, key=lambda row: float(row["formal_methods_quality"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["verification_overclaim_risk"]))["case_name"],
        "interpretation": "Formal-methods quality depends on specification clarity, documented assumptions, invariants, proof obligations, machine checks, counterexamples, model scope, refinement evidence, unknown-status handling, and governance.",
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
    rows = evaluate_cases(load_cases(article_root / "data" / "synthetic_formal_methods_cases.csv"))
    summary = summarize(rows)
    write_csv(article_root / "outputs" / "tables" / "formal_methods_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "formal_methods_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "formal_methods_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "formal_methods_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
