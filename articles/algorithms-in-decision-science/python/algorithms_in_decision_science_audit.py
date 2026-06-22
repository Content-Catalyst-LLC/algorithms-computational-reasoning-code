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
class DecisionScienceConfig:
    article: str = "algorithms_in_decision_science"
    action_threshold: float = 0.70
    low_governance_threshold: float = 0.65
    high_stakes_threshold: float = 0.80


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


def candidate_decisions() -> list[dict[str, object]]:
    return [
        {"decision_id": "clinical_triage_review", "predicted_probability": 0.82, "benefit_if_act": 0.88, "cost_if_act": 0.30, "loss_if_miss": 0.92, "calibration": 0.78, "uncertainty_communication": 0.74, "human_review": 0.82, "contestability": 0.70, "governance": 0.76, "stakes": 0.94},
        {"decision_id": "routine_document_routing", "predicted_probability": 0.76, "benefit_if_act": 0.55, "cost_if_act": 0.10, "loss_if_miss": 0.22, "calibration": 0.86, "uncertainty_communication": 0.72, "human_review": 0.62, "contestability": 0.64, "governance": 0.70, "stakes": 0.28},
        {"decision_id": "automated_benefits_denial", "predicted_probability": 0.72, "benefit_if_act": 0.40, "cost_if_act": 0.86, "loss_if_miss": 0.20, "calibration": 0.52, "uncertainty_communication": 0.38, "human_review": 0.40, "contestability": 0.36, "governance": 0.42, "stakes": 0.96},
        {"decision_id": "infrastructure_inspection_priority", "predicted_probability": 0.68, "benefit_if_act": 0.82, "cost_if_act": 0.34, "loss_if_miss": 0.88, "calibration": 0.80, "uncertainty_communication": 0.78, "human_review": 0.72, "contestability": 0.58, "governance": 0.74, "stakes": 0.82},
    ]


def score_decision(row: dict[str, object], config: DecisionScienceConfig) -> dict[str, object]:
    p = float(row["predicted_probability"])
    benefit = float(row["benefit_if_act"])
    cost = float(row["cost_if_act"])
    loss_if_miss = float(row["loss_if_miss"])
    expected_value = p * benefit - cost
    expected_loss_if_no_action = p * loss_if_miss

    decision_support_readiness = mean([
        float(row["calibration"]),
        float(row["uncertainty_communication"]),
        float(row["human_review"]),
        float(row["contestability"]),
        float(row["governance"]),
    ])

    threshold_action = p >= config.action_threshold
    recommendation = "monitor_or_defer"
    if threshold_action and decision_support_readiness >= config.low_governance_threshold:
        recommendation = "support_action_with_review"
    if threshold_action and float(row["stakes"]) >= config.high_stakes_threshold:
        recommendation = "escalate_to_human_review"
    if threshold_action and decision_support_readiness < config.low_governance_threshold:
        recommendation = "do_not_automate_action"
    if not threshold_action and expected_loss_if_no_action > expected_value:
        recommendation = "review_despite_below_threshold"

    return {
        "decision_id": row["decision_id"],
        "predicted_probability": round(p, 6),
        "expected_value_of_action": round(expected_value, 6),
        "expected_loss_if_no_action": round(expected_loss_if_no_action, 6),
        "threshold_action": threshold_action,
        "decision_support_readiness_score": round(decision_support_readiness, 6),
        "stakes": round(float(row["stakes"]), 6),
        "recommendation": recommendation,
    }


def decision_governance_register() -> list[dict[str, str]]:
    return [
        {"control": "forecast_documentation", "review_question": "Is the forecast calibrated, contextualized, and uncertainty-aware?", "status": "required"},
        {"control": "threshold_rationale", "review_question": "Is the action threshold justified by costs, harms, benefits, and rights?", "status": "required"},
        {"control": "human_review_protocol", "review_question": "Can reviewers understand, challenge, override, and document decisions?", "status": "required"},
        {"control": "contestability_pathway", "review_question": "Can affected people understand, challenge, and correct outcomes?", "status": "required"},
        {"control": "monitoring_and_feedback", "review_question": "Are outcomes, reliance, drift, and feedback effects monitored?", "status": "required"},
        {"control": "stop_rule", "review_question": "Can the institution pause, rollback, or retire the decision system?", "status": "required"},
    ]


def main() -> None:
    config = DecisionScienceConfig()
    decisions = candidate_decisions()
    audit = [score_decision(row, config) for row in decisions]
    controls = decision_governance_register()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "decisions_reviewed": len(audit),
        "decisions_supporting_action": sum(1 for row in audit if row["recommendation"] == "support_action_with_review"),
        "decisions_escalated": sum(1 for row in audit if row["recommendation"] == "escalate_to_human_review"),
        "decisions_not_automated": sum(1 for row in audit if row["recommendation"] == "do_not_automate_action"),
        "mean_decision_support_readiness_score": round(mean(float(row["decision_support_readiness_score"]) for row in audit), 6),
        "mean_expected_value_of_action": round(mean(float(row["expected_value_of_action"]) for row in audit), 6),
        "mean_expected_loss_if_no_action": round(mean(float(row["expected_loss_if_no_action"]) for row in audit), 6),
        "governance_controls": len(controls),
        "interpretation": "Algorithmic decision support should connect forecasts, thresholds, uncertainty, review, contestability, monitoring, and stop authority.",
    }

    write_csv(TABLES / "candidate_decisions.csv", decisions)
    write_csv(TABLES / "decision_science_audit.csv", audit)
    write_csv(TABLES / "decision_governance_register.csv", controls)
    write_csv(TABLES / "decision_science_summary.csv", [summary])

    write_json(JSON_DIR / "decision_science_config.json", asdict(config))
    write_json(JSON_DIR / "decision_science_audit.json", audit)
    write_json(JSON_DIR / "decision_governance_register.json", controls)
    write_json(JSON_DIR / "decision_science_summary.json", summary)

    print("Algorithms in decision science audit complete.")
    print(TABLES / "decision_science_summary.csv")


if __name__ == "__main__":
    main()
