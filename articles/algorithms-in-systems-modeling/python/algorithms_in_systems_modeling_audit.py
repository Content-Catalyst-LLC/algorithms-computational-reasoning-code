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
class SystemsModelingConfig:
    article: str = "algorithms_in_systems_modeling"
    high_vulnerability_threshold: float = 0.70
    low_governance_threshold: float = 0.65
    low_resilience_threshold: float = 0.50


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


def system_scenarios() -> list[dict[str, object]]:
    return [
        {"scenario_id": "urban_congestion_intervention", "feedback_strength": 0.72, "network_dependency": 0.68, "scenario_uncertainty": 0.54, "resilience": 0.62, "calibration": 0.70, "documentation": 0.74, "governance": 0.70, "stakes": 0.76},
        {"scenario_id": "public_health_capacity_stress", "feedback_strength": 0.80, "network_dependency": 0.74, "scenario_uncertainty": 0.62, "resilience": 0.46, "calibration": 0.66, "documentation": 0.70, "governance": 0.68, "stakes": 0.92},
        {"scenario_id": "supply_chain_disruption", "feedback_strength": 0.64, "network_dependency": 0.88, "scenario_uncertainty": 0.70, "resilience": 0.42, "calibration": 0.58, "documentation": 0.62, "governance": 0.54, "stakes": 0.84},
        {"scenario_id": "routine_service_queue", "feedback_strength": 0.34, "network_dependency": 0.28, "scenario_uncertainty": 0.32, "resilience": 0.82, "calibration": 0.82, "documentation": 0.78, "governance": 0.76, "stakes": 0.30},
    ]


def score_scenario(row: dict[str, object], config: SystemsModelingConfig) -> dict[str, object]:
    vulnerability = mean([
        float(row["feedback_strength"]),
        float(row["network_dependency"]),
        float(row["scenario_uncertainty"]),
        1.0 - float(row["resilience"]),
    ])
    readiness = mean([
        float(row["calibration"]),
        float(row["documentation"]),
        float(row["governance"]),
        float(row["resilience"]),
    ])
    system_risk = float(row["stakes"]) * vulnerability * (1.0 - readiness)

    recommendation = "model_support_acceptable"
    if vulnerability >= config.high_vulnerability_threshold and readiness < config.low_governance_threshold:
        recommendation = "do_not_use_for_decision_without_redesign"
    elif float(row["resilience"]) < config.low_resilience_threshold and float(row["stakes"]) >= 0.80:
        recommendation = "stress_test_and_escalate"
    elif readiness < config.low_governance_threshold:
        recommendation = "governance_review_required"
    elif vulnerability >= config.high_vulnerability_threshold:
        recommendation = "use_only_with_uncertainty_review"

    return {
        "scenario_id": row["scenario_id"],
        "feedback_strength": round(float(row["feedback_strength"]), 6),
        "network_dependency": round(float(row["network_dependency"]), 6),
        "scenario_uncertainty": round(float(row["scenario_uncertainty"]), 6),
        "resilience": round(float(row["resilience"]), 6),
        "calibration": round(float(row["calibration"]), 6),
        "documentation": round(float(row["documentation"]), 6),
        "governance": round(float(row["governance"]), 6),
        "stakes": round(float(row["stakes"]), 6),
        "system_vulnerability_score": round(vulnerability, 6),
        "model_readiness_score": round(readiness, 6),
        "system_modeling_risk_score": round(system_risk, 6),
        "recommendation": recommendation,
    }


def systems_modeling_register() -> list[dict[str, str]]:
    return [
        {"control": "boundary_statement", "review_question": "Are system boundaries and exclusions documented?", "status": "required"},
        {"control": "assumption_register", "review_question": "Are feedback loops, parameters, and behavioral assumptions recorded?", "status": "required"},
        {"control": "scenario_archive", "review_question": "Are scenarios, shocks, interventions, and outputs reproducible?", "status": "required"},
        {"control": "sensitivity_analysis", "review_question": "Which assumptions drive model conclusions?", "status": "required"},
        {"control": "uncertainty_report", "review_question": "Are ranges, fragility, and limits communicated?", "status": "required"},
        {"control": "decision_log", "review_question": "How did model outputs influence action?", "status": "required"},
        {"control": "stop_rule", "review_question": "Can model use be paused, revised, or retired?", "status": "required"},
    ]


def main() -> None:
    config = SystemsModelingConfig()
    scenarios = system_scenarios()
    audit = [score_scenario(row, config) for row in scenarios]
    controls = systems_modeling_register()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "scenarios_reviewed": len(audit),
        "scenarios_for_escalation": sum(1 for row in audit if row["recommendation"] == "stress_test_and_escalate"),
        "scenarios_requiring_governance_review": sum(1 for row in audit if row["recommendation"] == "governance_review_required"),
        "scenarios_not_ready_for_decision_use": sum(1 for row in audit if row["recommendation"] == "do_not_use_for_decision_without_redesign"),
        "mean_system_vulnerability_score": round(mean(float(row["system_vulnerability_score"]) for row in audit), 6),
        "mean_model_readiness_score": round(mean(float(row["model_readiness_score"]) for row in audit), 6),
        "mean_system_modeling_risk_score": round(mean(float(row["system_modeling_risk_score"]) for row in audit), 6),
        "governance_controls": len(controls),
        "interpretation": "Systems modeling review should connect feedback, network dependency, scenario uncertainty, resilience, calibration, documentation, governance, and decision use.",
    }

    write_csv(TABLES / "system_scenarios.csv", scenarios)
    write_csv(TABLES / "systems_modeling_audit.csv", audit)
    write_csv(TABLES / "systems_modeling_register.csv", controls)
    write_csv(TABLES / "systems_modeling_summary.csv", [summary])

    write_json(JSON_DIR / "systems_modeling_config.json", asdict(config))
    write_json(JSON_DIR / "systems_modeling_audit.json", audit)
    write_json(JSON_DIR / "systems_modeling_register.json", controls)
    write_json(JSON_DIR / "systems_modeling_summary.json", summary)

    print("Algorithms in systems modeling audit complete.")
    print(TABLES / "systems_modeling_summary.csv")


if __name__ == "__main__":
    main()
