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
class HealthAlgorithmConfig:
    article: str = "algorithms_in_health_care_and_public_health"
    high_health_risk_threshold: float = 0.70
    low_governance_threshold: float = 0.65
    high_patient_impact_threshold: float = 0.80
    high_population_impact_threshold: float = 0.80


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


def health_systems() -> list[dict[str, object]]:
    return [
        {"system_id": "sepsis_alert_model", "patient_impact": 0.92, "population_impact": 0.54, "clinical_validation": 0.70, "equity_readiness": 0.58, "privacy_readiness": 0.72, "human_review": 0.66, "workflow_integration": 0.62, "monitoring": 0.64, "governance": 0.60},
        {"system_id": "radiology_triage_classifier", "patient_impact": 0.88, "population_impact": 0.42, "clinical_validation": 0.78, "equity_readiness": 0.62, "privacy_readiness": 0.76, "human_review": 0.74, "workflow_integration": 0.68, "monitoring": 0.70, "governance": 0.68},
        {"system_id": "public_health_outbreak_detector", "patient_impact": 0.48, "population_impact": 0.92, "clinical_validation": 0.66, "equity_readiness": 0.64, "privacy_readiness": 0.56, "human_review": 0.72, "workflow_integration": 0.74, "monitoring": 0.82, "governance": 0.70},
        {"system_id": "care_management_risk_list", "patient_impact": 0.78, "population_impact": 0.76, "clinical_validation": 0.62, "equity_readiness": 0.50, "privacy_readiness": 0.70, "human_review": 0.60, "workflow_integration": 0.58, "monitoring": 0.54, "governance": 0.56},
    ]


def score_system(row: dict[str, object], config: HealthAlgorithmConfig) -> dict[str, object]:
    governance_readiness = mean([
        float(row["clinical_validation"]),
        float(row["equity_readiness"]),
        float(row["privacy_readiness"]),
        float(row["human_review"]),
        float(row["workflow_integration"]),
        float(row["monitoring"]),
        float(row["governance"]),
    ])
    impact = mean([
        float(row["patient_impact"]),
        float(row["population_impact"]),
    ])
    health_algorithm_risk = mean([
        impact,
        1.0 - float(row["clinical_validation"]),
        1.0 - float(row["equity_readiness"]),
        1.0 - governance_readiness,
    ])

    recommendation = "governed_use_with_monitoring"
    if health_algorithm_risk >= config.high_health_risk_threshold and governance_readiness < config.low_governance_threshold:
        recommendation = "redesign_before_clinical_or_public_health_use"
    elif float(row["patient_impact"]) >= config.high_patient_impact_threshold and governance_readiness < 0.75:
        recommendation = "clinical_safety_review_required"
    elif float(row["population_impact"]) >= config.high_population_impact_threshold and governance_readiness < 0.75:
        recommendation = "public_health_governance_review_required"
    elif float(row["equity_readiness"]) < 0.60:
        recommendation = "health_equity_review_required"
    elif governance_readiness < config.low_governance_threshold:
        recommendation = "governance_review_required"

    return {
        "system_id": row["system_id"],
        "patient_impact": round(float(row["patient_impact"]), 6),
        "population_impact": round(float(row["population_impact"]), 6),
        "clinical_validation": round(float(row["clinical_validation"]), 6),
        "equity_readiness": round(float(row["equity_readiness"]), 6),
        "privacy_readiness": round(float(row["privacy_readiness"]), 6),
        "human_review": round(float(row["human_review"]), 6),
        "workflow_integration": round(float(row["workflow_integration"]), 6),
        "monitoring": round(float(row["monitoring"]), 6),
        "governance": round(float(row["governance"]), 6),
        "impact_score": round(impact, 6),
        "governance_readiness_score": round(governance_readiness, 6),
        "health_algorithm_risk_score": round(health_algorithm_risk, 6),
        "recommendation": recommendation,
    }


def health_governance_register() -> list[dict[str, str]]:
    return [
        {"control": "algorithm_inventory", "review_question": "Is the health algorithm recorded with owner, purpose, data, setting, and decision role?", "status": "required"},
        {"control": "clinical_validation", "review_question": "Has performance been validated for the intended population, setting, workflow, and use?", "status": "required"},
        {"control": "equity_review", "review_question": "Are subgroup performance, missingness, access barriers, and proxy labels reviewed?", "status": "required"},
        {"control": "privacy_and_security_review", "review_question": "Are data minimization, access controls, security, and secondary-use limits documented?", "status": "required"},
        {"control": "human_review_protocol", "review_question": "Are clinician review, override authority, escalation, and accountability defined?", "status": "required"},
        {"control": "monitoring_and_drift_review", "review_question": "Are outcomes, errors, alert fatigue, drift, overrides, and harms monitored?", "status": "required"},
        {"control": "stop_rule", "review_question": "Can the system be paused, limited, rolled back, or retired when unsafe?", "status": "required"},
    ]


def main() -> None:
    config = HealthAlgorithmConfig()
    systems = health_systems()
    audit = [score_system(row, config) for row in systems]
    controls = health_governance_register()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "systems_reviewed": len(audit),
        "systems_requiring_redesign": sum(1 for row in audit if row["recommendation"] == "redesign_before_clinical_or_public_health_use"),
        "systems_requiring_clinical_safety_review": sum(1 for row in audit if row["recommendation"] == "clinical_safety_review_required"),
        "systems_requiring_public_health_review": sum(1 for row in audit if row["recommendation"] == "public_health_governance_review_required"),
        "systems_requiring_equity_review": sum(1 for row in audit if row["recommendation"] == "health_equity_review_required"),
        "mean_health_algorithm_risk_score": round(mean(float(row["health_algorithm_risk_score"]) for row in audit), 6),
        "mean_governance_readiness_score": round(mean(float(row["governance_readiness_score"]) for row in audit), 6),
        "mean_impact_score": round(mean(float(row["impact_score"]) for row in audit), 6),
        "governance_controls": len(controls),
        "interpretation": "Health algorithm governance should connect patient impact, population impact, clinical validation, equity readiness, privacy readiness, human review, workflow integration, monitoring, audit trails, and stop authority.",
    }

    write_csv(TABLES / "health_systems.csv", systems)
    write_csv(TABLES / "health_algorithm_safety_audit.csv", audit)
    write_csv(TABLES / "health_governance_register.csv", controls)
    write_csv(TABLES / "health_algorithm_summary.csv", [summary])

    write_json(JSON_DIR / "health_algorithm_config.json", asdict(config))
    write_json(JSON_DIR / "health_algorithm_safety_audit.json", audit)
    write_json(JSON_DIR / "health_governance_register.json", controls)
    write_json(JSON_DIR / "health_algorithm_summary.json", summary)

    print("Algorithms in health care and public health audit complete.")
    print(TABLES / "health_algorithm_summary.csv")


if __name__ == "__main__":
    main()
