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
class InfrastructureAlgorithmConfig:
    article: str = "algorithms_in_climate_energy_and_infrastructure"
    high_resilience_risk_threshold: float = 0.70
    low_governance_threshold: float = 0.65
    high_public_impact_threshold: float = 0.80
    high_reliability_impact_threshold: float = 0.80


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


def infrastructure_systems() -> list[dict[str, object]]:
    return [
        {"system_id": "grid_demand_forecast_dispatch", "public_impact": 0.82, "climate_exposure": 0.72, "reliability_impact": 0.92, "equity_readiness": 0.62, "validation_readiness": 0.74, "monitoring_readiness": 0.78, "governance_readiness": 0.66, "maintenance_readiness": 0.70},
        {"system_id": "flood_risk_resilience_map", "public_impact": 0.88, "climate_exposure": 0.94, "reliability_impact": 0.62, "equity_readiness": 0.54, "validation_readiness": 0.68, "monitoring_readiness": 0.60, "governance_readiness": 0.58, "maintenance_readiness": 0.56},
        {"system_id": "bridge_predictive_maintenance", "public_impact": 0.76, "climate_exposure": 0.58, "reliability_impact": 0.84, "equity_readiness": 0.66, "validation_readiness": 0.72, "monitoring_readiness": 0.70, "governance_readiness": 0.64, "maintenance_readiness": 0.78},
        {"system_id": "building_energy_optimization", "public_impact": 0.48, "climate_exposure": 0.42, "reliability_impact": 0.46, "equity_readiness": 0.70, "validation_readiness": 0.78, "monitoring_readiness": 0.74, "governance_readiness": 0.76, "maintenance_readiness": 0.72},
    ]


def score_system(row: dict[str, object], config: InfrastructureAlgorithmConfig) -> dict[str, object]:
    governance_score = mean([
        float(row["equity_readiness"]),
        float(row["validation_readiness"]),
        float(row["monitoring_readiness"]),
        float(row["governance_readiness"]),
        float(row["maintenance_readiness"]),
    ])
    impact_score = mean([
        float(row["public_impact"]),
        float(row["climate_exposure"]),
        float(row["reliability_impact"]),
    ])
    resilience_risk = mean([
        impact_score,
        1.0 - float(row["equity_readiness"]),
        1.0 - float(row["validation_readiness"]),
        1.0 - governance_score,
    ])

    recommendation = "governed_use_with_monitoring"
    if resilience_risk >= config.high_resilience_risk_threshold and governance_score < config.low_governance_threshold:
        recommendation = "redesign_governance_before_public_use"
    elif float(row["climate_exposure"]) >= 0.85 and float(row["equity_readiness"]) < 0.65:
        recommendation = "climate_equity_review_required"
    elif float(row["reliability_impact"]) >= config.high_reliability_impact_threshold and governance_score < 0.75:
        recommendation = "reliability_and_safety_review_required"
    elif float(row["public_impact"]) >= config.high_public_impact_threshold and governance_score < 0.75:
        recommendation = "public_value_and_equity_review_required"
    elif governance_score < config.low_governance_threshold:
        recommendation = "governance_review_required"

    return {
        "system_id": row["system_id"],
        "public_impact": round(float(row["public_impact"]), 6),
        "climate_exposure": round(float(row["climate_exposure"]), 6),
        "reliability_impact": round(float(row["reliability_impact"]), 6),
        "equity_readiness": round(float(row["equity_readiness"]), 6),
        "validation_readiness": round(float(row["validation_readiness"]), 6),
        "monitoring_readiness": round(float(row["monitoring_readiness"]), 6),
        "governance_readiness": round(float(row["governance_readiness"]), 6),
        "maintenance_readiness": round(float(row["maintenance_readiness"]), 6),
        "impact_score": round(impact_score, 6),
        "governance_score": round(governance_score, 6),
        "resilience_risk_score": round(resilience_risk, 6),
        "recommendation": recommendation,
    }


def infrastructure_governance_register() -> list[dict[str, str]]:
    return [
        {"control": "system_inventory", "review_question": "Is the model recorded with owner, purpose, physical system, data sources, decision role, and public impact?", "status": "required"},
        {"control": "uncertainty_and_scenario_review", "review_question": "Are uncertainty, scenarios, time horizon, spatial scale, and assumptions documented?", "status": "required"},
        {"control": "equity_and_public_value_review", "review_question": "Are affected communities, service access, vulnerability, and distributional burdens reviewed?", "status": "required"},
        {"control": "validation_and_stress_testing", "review_question": "Are historical tests, stress scenarios, sensitivity, and physical plausibility reviewed?", "status": "required"},
        {"control": "monitoring_and_maintenance", "review_question": "Are data quality, sensor coverage, drift, maintenance, and incident learning monitored?", "status": "required"},
        {"control": "human_override_and_emergency_protocol", "review_question": "Can operators override outputs during unsafe, uncertain, or emergency conditions?", "status": "required"},
        {"control": "stop_rule", "review_question": "Can the system be paused, limited, rolled back, or retired when unsafe or misleading?", "status": "required"},
    ]


def main() -> None:
    config = InfrastructureAlgorithmConfig()
    systems = infrastructure_systems()
    audit = [score_system(row, config) for row in systems]
    controls = infrastructure_governance_register()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "systems_reviewed": len(audit),
        "systems_requiring_governance_redesign": sum(1 for row in audit if row["recommendation"] == "redesign_governance_before_public_use"),
        "systems_requiring_public_value_review": sum(1 for row in audit if row["recommendation"] == "public_value_and_equity_review_required"),
        "systems_requiring_reliability_review": sum(1 for row in audit if row["recommendation"] == "reliability_and_safety_review_required"),
        "systems_requiring_climate_equity_review": sum(1 for row in audit if row["recommendation"] == "climate_equity_review_required"),
        "mean_resilience_risk_score": round(mean(float(row["resilience_risk_score"]) for row in audit), 6),
        "mean_governance_score": round(mean(float(row["governance_score"]) for row in audit), 6),
        "mean_impact_score": round(mean(float(row["impact_score"]) for row in audit), 6),
        "governance_controls": len(controls),
        "interpretation": "Infrastructure algorithm governance should connect climate exposure, public impact, reliability impact, equity readiness, validation, monitoring, maintenance, uncertainty, human override, audit trails, and stop authority.",
    }

    write_csv(TABLES / "infrastructure_systems.csv", systems)
    write_csv(TABLES / "infrastructure_algorithm_risk_audit.csv", audit)
    write_csv(TABLES / "infrastructure_governance_register.csv", controls)
    write_csv(TABLES / "infrastructure_algorithm_summary.csv", [summary])

    write_json(JSON_DIR / "infrastructure_algorithm_config.json", asdict(config))
    write_json(JSON_DIR / "infrastructure_algorithm_risk_audit.json", audit)
    write_json(JSON_DIR / "infrastructure_governance_register.json", controls)
    write_json(JSON_DIR / "infrastructure_algorithm_summary.json", summary)

    print("Algorithms in climate, energy, and infrastructure audit complete.")
    print(TABLES / "infrastructure_algorithm_summary.csv")


if __name__ == "__main__":
    main()
