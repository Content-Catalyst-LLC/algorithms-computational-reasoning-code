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
class AttentionSystemConfig:
    article: str = "algorithms_in_media_platforms_and_attention_systems"
    high_attention_risk_threshold: float = 0.70
    low_governance_threshold: float = 0.65
    high_public_impact_threshold: float = 0.80


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


def platform_systems() -> list[dict[str, object]]:
    return [
        {"system_id": "short_video_recommendation", "engagement_pressure": 0.92, "transparency": 0.48, "contestability": 0.42, "moderation_readiness": 0.66, "creator_impact": 0.88, "public_knowledge_impact": 0.78, "user_control": 0.44, "governance": 0.54, "monitoring": 0.60},
        {"system_id": "public_news_search_ranking", "engagement_pressure": 0.54, "transparency": 0.72, "contestability": 0.66, "moderation_readiness": 0.70, "creator_impact": 0.62, "public_knowledge_impact": 0.92, "user_control": 0.70, "governance": 0.76, "monitoring": 0.78},
        {"system_id": "creator_monetization_classifier", "engagement_pressure": 0.70, "transparency": 0.50, "contestability": 0.46, "moderation_readiness": 0.58, "creator_impact": 0.94, "public_knowledge_impact": 0.52, "user_control": 0.50, "governance": 0.56, "monitoring": 0.62},
        {"system_id": "community_safety_review_queue", "engagement_pressure": 0.38, "transparency": 0.68, "contestability": 0.74, "moderation_readiness": 0.82, "creator_impact": 0.64, "public_knowledge_impact": 0.70, "user_control": 0.68, "governance": 0.78, "monitoring": 0.82},
    ]


def score_system(row: dict[str, object], config: AttentionSystemConfig) -> dict[str, object]:
    governance_readiness = mean([
        float(row["transparency"]),
        float(row["contestability"]),
        float(row["moderation_readiness"]),
        float(row["user_control"]),
        float(row["governance"]),
        float(row["monitoring"]),
    ])
    attention_risk = mean([
        float(row["engagement_pressure"]),
        float(row["creator_impact"]),
        float(row["public_knowledge_impact"]),
        1.0 - float(row["user_control"]),
        1.0 - float(row["contestability"]),
    ])
    platform_risk = attention_risk * (1.0 - governance_readiness)

    recommendation = "governed_use_with_monitoring"
    if attention_risk >= config.high_attention_risk_threshold and governance_readiness < config.low_governance_threshold:
        recommendation = "redesign_before_scaling"
    elif float(row["public_knowledge_impact"]) >= config.high_public_impact_threshold and governance_readiness < 0.75:
        recommendation = "independent_public_interest_review_required"
    elif governance_readiness < config.low_governance_threshold:
        recommendation = "governance_review_required"
    elif attention_risk >= config.high_attention_risk_threshold:
        recommendation = "use_with_strong_attention_guardrails"

    return {
        "system_id": row["system_id"],
        "engagement_pressure": round(float(row["engagement_pressure"]), 6),
        "transparency": round(float(row["transparency"]), 6),
        "contestability": round(float(row["contestability"]), 6),
        "moderation_readiness": round(float(row["moderation_readiness"]), 6),
        "creator_impact": round(float(row["creator_impact"]), 6),
        "public_knowledge_impact": round(float(row["public_knowledge_impact"]), 6),
        "user_control": round(float(row["user_control"]), 6),
        "governance": round(float(row["governance"]), 6),
        "monitoring": round(float(row["monitoring"]), 6),
        "governance_readiness_score": round(governance_readiness, 6),
        "attention_risk_score": round(attention_risk, 6),
        "platform_risk_score": round(platform_risk, 6),
        "recommendation": recommendation,
    }


def platform_governance_register() -> list[dict[str, str]]:
    return [
        {"control": "algorithm_inventory", "review_question": "Are ranking, recommendation, moderation, and ad systems recorded with owners and purposes?", "status": "required"},
        {"control": "objective_review", "review_question": "Are engagement, revenue, safety, quality, and public-value objectives documented?", "status": "required"},
        {"control": "attention_impact_assessment", "review_question": "Are user agency, creator effects, public-knowledge impact, and vulnerable users reviewed?", "status": "required"},
        {"control": "contestability_and_appeals", "review_question": "Can users and creators understand, challenge, and repair major decisions?", "status": "required"},
        {"control": "moderation_governance", "review_question": "Are classifier thresholds, human review, policy changes, and appeals documented?", "status": "required"},
        {"control": "monetization_review", "review_question": "Are ad targeting, demonetization, creator revenue, and incentive effects reviewed?", "status": "required"},
        {"control": "monitoring_and_stop_rules", "review_question": "Can harmful ranking or recommendation behavior be detected, paused, rolled back, or redesigned?", "status": "required"},
    ]


def main() -> None:
    config = AttentionSystemConfig()
    systems = platform_systems()
    audit = [score_system(row, config) for row in systems]
    controls = platform_governance_register()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "systems_reviewed": len(audit),
        "systems_requiring_redesign": sum(1 for row in audit if row["recommendation"] == "redesign_before_scaling"),
        "systems_requiring_public_interest_review": sum(1 for row in audit if row["recommendation"] == "independent_public_interest_review_required"),
        "systems_requiring_governance_review": sum(1 for row in audit if row["recommendation"] == "governance_review_required"),
        "mean_attention_risk_score": round(mean(float(row["attention_risk_score"]) for row in audit), 6),
        "mean_governance_readiness_score": round(mean(float(row["governance_readiness_score"]) for row in audit), 6),
        "mean_platform_risk_score": round(mean(float(row["platform_risk_score"]) for row in audit), 6),
        "governance_controls": len(controls),
        "interpretation": "Media platform governance should connect engagement pressure, creator impact, public knowledge, transparency, contestability, moderation, user control, monitoring, and stop authority.",
    }

    write_csv(TABLES / "platform_systems.csv", systems)
    write_csv(TABLES / "attention_system_audit.csv", audit)
    write_csv(TABLES / "platform_governance_register.csv", controls)
    write_csv(TABLES / "attention_system_summary.csv", [summary])

    write_json(JSON_DIR / "attention_system_config.json", asdict(config))
    write_json(JSON_DIR / "attention_system_audit.json", audit)
    write_json(JSON_DIR / "platform_governance_register.json", controls)
    write_json(JSON_DIR / "attention_system_summary.json", summary)

    print("Algorithms in media platforms and attention systems audit complete.")
    print(TABLES / "attention_system_summary.csv")


if __name__ == "__main__":
    main()
