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
class FailureModeConfig:
    article: str = "failure_modes_in_algorithmic_systems"
    high_failure_risk_threshold: float = 0.20
    high_priority_threshold: float = 0.35
    low_resilience_threshold: float = 0.60
    severe_failure_threshold: float = 0.75


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


def failure_modes() -> list[dict[str, object]]:
    return [
        {"failure_id": "schema_drift_in_eligibility_pipeline", "category": "data", "likelihood": 0.42, "severity": 0.86, "detectability": 0.38, "controllability": 0.44, "monitoring": 0.42, "fallback": 0.36, "rollback": 0.50, "escalation": 0.46, "repair": 0.40},
        {"failure_id": "miscalibrated_health_risk_model", "category": "model", "likelihood": 0.28, "severity": 0.94, "detectability": 0.62, "controllability": 0.66, "monitoring": 0.70, "fallback": 0.62, "rollback": 0.68, "escalation": 0.74, "repair": 0.66},
        {"failure_id": "engagement_metric_reward_hacking", "category": "objective", "likelihood": 0.55, "severity": 0.64, "detectability": 0.35, "controllability": 0.40, "monitoring": 0.46, "fallback": 0.32, "rollback": 0.45, "escalation": 0.38, "repair": 0.34},
        {"failure_id": "automation_bias_in_review_workflow", "category": "workflow", "likelihood": 0.48, "severity": 0.78, "detectability": 0.44, "controllability": 0.38, "monitoring": 0.40, "fallback": 0.35, "rollback": 0.52, "escalation": 0.41, "repair": 0.39},
        {"failure_id": "missing_appeal_pathway", "category": "governance", "likelihood": 0.36, "severity": 0.82, "detectability": 0.52, "controllability": 0.30, "monitoring": 0.38, "fallback": 0.28, "rollback": 0.42, "escalation": 0.34, "repair": 0.24},
        {"failure_id": "logging_outage_blocks_audit_trail", "category": "infrastructure", "likelihood": 0.30, "severity": 0.72, "detectability": 0.40, "controllability": 0.46, "monitoring": 0.34, "fallback": 0.45, "rollback": 0.55, "escalation": 0.48, "repair": 0.36},
    ]


def audit_failure(row: dict[str, object], config: FailureModeConfig) -> dict[str, object]:
    likelihood = float(row["likelihood"])
    severity = float(row["severity"])
    detectability = float(row["detectability"])
    controllability = float(row["controllability"])
    resilience_components = [float(row[k]) for k in ["monitoring", "fallback", "rollback", "escalation", "repair"]]

    failure_risk = likelihood * severity * (1.0 - detectability) * (1.0 - controllability)
    priority_score = likelihood * severity * (1.0 - detectability)
    resilience_capacity = mean(resilience_components)
    severe_failure = int(severity >= config.severe_failure_threshold)
    high_failure_risk = int(failure_risk >= config.high_failure_risk_threshold)
    high_priority = int(priority_score >= config.high_priority_threshold)
    low_resilience = int(resilience_capacity < config.low_resilience_threshold)

    status = "pass"
    if high_failure_risk or high_priority or low_resilience:
        status = "review"
    if (high_failure_risk and low_resilience) or (severe_failure and high_priority and low_resilience):
        status = "escalate"

    return {
        "failure_id": row["failure_id"],
        "category": row["category"],
        "likelihood": round(likelihood, 6),
        "severity": round(severity, 6),
        "detectability": round(detectability, 6),
        "controllability": round(controllability, 6),
        "monitoring": round(float(row["monitoring"]), 6),
        "fallback": round(float(row["fallback"]), 6),
        "rollback": round(float(row["rollback"]), 6),
        "escalation": round(float(row["escalation"]), 6),
        "repair": round(float(row["repair"]), 6),
        "failure_risk_score": round(failure_risk, 6),
        "priority_score": round(priority_score, 6),
        "resilience_capacity": round(resilience_capacity, 6),
        "severe_failure": severe_failure,
        "high_failure_risk": high_failure_risk,
        "high_priority": high_priority,
        "low_resilience": low_resilience,
        "status": status,
        "interpretation": "Failure risk rises with likelihood, severity, weak detectability, and weak controllability; resilience depends on monitoring, fallback, rollback, escalation, and repair.",
    }


