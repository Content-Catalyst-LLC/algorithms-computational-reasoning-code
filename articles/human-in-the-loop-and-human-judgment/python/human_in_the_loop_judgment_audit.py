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
class HumanReviewConfig:
    article: str = "human_in_the_loop_and_human_judgment"
    low_review_capacity_threshold: float = 0.70
    high_reliance_threshold: float = 0.90
    low_override_floor: float = 0.02
    high_review_risk_threshold: float = 0.30


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


def review_contexts() -> list[dict[str, object]]:
    return [
        {"context_id": "benefits_case_review", "time": 0.56, "information": 0.62, "authority": 0.58, "training": 0.60, "protection": 0.48, "accepted_recommendations": 920, "total_recommendations": 1000, "overrides": 18, "reviewed_cases": 1000, "escalation_capacity": 0.54, "contestability": 0.52, "governance": 0.60, "stakes": 0.88},
        {"context_id": "clinical_decision_support", "time": 0.74, "information": 0.80, "authority": 0.78, "training": 0.76, "protection": 0.72, "accepted_recommendations": 690, "total_recommendations": 1000, "overrides": 115, "reviewed_cases": 1000, "escalation_capacity": 0.80, "contestability": 0.70, "governance": 0.78, "stakes": 0.96},
        {"context_id": "content_moderation_review", "time": 0.42, "information": 0.50, "authority": 0.46, "training": 0.58, "protection": 0.44, "accepted_recommendations": 960, "total_recommendations": 1000, "overrides": 9, "reviewed_cases": 1000, "escalation_capacity": 0.48, "contestability": 0.46, "governance": 0.52, "stakes": 0.70},
        {"context_id": "fraud_alert_investigation", "time": 0.68, "information": 0.72, "authority": 0.70, "training": 0.66, "protection": 0.64, "accepted_recommendations": 760, "total_recommendations": 1000, "overrides": 74, "reviewed_cases": 1000, "escalation_capacity": 0.72, "contestability": 0.62, "governance": 0.70, "stakes": 0.82},
    ]


def score_review_context(row: dict[str, object], config: HumanReviewConfig) -> dict[str, object]:
    review_capacity = mean([
        float(row["time"]),
        float(row["information"]),
        float(row["authority"]),
        float(row["training"]),
        float(row["protection"]),
    ])
    total_recommendations = float(row["total_recommendations"])
    reviewed_cases = float(row["reviewed_cases"])
    reliance = 0.0 if total_recommendations == 0 else float(row["accepted_recommendations"]) / total_recommendations
    override_rate = 0.0 if reviewed_cases == 0 else float(row["overrides"]) / reviewed_cases
    judgment_capacity = mean([
        review_capacity,
        float(row["escalation_capacity"]),
        float(row["contestability"]),
        float(row["governance"]),
    ])
    review_risk = float(row["stakes"]) * (1.0 - judgment_capacity)

    status = "pass"
    if (
        review_capacity < config.low_review_capacity_threshold
        or reliance >= config.high_reliance_threshold
        or override_rate <= config.low_override_floor
        or review_risk >= config.high_review_risk_threshold
    ):
        status = "review"
    if review_risk >= config.high_review_risk_threshold and reliance >= config.high_reliance_threshold:
        status = "escalate"

    return {
        "context_id": row["context_id"],
        "review_capacity_score": round(review_capacity, 6),
        "reliance_score": round(reliance, 6),
        "override_rate": round(override_rate, 6),
        "escalation_capacity": round(float(row["escalation_capacity"]), 6),
        "contestability": round(float(row["contestability"]), 6),
        "governance": round(float(row["governance"]), 6),
        "stakes": round(float(row["stakes"]), 6),
        "judgment_capacity_score": round(judgment_capacity, 6),
        "review_risk_score": round(review_risk, 6),
        "status": status,
    }


def governance_register() -> list[dict[str, str]]:
    return [
        {"item": "review_authority", "review_question": "Can the human reviewer override, pause, or escalate the system?", "status": "required"},
        {"item": "evidence_access", "review_question": "Can the reviewer see inputs, reasons, uncertainty, and case context?", "status": "required"},
        {"item": "workload_design", "review_question": "Does the reviewer have enough time for meaningful judgment?", "status": "required"},
        {"item": "override_logging", "review_question": "Are overrides documented, reviewed, and used for system learning?", "status": "required"},
        {"item": "contestability", "review_question": "Can affected people challenge and correct outcomes?", "status": "required"},
        {"item": "institutional_ownership", "review_question": "Who is responsible for review conditions and remediation?", "status": "required"},
    ]


def main() -> None:
    config = HumanReviewConfig()
    contexts = review_contexts()
    audit = [score_review_context(row, config) for row in contexts]
    governance = governance_register()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "contexts_reviewed": len(audit),
        "contexts_passed": sum(1 for row in audit if row["status"] == "pass"),
        "contexts_requiring_review": sum(1 for row in audit if row["status"] == "review"),
        "contexts_escalated": sum(1 for row in audit if row["status"] == "escalate"),
        "mean_review_capacity_score": round(mean(float(row["review_capacity_score"]) for row in audit), 6),
        "mean_reliance_score": round(mean(float(row["reliance_score"]) for row in audit), 6),
        "mean_override_rate": round(mean(float(row["override_rate"]) for row in audit), 6),
        "mean_judgment_capacity_score": round(mean(float(row["judgment_capacity_score"]) for row in audit), 6),
        "mean_review_risk_score": round(mean(float(row["review_risk_score"]) for row in audit), 6),
        "governance_items": len(governance),
        "interpretation": "Human-in-the-loop review should connect time, information, authority, training, protection, reliance, overrides, escalation, contestability, and governance.",
    }

    write_csv(TABLES / "human_review_contexts.csv", contexts)
    write_csv(TABLES / "human_review_audit.csv", audit)
    write_csv(TABLES / "human_review_governance_register.csv", governance)
    write_csv(TABLES / "human_review_audit_summary.csv", [summary])

    write_json(JSON_DIR / "human_review_config.json", asdict(config))
    write_json(JSON_DIR / "human_review_audit.json", audit)
    write_json(JSON_DIR / "human_review_governance_register.json", governance)
    write_json(JSON_DIR / "human_review_audit_summary.json", summary)

    print("Human-in-the-loop and human judgment audit complete.")
    print(TABLES / "human_review_audit_summary.csv")


if __name__ == "__main__":
    main()
