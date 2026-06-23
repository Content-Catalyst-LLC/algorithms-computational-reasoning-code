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
class LearningSystemConfig:
    article: str = "algorithms_in_education_and_learning_systems"
    high_learning_risk_threshold: float = 0.70
    low_governance_threshold: float = 0.65
    high_learner_impact_threshold: float = 0.80
    low_pedagogical_validity_threshold: float = 0.60


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


def learning_systems() -> list[dict[str, object]]:
    return [
        {"system_id": "adaptive_math_learning_pathway", "learner_impact": 0.78, "instructional_impact": 0.86, "equity_readiness": 0.62, "privacy_readiness": 0.72, "pedagogical_validity": 0.70, "human_review": 0.66, "accessibility_readiness": 0.68, "monitoring": 0.64, "governance": 0.62},
        {"system_id": "student_early_warning_dashboard", "learner_impact": 0.90, "instructional_impact": 0.72, "equity_readiness": 0.56, "privacy_readiness": 0.60, "pedagogical_validity": 0.64, "human_review": 0.58, "accessibility_readiness": 0.62, "monitoring": 0.60, "governance": 0.58},
        {"system_id": "automated_essay_scoring", "learner_impact": 0.84, "instructional_impact": 0.68, "equity_readiness": 0.54, "privacy_readiness": 0.70, "pedagogical_validity": 0.52, "human_review": 0.50, "accessibility_readiness": 0.60, "monitoring": 0.58, "governance": 0.56},
        {"system_id": "course_pathway_recommender", "learner_impact": 0.70, "instructional_impact": 0.62, "equity_readiness": 0.55, "privacy_readiness": 0.72, "pedagogical_validity": 0.68, "human_review": 0.70, "accessibility_readiness": 0.66, "monitoring": 0.68, "governance": 0.66},
        {"system_id": "accessible_course_recommender", "learner_impact": 0.62, "instructional_impact": 0.58, "equity_readiness": 0.74, "privacy_readiness": 0.78, "pedagogical_validity": 0.76, "human_review": 0.72, "accessibility_readiness": 0.82, "monitoring": 0.76, "governance": 0.74},
    ]


def score_system(row: dict[str, object], config: LearningSystemConfig) -> dict[str, object]:
    governance_readiness = mean([
        float(row["equity_readiness"]),
        float(row["privacy_readiness"]),
        float(row["pedagogical_validity"]),
        float(row["human_review"]),
        float(row["accessibility_readiness"]),
        float(row["monitoring"]),
        float(row["governance"]),
    ])
    impact_score = mean([
        float(row["learner_impact"]),
        float(row["instructional_impact"]),
    ])
    learning_system_risk = mean([
        impact_score,
        1.0 - float(row["equity_readiness"]),
        1.0 - float(row["pedagogical_validity"]),
        1.0 - governance_readiness,
    ])

    recommendation = "governed_use_with_monitoring"
    if learning_system_risk >= config.high_learning_risk_threshold and governance_readiness < config.low_governance_threshold:
        recommendation = "redesign_before_educational_use"
    elif float(row["pedagogical_validity"]) < config.low_pedagogical_validity_threshold:
        recommendation = "pedagogical_validity_review_required"
    elif float(row["learner_impact"]) >= config.high_learner_impact_threshold and governance_readiness < 0.75:
        recommendation = "student_impact_review_required"
    elif float(row["equity_readiness"]) < 0.60:
        recommendation = "educational_equity_review_required"
    elif float(row["privacy_readiness"]) < 0.65:
        recommendation = "student_privacy_review_required"
    elif governance_readiness < config.low_governance_threshold:
        recommendation = "governance_review_required"

    return {
        "system_id": row["system_id"],
        "learner_impact": round(float(row["learner_impact"]), 6),
        "instructional_impact": round(float(row["instructional_impact"]), 6),
        "equity_readiness": round(float(row["equity_readiness"]), 6),
        "privacy_readiness": round(float(row["privacy_readiness"]), 6),
        "pedagogical_validity": round(float(row["pedagogical_validity"]), 6),
        "human_review": round(float(row["human_review"]), 6),
        "accessibility_readiness": round(float(row["accessibility_readiness"]), 6),
        "monitoring": round(float(row["monitoring"]), 6),
        "governance": round(float(row["governance"]), 6),
        "impact_score": round(impact_score, 6),
        "governance_readiness_score": round(governance_readiness, 6),
        "learning_system_risk_score": round(learning_system_risk, 6),
        "recommendation": recommendation,
    }


