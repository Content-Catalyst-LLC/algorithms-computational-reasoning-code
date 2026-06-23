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
class WorkplaceAlgorithmConfig:
    article: str = "algorithms_in_labor_management_and_organizational_systems"
    high_workplace_risk_threshold: float = 0.70
    low_governance_threshold: float = 0.65
    high_worker_impact_threshold: float = 0.80
    low_contestability_threshold: float = 0.60


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


def workplace_systems() -> list[dict[str, object]]:
    return [
        {"system_id": "applicant_screening_ranker", "worker_impact": 0.88, "managerial_impact": 0.72, "fairness_readiness": 0.58, "privacy_readiness": 0.66, "contestability": 0.52, "safety_readiness": 0.70, "human_review": 0.60, "monitoring": 0.58, "governance": 0.56},
        {"system_id": "shift_scheduling_optimizer", "worker_impact": 0.82, "managerial_impact": 0.80, "fairness_readiness": 0.62, "privacy_readiness": 0.72, "contestability": 0.64, "safety_readiness": 0.60, "human_review": 0.66, "monitoring": 0.68, "governance": 0.62},
        {"system_id": "warehouse_productivity_dashboard", "worker_impact": 0.90, "managerial_impact": 0.86, "fairness_readiness": 0.64, "privacy_readiness": 0.48, "contestability": 0.62, "safety_readiness": 0.52, "human_review": 0.50, "monitoring": 0.62, "governance": 0.50},
        {"system_id": "promotion_pipeline_model", "worker_impact": 0.72, "managerial_impact": 0.70, "fairness_readiness": 0.54, "privacy_readiness": 0.72, "contestability": 0.66, "safety_readiness": 0.72, "human_review": 0.70, "monitoring": 0.68, "governance": 0.66},
        {"system_id": "worker_safety_incident_model", "worker_impact": 0.74, "managerial_impact": 0.68, "fairness_readiness": 0.70, "privacy_readiness": 0.74, "contestability": 0.72, "safety_readiness": 0.82, "human_review": 0.78, "monitoring": 0.80, "governance": 0.76},
    ]


def score_system(row: dict[str, object], config: WorkplaceAlgorithmConfig) -> dict[str, object]:
    governance_readiness = mean([
        float(row["fairness_readiness"]),
        float(row["privacy_readiness"]),
        float(row["contestability"]),
        float(row["safety_readiness"]),
        float(row["human_review"]),
        float(row["monitoring"]),
        float(row["governance"]),
    ])
    impact_score = mean([
        float(row["worker_impact"]),
        float(row["managerial_impact"]),
    ])
    workplace_algorithm_risk = mean([
        impact_score,
        1.0 - float(row["fairness_readiness"]),
        1.0 - float(row["privacy_readiness"]),
        1.0 - float(row["contestability"]),
        1.0 - governance_readiness,
    ])

    recommendation = "governed_use_with_monitoring"
    if workplace_algorithm_risk >= config.high_workplace_risk_threshold and governance_readiness < config.low_governance_threshold:
        recommendation = "redesign_before_workplace_use"
    elif float(row["contestability"]) < config.low_contestability_threshold:
        recommendation = "contestability_and_appeal_review_required"
    elif float(row["privacy_readiness"]) < 0.60:
        recommendation = "workplace_privacy_review_required"
    elif float(row["fairness_readiness"]) < 0.60:
        recommendation = "workplace_equity_review_required"
    elif float(row["worker_impact"]) >= config.high_worker_impact_threshold and governance_readiness < 0.75:
        recommendation = "worker_impact_review_required"
    elif governance_readiness < config.low_governance_threshold:
        recommendation = "governance_review_required"

    return {
        "system_id": row["system_id"],
        "worker_impact": round(float(row["worker_impact"]), 6),
        "managerial_impact": round(float(row["managerial_impact"]), 6),
        "fairness_readiness": round(float(row["fairness_readiness"]), 6),
        "privacy_readiness": round(float(row["privacy_readiness"]), 6),
        "contestability": round(float(row["contestability"]), 6),
        "safety_readiness": round(float(row["safety_readiness"]), 6),
        "human_review": round(float(row["human_review"]), 6),
        "monitoring": round(float(row["monitoring"]), 6),
        "governance": round(float(row["governance"]), 6),
        "impact_score": round(impact_score, 6),
        "governance_readiness_score": round(governance_readiness, 6),
        "workplace_algorithm_risk_score": round(workplace_algorithm_risk, 6),
        "recommendation": recommendation,
    }


