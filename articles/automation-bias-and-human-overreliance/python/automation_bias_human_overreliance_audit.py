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
class AutomationBiasConfig:
    article: str = "automation_bias_and_human_overreliance"
    high_acceptance_threshold: float = 0.85
    low_quality_threshold: float = 0.75
    calibration_gap_threshold: float = 0.15
    minimum_review_time: float = 2.0
    override_friction_threshold: float = 0.60


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


def oversight_cases() -> list[dict[str, object]]:
    return [
        {"case_id": "clinical_decision_support", "context": "health", "acceptance_rate": 0.88, "model_quality": 0.78, "uncertainty": 0.22, "review_time_minutes": 1.8, "override_friction": 0.54, "appeal_pathway": 1},
        {"case_id": "content_moderation_queue", "context": "platform", "acceptance_rate": 0.93, "model_quality": 0.71, "uncertainty": 0.29, "review_time_minutes": 0.7, "override_friction": 0.72, "appeal_pathway": 1},
        {"case_id": "fraud_alert_review", "context": "finance", "acceptance_rate": 0.81, "model_quality": 0.83, "uncertainty": 0.18, "review_time_minutes": 3.4, "override_friction": 0.31, "appeal_pathway": 1},
        {"case_id": "hiring_rank_review", "context": "employment", "acceptance_rate": 0.86, "model_quality": 0.68, "uncertainty": 0.33, "review_time_minutes": 1.2, "override_friction": 0.66, "appeal_pathway": 0},
        {"case_id": "public_benefits_screening", "context": "public_administration", "acceptance_rate": 0.90, "model_quality": 0.72, "uncertainty": 0.30, "review_time_minutes": 1.0, "override_friction": 0.64, "appeal_pathway": 0},
        {"case_id": "ai_code_assistant", "context": "software", "acceptance_rate": 0.76, "model_quality": 0.74, "uncertainty": 0.25, "review_time_minutes": 2.6, "override_friction": 0.20, "appeal_pathway": 1},
    ]


def audit_oversight(row: dict[str, object], config: AutomationBiasConfig) -> dict[str, object]:
    acceptance = float(row["acceptance_rate"])
    quality = float(row["model_quality"])
    uncertainty = float(row["uncertainty"])
    review_time = float(row["review_time_minutes"])
    override_friction = float(row["override_friction"])
    appeal_pathway = int(row["appeal_pathway"])

    calibration_gap = abs(acceptance - quality)
    overreliance_gap = max(0.0, acceptance - quality)
    high_acceptance = int(acceptance >= config.high_acceptance_threshold)
    low_quality = int(quality <= config.low_quality_threshold)
    high_calibration_gap = int(calibration_gap >= config.calibration_gap_threshold)
    low_review_time = int(review_time < config.minimum_review_time)
    high_override_friction = int(override_friction >= config.override_friction_threshold)
    weak_contestability = int(appeal_pathway == 0)

    review_time_deficit = max(0.0, (config.minimum_review_time - review_time) / config.minimum_review_time)

    bias_risk_score = mean([
        acceptance,
        overreliance_gap,
        uncertainty,
        review_time_deficit,
        override_friction,
        float(weak_contestability),
    ])

    status = "pass"
    if high_acceptance or high_calibration_gap or low_review_time or high_override_friction or weak_contestability:
        status = "review"
    if (high_acceptance and low_quality) or (high_calibration_gap and low_review_time) or (high_override_friction and weak_contestability):
        status = "escalate"

    return {
        "case_id": row["case_id"],
        "context": row["context"],
        "acceptance_rate": round(acceptance, 6),
        "model_quality": round(quality, 6),
        "uncertainty": round(uncertainty, 6),
        "review_time_minutes": round(review_time, 6),
        "review_time_deficit": round(review_time_deficit, 6),
        "override_friction": round(override_friction, 6),
        "appeal_pathway": appeal_pathway,
        "calibration_gap": round(calibration_gap, 6),
        "overreliance_gap": round(overreliance_gap, 6),
        "high_acceptance": high_acceptance,
        "low_quality": low_quality,
        "high_calibration_gap": high_calibration_gap,
        "low_review_time": low_review_time,
        "high_override_friction": high_override_friction,
        "weak_contestability": weak_contestability,
        "automation_bias_risk_score": round(bias_risk_score, 6),
        "status": status,
        "interpretation": "Automation-bias risk rises when acceptance exceeds model quality, uncertainty is high, review time is low, override friction is high, or contestability is weak.",
    }


