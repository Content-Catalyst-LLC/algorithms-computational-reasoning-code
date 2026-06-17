from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class AutomatedReasoningCase:
    case_name: str
    reasoning_context: str
    inference_claim: str
    formalization_clarity: float
    premise_quality: float
    rule_soundness: float
    inference_traceability: float
    proof_or_model_evidence: float
    satisfiability_handling: float
    counterexample_handling: float
    unknown_status_handling: float
    human_review_pathway: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def automated_reasoning_quality(case: AutomatedReasoningCase) -> float:
    return clamp(100.0 * (
        0.12 * case.formalization_clarity
        + 0.10 * case.premise_quality
        + 0.12 * case.rule_soundness
        + 0.12 * case.inference_traceability
        + 0.10 * case.proof_or_model_evidence
        + 0.08 * case.satisfiability_handling
        + 0.10 * case.counterexample_handling
        + 0.08 * case.unknown_status_handling
        + 0.08 * case.human_review_pathway
        + 0.10 * case.governance_readiness
    ))


def inference_overclaim_risk(case: AutomatedReasoningCase) -> float:
    weak_points = [
        1.0 - case.formalization_clarity,
        1.0 - case.premise_quality,
        1.0 - case.rule_soundness,
        1.0 - case.inference_traceability,
        1.0 - case.proof_or_model_evidence,
        1.0 - case.unknown_status_handling,
        1.0 - case.human_review_pathway,
        1.0 - case.governance_readiness,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 82 and risk <= 22:
        return "strong automated-reasoning posture with clear formal evidence and interpretation boundaries"
    if quality >= 68 and risk <= 38:
        return "usable automated-reasoning posture with review needs"
    if risk >= 55:
        return "high inference-overclaim risk; formalization or evidence boundaries may be unclear"
    return "partial automated-reasoning posture; strengthen premises, rules, traces, evidence, or governance"


def load_cases(path: Path) -> list[AutomatedReasoningCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            AutomatedReasoningCase(
                row["case_name"],
                row["reasoning_context"],
                row["inference_claim"],
                float(row["formalization_clarity"]),
                float(row["premise_quality"]),
                float(row["rule_soundness"]),
                float(row["inference_traceability"]),
                float(row["proof_or_model_evidence"]),
                float(row["satisfiability_handling"]),
                float(row["counterexample_handling"]),
                float(row["unknown_status_handling"]),
                float(row["human_review_pathway"]),
                float(row["governance_readiness"]),
            )
            for row in reader
        ]


def evaluate_cases(cases: list[AutomatedReasoningCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        quality = automated_reasoning_quality(case)
        risk = inference_overclaim_risk(case)
        rows.append({
            **asdict(case),
            "automated_reasoning_quality": round(quality, 3),
            "inference_overclaim_risk": round(risk, 3),
            "diagnostic": diagnose(quality, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_automated_reasoning_quality": round(mean(float(row["automated_reasoning_quality"]) for row in rows), 3),
        "average_inference_overclaim_risk": round(mean(float(row["inference_overclaim_risk"]) for row in rows), 3),
        "highest_quality_case": max(rows, key=lambda row: float(row["automated_reasoning_quality"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["inference_overclaim_risk"]))["case_name"],
        "interpretation": "Automated reasoning quality depends on formalization clarity, premise quality, rule soundness, traceability, proof or model evidence, satisfiability handling, counterexamples, unknown status, human review, and governance.",
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
    rows = evaluate_cases(load_cases(article_root / "data" / "synthetic_automated_reasoning_cases.csv"))
    summary = summarize(rows)
    write_csv(article_root / "outputs" / "tables" / "automated_reasoning_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "automated_reasoning_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "automated_reasoning_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "automated_reasoning_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