def workplace_governance_register() -> list[dict[str, str]]:
    return [
        {"control": "algorithm_inventory", "review_question": "Is the workplace algorithm recorded with owner, purpose, data, vendor, decision role, worker impact, and status?", "status": "required"},
        {"control": "labor_impact_assessment", "review_question": "Are effects on hiring, scheduling, pay, discipline, workload, safety, autonomy, and opportunity reviewed?", "status": "required"},
        {"control": "fairness_and_opportunity_review", "review_question": "Are subgroup outcomes, error rates, rating bias, access, promotion, and workload distribution reviewed?", "status": "required"},
        {"control": "privacy_and_surveillance_review", "review_question": "Are monitoring scope, data minimization, purpose limits, retention, and vendor access documented?", "status": "required"},
        {"control": "contestability_and_appeal", "review_question": "Can workers understand, correct, challenge, and appeal consequential outputs?", "status": "required"},
        {"control": "human_review_and_worker_voice", "review_question": "Are manager review, worker feedback, override authority, and collective governance channels defined?", "status": "required"},
        {"control": "monitoring_and_stop_rule", "review_question": "Are harms, bias, privacy incidents, safety problems, and metric distortion monitored with stop authority?", "status": "required"},
    ]


def main() -> None:
    config = WorkplaceAlgorithmConfig()
    systems = workplace_systems()
    audit = [score_system(row, config) for row in systems]
    controls = workplace_governance_register()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "systems_reviewed": len(audit),
        "systems_requiring_redesign": sum(1 for row in audit if row["recommendation"] == "redesign_before_workplace_use"),
        "systems_requiring_contestability_review": sum(1 for row in audit if row["recommendation"] == "contestability_and_appeal_review_required"),
        "systems_requiring_worker_impact_review": sum(1 for row in audit if row["recommendation"] == "worker_impact_review_required"),
        "systems_requiring_privacy_review": sum(1 for row in audit if row["recommendation"] == "workplace_privacy_review_required"),
        "systems_requiring_equity_review": sum(1 for row in audit if row["recommendation"] == "workplace_equity_review_required"),
        "mean_workplace_algorithm_risk_score": round(mean(float(row["workplace_algorithm_risk_score"]) for row in audit), 6),
        "mean_governance_readiness_score": round(mean(float(row["governance_readiness_score"]) for row in audit), 6),
        "mean_impact_score": round(mean(float(row["impact_score"]) for row in audit), 6),
        "governance_controls": len(controls),
        "interpretation": "Workplace algorithm governance should connect worker impact, managerial impact, fairness, privacy, contestability, safety, human review, worker voice, monitoring, audit trails, and stop authority.",
    }

    write_csv(TABLES / "workplace_systems.csv", systems)
    write_csv(TABLES / "workplace_algorithm_governance_audit.csv", audit)
    write_csv(TABLES / "workplace_governance_register.csv", controls)
    write_csv(TABLES / "workplace_algorithm_summary.csv", [summary])

    write_json(JSON_DIR / "workplace_algorithm_config.json", asdict(config))
    write_json(JSON_DIR / "workplace_algorithm_governance_audit.json", audit)
    write_json(JSON_DIR / "workplace_governance_register.json", controls)
    write_json(JSON_DIR / "workplace_algorithm_summary.json", summary)

    print("Algorithms in labor, management, and organizational systems audit complete.")
    print(TABLES / "workplace_algorithm_summary.csv")


if __name__ == "__main__":
    main()