def learning_governance_register() -> list[dict[str, str]]:
    return [
        {"control": "algorithm_inventory", "review_question": "Is the learning algorithm recorded with owner, purpose, data, decision role, learner impact, and status?", "status": "required"},
        {"control": "pedagogical_review", "review_question": "Does the system support meaningful learning goals, teacher judgment, and educational purpose?", "status": "required"},
        {"control": "equity_review", "review_question": "Are access barriers, subgroup errors, tracking risks, and opportunity effects reviewed?", "status": "required"},
        {"control": "student_privacy_review", "review_question": "Are data collection, secondary use, retention, vendor access, and security governed?", "status": "required"},
        {"control": "accessibility_review", "review_question": "Is the system usable and adaptable for disabled, multilingual, neurodivergent, and diverse learners?", "status": "required"},
        {"control": "human_review_and_contestability", "review_question": "Can students and educators understand, challenge, correct, and override consequential outputs?", "status": "required"},
        {"control": "monitoring_and_stop_rule", "review_question": "Are outcomes, burden, bias, privacy incidents, and educational harms monitored with stop authority?", "status": "required"},
    ]


def main() -> None:
    config = LearningSystemConfig()
    systems = learning_systems()
    audit = [score_system(row, config) for row in systems]
    controls = learning_governance_register()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "systems_reviewed": len(audit),
        "systems_requiring_redesign": sum(1 for row in audit if row["recommendation"] == "redesign_before_educational_use"),
        "systems_requiring_pedagogical_review": sum(1 for row in audit if row["recommendation"] == "pedagogical_validity_review_required"),
        "systems_requiring_student_impact_review": sum(1 for row in audit if row["recommendation"] == "student_impact_review_required"),
        "systems_requiring_equity_review": sum(1 for row in audit if row["recommendation"] == "educational_equity_review_required"),
        "systems_requiring_privacy_review": sum(1 for row in audit if row["recommendation"] == "student_privacy_review_required"),
        "mean_learning_system_risk_score": round(mean(float(row["learning_system_risk_score"]) for row in audit), 6),
        "mean_governance_readiness_score": round(mean(float(row["governance_readiness_score"]) for row in audit), 6),
        "mean_impact_score": round(mean(float(row["impact_score"]) for row in audit), 6),
        "governance_controls": len(controls),
        "interpretation": "Education algorithm governance should connect learner impact, instructional impact, equity readiness, privacy readiness, pedagogical validity, accessibility, teacher judgment, monitoring, contestability, and stop authority.",
    }

    write_csv(TABLES / "learning_systems.csv", systems)
    write_csv(TABLES / "learning_system_governance_audit.csv", audit)
    write_csv(TABLES / "learning_governance_register.csv", controls)
    write_csv(TABLES / "learning_system_summary.csv", [summary])

    write_json(JSON_DIR / "learning_system_config.json", asdict(config))
    write_json(JSON_DIR / "learning_system_governance_audit.json", audit)
    write_json(JSON_DIR / "learning_governance_register.json", controls)
    write_json(JSON_DIR / "learning_system_summary.json", summary)

    print("Algorithms in education and learning systems audit complete.")
    print(TABLES / "learning_system_summary.csv")


if __name__ == "__main__":
    main()
