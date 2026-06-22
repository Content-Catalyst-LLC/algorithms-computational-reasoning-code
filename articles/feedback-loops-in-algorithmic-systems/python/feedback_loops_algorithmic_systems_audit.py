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
class FeedbackAuditConfig:
    article: str = "feedback_loops_in_algorithmic_systems"
    amplification_threshold: float = 0.70
    exposure_concentration_threshold: float = 0.65
    drift_threshold: float = 0.25
    recursive_data_threshold: float = 0.30


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


def feedback_cases() -> list[dict[str, object]]:
    return [
        {"case_id": "recommendation_feed", "system": "content_recommendation", "feedback_path": "exposure_to_clicks_to_future_exposure", "amplification": 0.82, "exposure_concentration": 0.76, "intervention_influence": 0.44, "drift": 0.28, "recursive_data": 0.31},
        {"case_id": "search_ranking", "system": "search", "feedback_path": "rank_to_clicks_to_rank", "amplification": 0.74, "exposure_concentration": 0.71, "intervention_influence": 0.35, "drift": 0.20, "recursive_data": 0.18},
        {"case_id": "risk_scoring", "system": "institutional_decision_support", "feedback_path": "score_to_intervention_to_recorded_outcome", "amplification": 0.66, "exposure_concentration": 0.40, "intervention_influence": 0.81, "drift": 0.32, "recursive_data": 0.22},
        {"case_id": "fraud_detection", "system": "adversarial_detection", "feedback_path": "detection_to_evasion_to_new_patterns", "amplification": 0.58, "exposure_concentration": 0.30, "intervention_influence": 0.70, "drift": 0.46, "recursive_data": 0.12},
        {"case_id": "generative_ai_data_loop", "system": "generative_model", "feedback_path": "model_output_to_public_data_to_future_training", "amplification": 0.69, "exposure_concentration": 0.55, "intervention_influence": 0.42, "drift": 0.34, "recursive_data": 0.62},
        {"case_id": "workplace_dashboard", "system": "institutional_metrics", "feedback_path": "metric_to_behavior_to_future_metric", "amplification": 0.72, "exposure_concentration": 0.58, "intervention_influence": 0.62, "drift": 0.30, "recursive_data": 0.26},
    ]


def audit_feedback(row: dict[str, object], config: FeedbackAuditConfig) -> dict[str, object]:
    amplification = float(row["amplification"])
    concentration = float(row["exposure_concentration"])
    intervention = float(row["intervention_influence"])
    drift = float(row["drift"])
    recursive = float(row["recursive_data"])

    high_amplification = int(amplification >= config.amplification_threshold)
    high_concentration = int(concentration >= config.exposure_concentration_threshold)
    high_drift = int(drift >= config.drift_threshold)
    high_recursive = int(recursive >= config.recursive_data_threshold)

    feedback_risk = mean([amplification, concentration, intervention, drift, recursive])
    status = "pass"
    if high_amplification or high_concentration or high_drift or high_recursive:
        status = "review"
    if (high_amplification and high_concentration) or (high_drift and high_recursive):
        status = "escalate"

    return {
        "case_id": row["case_id"],
        "system": row["system"],
        "feedback_path": row["feedback_path"],
        "amplification": round(amplification, 6),
        "exposure_concentration": round(concentration, 6),
        "intervention_influence": round(intervention, 6),
        "drift": round(drift, 6),
        "recursive_data": round(recursive, 6),
        "high_amplification": high_amplification,
        "high_concentration": high_concentration,
        "high_drift": high_drift,
        "high_recursive_data": high_recursive,
        "feedback_risk_score": round(feedback_risk, 6),
        "status": status,
        "interpretation": "Feedback risk rises when outputs amplify exposure, influence interventions, shift distributions, or enter future training data.",
    }


def drift_scenarios() -> list[dict[str, object]]:
    rows = []
    for distance in [0.05, 0.15, 0.25, 0.35, 0.50]:
        rows.append({
            "distribution_distance": distance,
            "review_trigger": int(distance > 0.25),
            "interpretation": "Distribution shift should trigger review when it exceeds the operational drift threshold.",
        })
    return rows


def feedback_governance_register() -> list[dict[str, str]]:
    return [
        {"item": "feedback_map", "review_question": "How do outputs influence future inputs and records?", "status": "required"},
        {"item": "exposure_logging", "review_question": "Who or what was shown, ranked, recommended, or hidden?", "status": "required"},
        {"item": "intervention_tracking", "review_question": "What actions followed the prediction or score?", "status": "required"},
        {"item": "drift_monitoring", "review_question": "How are data distributions changing after deployment?", "status": "required"},
        {"item": "recursive_data_labeling", "review_question": "Are model-mediated or synthetic data labeled and bounded?", "status": "required"},
        {"item": "correction_pathway", "review_question": "How are feedback harms appealed, corrected, and prevented?", "status": "required"},
        {"item": "update_boundary", "review_question": "When should feedback-shaped data be excluded from retraining?", "status": "required"},
    ]


def main() -> None:
    config = FeedbackAuditConfig()
    cases = feedback_cases()
    audits = [audit_feedback(row, config) for row in cases]
    drift = drift_scenarios()
    governance = feedback_governance_register()
    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "feedback_cases_reviewed": len(audits),
        "cases_passed": sum(1 for row in audits if row["status"] == "pass"),
        "cases_requiring_review": sum(1 for row in audits if row["status"] == "review"),
        "cases_escalated": sum(1 for row in audits if row["status"] == "escalate"),
        "mean_feedback_risk_score": round(mean(float(row["feedback_risk_score"]) for row in audits), 6),
        "mean_drift": round(mean(float(row["drift"]) for row in audits), 6),
        "drift_scenarios": len(drift),
        "governance_items": len(governance),
        "interpretation": "Feedback loops should be reviewed through exposure, amplification, intervention influence, drift, recursive data, correction pathways, and update boundaries.",
    }

    write_csv(TABLES / "feedback_loop_cases.csv", cases)
    write_csv(TABLES / "feedback_loop_audit.csv", audits)
    write_csv(TABLES / "feedback_drift_scenarios.csv", drift)
    write_csv(TABLES / "feedback_governance_register.csv", governance)
    write_csv(TABLES / "feedback_audit_summary.csv", [summary])

    write_json(JSON_DIR / "feedback_audit_config.json", asdict(config))
    write_json(JSON_DIR / "feedback_loop_audit.json", audits)
    write_json(JSON_DIR / "feedback_drift_scenarios.json", drift)
    write_json(JSON_DIR / "feedback_governance_register.json", governance)
    write_json(JSON_DIR / "feedback_audit_summary.json", summary)

    print("Algorithmic feedback-loop audit complete.")
    print(TABLES / "feedback_audit_summary.csv")


if __name__ == "__main__":
    main()
