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
class PublicGovernanceConfig:
    article: str = "algorithms_in_public_policy_and_governance"
    high_rights_impact_threshold: float = 0.80
    low_due_process_threshold: float = 0.65
    low_governance_threshold: float = 0.65


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


def public_algorithm_use_cases() -> list[dict[str, object]]:
    return [
        {"use_case_id": "benefits_eligibility_screening", "rights_impact": 0.94, "due_process": 0.58, "transparency": 0.52, "human_review": 0.60, "data_quality": 0.66, "vendor_accountability": 0.48, "appeal_readiness": 0.54, "monitoring": 0.56, "public_value": 0.70},
        {"use_case_id": "restaurant_inspection_targeting", "rights_impact": 0.54, "due_process": 0.70, "transparency": 0.68, "human_review": 0.72, "data_quality": 0.76, "vendor_accountability": 0.74, "appeal_readiness": 0.62, "monitoring": 0.78, "public_value": 0.84},
        {"use_case_id": "fraud_anomaly_flagging", "rights_impact": 0.86, "due_process": 0.50, "transparency": 0.46, "human_review": 0.58, "data_quality": 0.60, "vendor_accountability": 0.44, "appeal_readiness": 0.42, "monitoring": 0.52, "public_value": 0.62},
        {"use_case_id": "emergency_resource_allocation", "rights_impact": 0.78, "due_process": 0.72, "transparency": 0.74, "human_review": 0.80, "data_quality": 0.78, "vendor_accountability": 0.70, "appeal_readiness": 0.66, "monitoring": 0.82, "public_value": 0.90},
    ]


def score_use_case(row: dict[str, object], config: PublicGovernanceConfig) -> dict[str, object]:
    procedural_readiness = mean([
        float(row["due_process"]),
        float(row["transparency"]),
        float(row["human_review"]),
        float(row["appeal_readiness"]),
    ])
    governance_readiness = mean([
        float(row["data_quality"]),
        float(row["vendor_accountability"]),
        float(row["monitoring"]),
        procedural_readiness,
    ])
    public_algorithmic_risk = float(row["rights_impact"]) * (1.0 - governance_readiness)

    recommendation = "proceed_with_governed_support"
    if float(row["rights_impact"]) >= config.high_rights_impact_threshold and procedural_readiness < config.low_due_process_threshold:
        recommendation = "do_not_deploy_without_due_process_redesign"
    elif governance_readiness < config.low_governance_threshold:
        recommendation = "governance_review_required"
    elif float(row["rights_impact"]) >= config.high_rights_impact_threshold:
        recommendation = "deploy_only_with_independent_oversight"
    elif float(row["public_value"]) < 0.60:
        recommendation = "reassess_public_value"

    return {
        "use_case_id": row["use_case_id"],
        "rights_impact": round(float(row["rights_impact"]), 6),
        "due_process": round(float(row["due_process"]), 6),
        "transparency": round(float(row["transparency"]), 6),
        "human_review": round(float(row["human_review"]), 6),
        "data_quality": round(float(row["data_quality"]), 6),
        "vendor_accountability": round(float(row["vendor_accountability"]), 6),
        "appeal_readiness": round(float(row["appeal_readiness"]), 6),
        "monitoring": round(float(row["monitoring"]), 6),
        "public_value": round(float(row["public_value"]), 6),
        "procedural_readiness_score": round(procedural_readiness, 6),
        "governance_readiness_score": round(governance_readiness, 6),
        "public_algorithmic_risk_score": round(public_algorithmic_risk, 6),
        "recommendation": recommendation,
    }


def governance_register() -> list[dict[str, str]]:
    return [
        {"control": "algorithm_inventory", "review_question": "Is the system listed with purpose, owner, vendor, data, and decision role?", "status": "required"},
        {"control": "legal_authority_review", "review_question": "Is there lawful authority for this use and decision role?", "status": "required"},
        {"control": "impact_assessment", "review_question": "Have rights, equity, public value, alternatives, and risks been reviewed?", "status": "required"},
        {"control": "due_process_plan", "review_question": "Are notice, reasons, correction, appeal, and remedy available?", "status": "required"},
        {"control": "vendor_accountability", "review_question": "Do contracts provide documentation, audit rights, update controls, and exit options?", "status": "required"},
        {"control": "monitoring_and_audit", "review_question": "Are performance, errors, drift, reliance, appeals, and harms monitored?", "status": "required"},
        {"control": "stop_rule", "review_question": "Can the system be paused, limited, rolled back, or retired?", "status": "required"},
    ]


def main() -> None:
    config = PublicGovernanceConfig()
    use_cases = public_algorithm_use_cases()
    audit = [score_use_case(row, config) for row in use_cases]
    controls = governance_register()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "use_cases_reviewed": len(audit),
        "use_cases_not_ready_for_deployment": sum(1 for row in audit if row["recommendation"] == "do_not_deploy_without_due_process_redesign"),
        "use_cases_requiring_governance_review": sum(1 for row in audit if row["recommendation"] == "governance_review_required"),
        "use_cases_requiring_independent_oversight": sum(1 for row in audit if row["recommendation"] == "deploy_only_with_independent_oversight"),
        "mean_procedural_readiness_score": round(mean(float(row["procedural_readiness_score"]) for row in audit), 6),
        "mean_governance_readiness_score": round(mean(float(row["governance_readiness_score"]) for row in audit), 6),
        "mean_public_algorithmic_risk_score": round(mean(float(row["public_algorithmic_risk_score"]) for row in audit), 6),
        "governance_controls": len(controls),
        "interpretation": "Public algorithmic governance should connect rights impact, due process, transparency, human review, data quality, vendor accountability, appeals, monitoring, public value, and stop authority.",
    }

    write_csv(TABLES / "public_algorithm_use_cases.csv", use_cases)
    write_csv(TABLES / "public_governance_audit.csv", audit)
    write_csv(TABLES / "public_governance_register.csv", controls)
    write_csv(TABLES / "public_governance_summary.csv", [summary])

    write_json(JSON_DIR / "public_governance_config.json", asdict(config))
    write_json(JSON_DIR / "public_governance_audit.json", audit)
    write_json(JSON_DIR / "public_governance_register.json", controls)
    write_json(JSON_DIR / "public_governance_summary.json", summary)

    print("Algorithms in public policy and governance audit complete.")
    print(TABLES / "public_governance_summary.csv")


if __name__ == "__main__":
    main()
