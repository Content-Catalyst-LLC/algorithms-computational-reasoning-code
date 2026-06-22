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
class RiskGovernanceConfig:
    article: str = "algorithmic_risk_management_and_ai_governance"
    high_residual_risk_threshold: float = 0.30
    low_governance_readiness_threshold: float = 0.70
    high_inherent_risk_threshold: float = 0.50


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


def risk_items() -> list[dict[str, object]]:
    return [
        {"risk_id": "benefits_denial_error", "system": "benefits_eligibility_model", "severity": 0.92, "likelihood": 0.44, "detectability": 0.42, "ownership": 0.60, "documentation": 0.62, "monitoring": 0.58, "contestability": 0.52, "remediation": 0.46, "stop_authority": 0.50, "control_effectiveness": 0.48},
        {"risk_id": "clinical_triage_miscalibration", "system": "clinical_triage_support", "severity": 0.96, "likelihood": 0.30, "detectability": 0.64, "ownership": 0.78, "documentation": 0.80, "monitoring": 0.76, "contestability": 0.70, "remediation": 0.72, "stop_authority": 0.76, "control_effectiveness": 0.72},
        {"risk_id": "content_visibility_feedback_loop", "system": "content_ranking_system", "severity": 0.74, "likelihood": 0.62, "detectability": 0.38, "ownership": 0.56, "documentation": 0.54, "monitoring": 0.50, "contestability": 0.42, "remediation": 0.44, "stop_authority": 0.48, "control_effectiveness": 0.42},
        {"risk_id": "fraud_false_positive", "system": "fraud_alert_model", "severity": 0.82, "likelihood": 0.40, "detectability": 0.58, "ownership": 0.72, "documentation": 0.74, "monitoring": 0.70, "contestability": 0.66, "remediation": 0.68, "stop_authority": 0.70, "control_effectiveness": 0.64},
    ]


def score_risk(row: dict[str, object], config: RiskGovernanceConfig) -> dict[str, object]:
    severity = float(row["severity"])
    likelihood = float(row["likelihood"])
    detectability = float(row["detectability"])
    inherent_risk = severity * likelihood * (1.0 - detectability)

    governance_readiness = mean([
        float(row["ownership"]),
        float(row["documentation"]),
        float(row["monitoring"]),
        float(row["contestability"]),
        float(row["remediation"]),
        float(row["stop_authority"]),
    ])

    control_effectiveness = float(row["control_effectiveness"])
    residual_risk = inherent_risk * (1.0 - control_effectiveness)

    status = "controlled"
    if (
        residual_risk >= config.high_residual_risk_threshold
        or governance_readiness < config.low_governance_readiness_threshold
        or inherent_risk >= config.high_inherent_risk_threshold
    ):
        status = "review"
    if residual_risk >= config.high_residual_risk_threshold and governance_readiness < config.low_governance_readiness_threshold:
        status = "escalate"

    return {
        "risk_id": row["risk_id"],
        "system": row["system"],
        "severity": round(severity, 6),
        "likelihood": round(likelihood, 6),
        "detectability": round(detectability, 6),
        "inherent_risk_score": round(inherent_risk, 6),
        "governance_readiness_score": round(governance_readiness, 6),
        "control_effectiveness": round(control_effectiveness, 6),
        "residual_risk_score": round(residual_risk, 6),
        "status": status,
    }


def governance_controls() -> list[dict[str, str]]:
    return [
        {"control": "use_case_approval", "review_question": "Should this system be built, bought, or deployed?", "status": "required"},
        {"control": "risk_register", "review_question": "Are risks, controls, owners, and escalation triggers documented?", "status": "required"},
        {"control": "impact_assessment", "review_question": "Who may be affected and what harms are possible?", "status": "required"},
        {"control": "monitoring_plan", "review_question": "What signals indicate drift, failure, or harm?", "status": "required"},
        {"control": "incident_response", "review_question": "How are failures preserved, investigated, and remediated?", "status": "required"},
        {"control": "pause_retirement_authority", "review_question": "Who can pause, rollback, or retire the system?", "status": "required"},
    ]


def main() -> None:
    config = RiskGovernanceConfig()
    risks = risk_items()
    audit = [score_risk(row, config) for row in risks]
    controls = governance_controls()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "risks_reviewed": len(audit),
        "risks_controlled": sum(1 for row in audit if row["status"] == "controlled"),
        "risks_requiring_review": sum(1 for row in audit if row["status"] == "review"),
        "risks_escalated": sum(1 for row in audit if row["status"] == "escalate"),
        "mean_inherent_risk_score": round(mean(float(row["inherent_risk_score"]) for row in audit), 6),
        "mean_governance_readiness_score": round(mean(float(row["governance_readiness_score"]) for row in audit), 6),
        "mean_residual_risk_score": round(mean(float(row["residual_risk_score"]) for row in audit), 6),
        "governance_controls": len(controls),
        "interpretation": "Risk governance should connect severity, likelihood, detectability, control effectiveness, ownership, documentation, monitoring, contestability, remediation, and stop authority.",
    }

    write_csv(TABLES / "risk_items.csv", risks)
    write_csv(TABLES / "risk_governance_audit.csv", audit)
    write_csv(TABLES / "risk_governance_controls.csv", controls)
    write_csv(TABLES / "risk_governance_summary.csv", [summary])

    write_json(JSON_DIR / "risk_governance_config.json", asdict(config))
    write_json(JSON_DIR / "risk_governance_audit.json", audit)
    write_json(JSON_DIR / "risk_governance_controls.json", controls)
    write_json(JSON_DIR / "risk_governance_summary.json", summary)

    print("Algorithmic risk management and AI governance audit complete.")
    print(TABLES / "risk_governance_summary.csv")


if __name__ == "__main__":
    main()
