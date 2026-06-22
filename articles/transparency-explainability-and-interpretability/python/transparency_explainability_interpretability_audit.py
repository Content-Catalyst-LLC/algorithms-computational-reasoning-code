from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv
import json
from datetime import datetime, timezone

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class ExplanationAuditConfig:
    article: str = "transparency_explainability_and_interpretability"
    low_explanation_quality_threshold: float = 0.65
    low_transparency_threshold: float = 0.70
    low_contestability_threshold: float = 0.65
    high_risk_threshold: float = 0.40


def timestamp_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = sorted({key for row in rows for key in row.keys()})
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def explanation_cases() -> list[dict[str, object]]:
    return [
        {"case_id": "benefits_eligibility_notice", "audience": "affected_person", "faithfulness": 0.70, "stability": 0.74, "understandability": 0.62, "actionability": 0.58, "uncertainty_communication": 0.46, "documentation_completeness": 0.68, "contestability": 0.55, "governance_readiness": 0.60, "stakes": 0.88},
        {"case_id": "model_debugging_report", "audience": "developer", "faithfulness": 0.82, "stability": 0.78, "understandability": 0.76, "actionability": 0.80, "uncertainty_communication": 0.72, "documentation_completeness": 0.84, "contestability": 0.70, "governance_readiness": 0.76, "stakes": 0.62},
        {"case_id": "public_model_card", "audience": "public", "faithfulness": 0.64, "stability": 0.66, "understandability": 0.82, "actionability": 0.50, "uncertainty_communication": 0.54, "documentation_completeness": 0.72, "contestability": 0.48, "governance_readiness": 0.58, "stakes": 0.74},
        {"case_id": "clinical_decision_support", "audience": "frontline_reviewer", "faithfulness": 0.76, "stability": 0.70, "understandability": 0.68, "actionability": 0.64, "uncertainty_communication": 0.62, "documentation_completeness": 0.78, "contestability": 0.66, "governance_readiness": 0.72, "stakes": 0.92},
    ]


def score_explanation(row: dict[str, object], config: ExplanationAuditConfig) -> dict[str, object]:
    explanation_quality = mean([
        float(row["faithfulness"]),
        float(row["stability"]),
        float(row["understandability"]),
        float(row["actionability"]),
        float(row["uncertainty_communication"]),
    ])
    transparency_capacity = mean([
        float(row["documentation_completeness"]),
        float(row["governance_readiness"]),
        float(row["uncertainty_communication"]),
    ])
    accountability_capacity = mean([
        explanation_quality,
        transparency_capacity,
        float(row["contestability"]),
        float(row["governance_readiness"]),
    ])
    explanation_risk = float(row["stakes"]) * (1.0 - accountability_capacity)

    status = "pass"
    if (
        explanation_quality < config.low_explanation_quality_threshold
        or transparency_capacity < config.low_transparency_threshold
        or float(row["contestability"]) < config.low_contestability_threshold
        or explanation_risk >= config.high_risk_threshold
    ):
        status = "review"
    if explanation_risk >= config.high_risk_threshold and float(row["contestability"]) < config.low_contestability_threshold:
        status = "escalate"

    return {
        "case_id": row["case_id"],
        "audience": row["audience"],
        "faithfulness": round(float(row["faithfulness"]), 6),
        "stability": round(float(row["stability"]), 6),
        "understandability": round(float(row["understandability"]), 6),
        "actionability": round(float(row["actionability"]), 6),
        "uncertainty_communication": round(float(row["uncertainty_communication"]), 6),
        "documentation_completeness": round(float(row["documentation_completeness"]), 6),
        "contestability": round(float(row["contestability"]), 6),
        "governance_readiness": round(float(row["governance_readiness"]), 6),
        "stakes": round(float(row["stakes"]), 6),
        "explanation_quality_score": round(explanation_quality, 6),
        "transparency_capacity_score": round(transparency_capacity, 6),
        "accountability_capacity_score": round(accountability_capacity, 6),
        "explanation_risk_score": round(explanation_risk, 6),
        "status": status,
    }


def governance_register() -> list[dict[str, str]]:
    return [
        {"item": "audience_definition", "review_question": "Who needs the explanation and what action must it support?", "status": "required"},
        {"item": "faithfulness_testing", "review_question": "Does the explanation accurately reflect system behavior?", "status": "required"},
        {"item": "uncertainty_communication", "review_question": "Does the explanation communicate confidence, limits, and unsupported use?", "status": "required"},
        {"item": "documentation", "review_question": "Are data, model, evaluation, limits, versions, and governance documented?", "status": "required"},
        {"item": "contestability", "review_question": "Can affected people challenge, correct, and appeal outcomes?", "status": "required"},
        {"item": "remediation", "review_question": "Do explanations connect to correction, remedy, and recurrence prevention?", "status": "required"},
    ]


def main() -> None:
    config = ExplanationAuditConfig()
    cases = explanation_cases()
    audits = [score_explanation(row, config) for row in cases]
    governance = governance_register()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "cases_reviewed": len(audits),
        "cases_passed": sum(1 for row in audits if row["status"] == "pass"),
        "cases_requiring_review": sum(1 for row in audits if row["status"] == "review"),
        "cases_escalated": sum(1 for row in audits if row["status"] == "escalate"),
        "mean_explanation_quality_score": round(mean(float(row["explanation_quality_score"]) for row in audits), 6),
        "mean_transparency_capacity_score": round(mean(float(row["transparency_capacity_score"]) for row in audits), 6),
        "mean_accountability_capacity_score": round(mean(float(row["accountability_capacity_score"]) for row in audits), 6),
        "mean_explanation_risk_score": round(mean(float(row["explanation_risk_score"]) for row in audits), 6),
        "governance_items": len(governance),
        "interpretation": "Explanation review should connect faithfulness, stability, understandability, actionability, uncertainty, documentation, contestability, and governance.",
    }

    write_csv(TABLES / "explanation_cases.csv", cases)
    write_csv(TABLES / "explanation_audit.csv", audits)
    write_csv(TABLES / "explanation_governance_register.csv", governance)
    write_csv(TABLES / "explanation_audit_summary.csv", [summary])

    write_json(JSON_DIR / "explanation_audit_config.json", asdict(config))
    write_json(JSON_DIR / "explanation_audit.json", audits)
    write_json(JSON_DIR / "explanation_governance_register.json", governance)
    write_json(JSON_DIR / "explanation_audit_summary.json", summary)

    print("Transparency, explainability, and interpretability audit complete.")
    print(TABLES / "explanation_audit_summary.csv")


if __name__ == "__main__":
    main()