def failure_taxonomy() -> list[dict[str, str]]:
    return [
        {"category": "data", "description": "Failure in inputs, labels, records, schemas, pipelines, or measurement.", "monitoring_focus": "missingness drift data quality and provenance"},
        {"category": "model", "description": "Failure in prediction, calibration, robustness, subgroup behavior, or generalization.", "monitoring_focus": "error calibration drift and disaggregated performance"},
        {"category": "objective", "description": "Failure from optimizing a metric that does not represent the real goal.", "monitoring_focus": "metric gaming reward hacking and outcome quality"},
        {"category": "interface", "description": "Failure from misleading display, defaults, warnings, explanations, or uncertainty communication.", "monitoring_focus": "user interpretation reliance and error detection"},
        {"category": "workflow", "description": "Failure from human review, organizational procedure, workload, or authority gaps.", "monitoring_focus": "review time acceptance override and escalation"},
        {"category": "infrastructure", "description": "Failure from deployment, dependency, logging, version, API, schema, or rollback problems.", "monitoring_focus": "system dependencies logging and release controls"},
        {"category": "governance", "description": "Failure from weak ownership, appeal, incident response, audit trail, remediation, or retirement.", "monitoring_focus": "ownership incidents appeals and repair"},
    ]


def governance_register() -> list[dict[str, str]]:
    return [
        {"item": "failure_taxonomy", "review_question": "Are data, model, objective, interface, workflow, infrastructure, and governance failures identified?", "status": "required"},
        {"item": "monitoring", "review_question": "Are technical, institutional, and harm signals monitored?", "status": "required"},
        {"item": "fallback", "review_question": "Can the system degrade safely or shift to manual process?", "status": "required"},
        {"item": "rollback", "review_question": "Can unsafe changes be reversed quickly?", "status": "required"},
        {"item": "escalation", "review_question": "Are severe failures routed to accountable owners?", "status": "required"},
        {"item": "repair", "review_question": "Are affected people and source conditions corrected?", "status": "required"},
        {"item": "recurrence_review", "review_question": "Are incidents reviewed for repeated causes and control updates?", "status": "required"},
    ]


def main() -> None:
    config = FailureModeConfig()
    failures = failure_modes()
    audits = [audit_failure(row, config) for row in failures]
    taxonomy = failure_taxonomy()
    governance = governance_register()
    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "failure_modes_reviewed": len(audits),
        "failure_modes_passed": sum(1 for row in audits if row["status"] == "pass"),
        "failure_modes_requiring_review": sum(1 for row in audits if row["status"] == "review"),
        "failure_modes_escalated": sum(1 for row in audits if row["status"] == "escalate"),
        "mean_failure_risk_score": round(mean(float(row["failure_risk_score"]) for row in audits), 6),
        "mean_priority_score": round(mean(float(row["priority_score"]) for row in audits), 6),
        "mean_resilience_capacity": round(mean(float(row["resilience_capacity"]) for row in audits), 6),
        "failure_taxonomy_entries": len(taxonomy),
        "governance_items": len(governance),
        "interpretation": "Failure-mode review should connect technical breakdown, institutional consequence, detection, control, resilience, and accountable response.",
    }

    write_csv(TABLES / "failure_modes.csv", failures)
    write_csv(TABLES / "failure_mode_audit.csv", audits)
    write_csv(TABLES / "failure_mode_taxonomy.csv", taxonomy)
    write_csv(TABLES / "failure_mode_governance_register.csv", governance)
    write_csv(TABLES / "failure_mode_summary.csv", [summary])

    write_json(JSON_DIR / "failure_mode_config.json", asdict(config))
    write_json(JSON_DIR / "failure_mode_audit.json", audits)
    write_json(JSON_DIR / "failure_mode_taxonomy.json", taxonomy)
    write_json(JSON_DIR / "failure_mode_governance_register.json", governance)
    write_json(JSON_DIR / "failure_mode_summary.json", summary)

    print("Failure modes in algorithmic systems audit complete.")
    print(TABLES / "failure_mode_summary.csv")


if __name__ == "__main__":
    main()