def reliance_scenarios() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for acceptance, quality in [(0.65, 0.80), (0.80, 0.82), (0.90, 0.75), (0.95, 0.70)]:
        gap = max(0.0, acceptance - quality)
        rows.append({
            "acceptance_rate": acceptance,
            "model_quality": quality,
            "overreliance_gap": round(gap, 6),
            "calibration_error": round(abs(acceptance - quality), 6),
            "interpretation": "Trust is better calibrated when reliance behavior matches context-specific model quality.",
        })
    return rows


def governance_register() -> list[dict[str, str]]:
    return [
        {"item": "human_authority", "review_question": "Can the human meaningfully reject or modify the automated output?", "status": "required"},
        {"item": "review_time", "review_question": "Does the workflow provide enough time for independent review?", "status": "required"},
        {"item": "uncertainty_display", "review_question": "Are uncertainty, limits, and scope shown to users?", "status": "required"},
        {"item": "override_logging", "review_question": "Are overrides, disagreements, and reasons recorded?", "status": "required"},
        {"item": "appeal_pathway", "review_question": "Can affected people contest decisions influenced by automation?", "status": "required"},
        {"item": "training", "review_question": "Do users understand system limits and failure modes?", "status": "required"},
        {"item": "accountability", "review_question": "Who owns the final decision and correction process?", "status": "required"},
    ]


def main() -> None:
    config = AutomationBiasConfig()
    cases = oversight_cases()
    audits = [audit_oversight(row, config) for row in cases]
    scenarios = reliance_scenarios()
    governance = governance_register()
    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "cases_reviewed": len(audits),
        "cases_passed": sum(1 for row in audits if row["status"] == "pass"),
        "cases_requiring_review": sum(1 for row in audits if row["status"] == "review"),
        "cases_escalated": sum(1 for row in audits if row["status"] == "escalate"),
        "mean_acceptance_rate": round(mean(float(row["acceptance_rate"]) for row in audits), 6),
        "mean_overreliance_gap": round(mean(float(row["overreliance_gap"]) for row in audits), 6),
        "mean_automation_bias_risk_score": round(mean(float(row["automation_bias_risk_score"]) for row in audits), 6),
        "reliance_scenarios": len(scenarios),
        "governance_items": len(governance),
        "interpretation": "Human oversight should be monitored through acceptance, model quality, uncertainty, review time, override friction, contestability, and appeal pathways.",
    }

    write_csv(TABLES / "automation_oversight_cases.csv", cases)
    write_csv(TABLES / "automation_bias_overreliance_audit.csv", audits)
    write_csv(TABLES / "trust_calibration_scenarios.csv", scenarios)
    write_csv(TABLES / "automation_oversight_governance_register.csv", governance)
    write_csv(TABLES / "automation_bias_summary.csv", [summary])

    write_json(JSON_DIR / "automation_bias_config.json", asdict(config))
    write_json(JSON_DIR / "automation_bias_overreliance_audit.json", audits)
    write_json(JSON_DIR / "trust_calibration_scenarios.json", scenarios)
    write_json(JSON_DIR / "automation_oversight_governance_register.json", governance)
    write_json(JSON_DIR / "automation_bias_summary.json", summary)

    print("Automation bias and human overreliance audit complete.")
    print(TABLES / "automation_bias_summary.csv")


if __name__ == "__main__":
    main()
