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
class FutureAlgorithmsConfig:
    article: str = "the_future_of_algorithms_computational_reasoning"
    readiness_threshold: float = 0.72
    high_risk_threshold: float = 0.82


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


def future_domains() -> list[dict[str, object]]:
    return [
        {"domain_id": "ai_agents_and_tool_use", "technical_capability": 0.92, "institutional_consequence": 0.94, "uncertainty": 0.86, "automation_level": 0.94, "opacity": 0.88, "contestability_need": 0.94, "governance_maturity": 0.58, "human_judgment_requirement": 0.98, "failure_severity": 0.92, "deployment_readiness": 0.56},
        {"domain_id": "scientific_computing_and_simulation", "technical_capability": 0.90, "institutional_consequence": 0.84, "uncertainty": 0.88, "automation_level": 0.62, "opacity": 0.64, "contestability_need": 0.76, "governance_maturity": 0.76, "human_judgment_requirement": 0.92, "failure_severity": 0.82, "deployment_readiness": 0.76},
        {"domain_id": "public_policy_algorithmic_governance", "technical_capability": 0.78, "institutional_consequence": 0.98, "uncertainty": 0.90, "automation_level": 0.78, "opacity": 0.82, "contestability_need": 0.98, "governance_maturity": 0.62, "human_judgment_requirement": 0.98, "failure_severity": 0.98, "deployment_readiness": 0.50},
        {"domain_id": "platform_attention_systems", "technical_capability": 0.94, "institutional_consequence": 0.96, "uncertainty": 0.80, "automation_level": 0.96, "opacity": 0.90, "contestability_need": 0.92, "governance_maturity": 0.54, "human_judgment_requirement": 0.90, "failure_severity": 0.92, "deployment_readiness": 0.52},
        {"domain_id": "health_decision_support", "technical_capability": 0.86, "institutional_consequence": 0.98, "uncertainty": 0.88, "automation_level": 0.70, "opacity": 0.76, "contestability_need": 0.96, "governance_maturity": 0.72, "human_judgment_requirement": 0.99, "failure_severity": 0.99, "deployment_readiness": 0.66},
        {"domain_id": "climate_energy_infrastructure", "technical_capability": 0.88, "institutional_consequence": 0.96, "uncertainty": 0.94, "automation_level": 0.74, "opacity": 0.70, "contestability_need": 0.86, "governance_maturity": 0.70, "human_judgment_requirement": 0.96, "failure_severity": 0.96, "deployment_readiness": 0.68},
        {"domain_id": "education_learning_systems", "technical_capability": 0.82, "institutional_consequence": 0.90, "uncertainty": 0.82, "automation_level": 0.78, "opacity": 0.78, "contestability_need": 0.90, "governance_maturity": 0.60, "human_judgment_requirement": 0.94, "failure_severity": 0.86, "deployment_readiness": 0.58},
        {"domain_id": "labor_management_systems", "technical_capability": 0.84, "institutional_consequence": 0.96, "uncertainty": 0.84, "automation_level": 0.88, "opacity": 0.86, "contestability_need": 0.96, "governance_maturity": 0.56, "human_judgment_requirement": 0.96, "failure_severity": 0.94, "deployment_readiness": 0.52},
        {"domain_id": "ai_generated_code_and_software", "technical_capability": 0.90, "institutional_consequence": 0.86, "uncertainty": 0.80, "automation_level": 0.84, "opacity": 0.78, "contestability_need": 0.78, "governance_maturity": 0.66, "human_judgment_requirement": 0.94, "failure_severity": 0.84, "deployment_readiness": 0.70},
        {"domain_id": "knowledge_architecture_and_retrieval", "technical_capability": 0.88, "institutional_consequence": 0.84, "uncertainty": 0.78, "automation_level": 0.76, "opacity": 0.72, "contestability_need": 0.82, "governance_maturity": 0.70, "human_judgment_requirement": 0.90, "failure_severity": 0.78, "deployment_readiness": 0.72},
    ]


def risk_score(row: dict[str, object]) -> float:
    return mean([
        float(row["institutional_consequence"]),
        float(row["uncertainty"]),
        float(row["automation_level"]),
        float(row["opacity"]),
        float(row["contestability_need"]),
        float(row["human_judgment_requirement"]),
        float(row["failure_severity"]),
    ])


def readiness_score(row: dict[str, object]) -> float:
    return mean([
        float(row["technical_capability"]),
        float(row["governance_maturity"]),
        float(row["deployment_readiness"]),
    ])


def score_domain(row: dict[str, object], config: FutureAlgorithmsConfig) -> dict[str, object]:
    risk = risk_score(row)
    readiness = readiness_score(row)

    if risk >= config.high_risk_threshold and readiness < config.readiness_threshold:
        status = "high_risk_governance_gap"
    elif risk >= config.high_risk_threshold:
        status = "high_risk_requires_strong_governance"
    elif readiness >= config.readiness_threshold:
        status = "cautious_deployment_possible"
    else:
        status = "further_review_needed"

    scored = {key: round(float(row[key]), 6) for key in [
        "technical_capability", "institutional_consequence", "uncertainty",
        "automation_level", "opacity", "contestability_need", "governance_maturity",
        "human_judgment_requirement", "failure_severity", "deployment_readiness"
    ]}
    scored.update({
        "domain_id": row["domain_id"],
        "risk_score": round(risk, 6),
        "readiness_score": round(readiness, 6),
        "future_status": status,
    })
    return scored


def future_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_confuse_capability_with_readiness", "meaning": "A system can be technically capable before it is institutionally ready."},
        {"caution": "do_not_confuse_ai_assistance_with_authority", "meaning": "AI can assist judgment without replacing accountable decision-making."},
        {"caution": "do_not_optimize_without_value_review", "meaning": "Objectives and metrics must be examined for Goodhart effects and excluded values."},
        {"caution": "do_not_deploy_without_contestability", "meaning": "Affected people need notice, reasons, appeal, and correction pathways."},
        {"caution": "do_not_automate_when_governance_is_absent", "meaning": "High-stakes systems should not be deployed without monitoring, audit, and repair capacity."},
    ]


def no_go_flag(poor_fit: bool, invalid_data: bool, high_opacity: bool, no_appeal: bool, no_governance: bool) -> bool:
    return poor_fit or invalid_data or high_opacity or no_appeal or no_governance


def main() -> None:
    config = FutureAlgorithmsConfig()
    domains = future_domains()
    scored = [score_domain(row, config) for row in domains]
    cautions = future_cautions()

    no_go_rows = [
        {"case_id": "clean_low_stakes_tool", "poor_fit": False, "invalid_data": False, "high_opacity": False, "no_appeal": False, "no_governance": False, "no_go": no_go_flag(False, False, False, False, False)},
        {"case_id": "opaque_high_stakes_decision", "poor_fit": False, "invalid_data": False, "high_opacity": True, "no_appeal": True, "no_governance": True, "no_go": no_go_flag(False, False, True, True, True)},
        {"case_id": "invalid_data_prediction", "poor_fit": False, "invalid_data": True, "high_opacity": False, "no_appeal": False, "no_governance": False, "no_go": no_go_flag(False, True, False, False, False)},
        {"case_id": "poorly_defined_target", "poor_fit": True, "invalid_data": False, "high_opacity": False, "no_appeal": False, "no_governance": False, "no_go": no_go_flag(True, False, False, False, False)},
    ]

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "domains_reviewed": len(scored),
        "high_risk_governance_gaps": sum(1 for row in scored if row["future_status"] == "high_risk_governance_gap"),
        "high_risk_requires_governance": sum(1 for row in scored if row["future_status"] == "high_risk_requires_strong_governance"),
        "cautious_deployment_possible": sum(1 for row in scored if row["future_status"] == "cautious_deployment_possible"),
        "further_review_needed": sum(1 for row in scored if row["future_status"] == "further_review_needed"),
        "mean_risk_score": round(mean(float(row["risk_score"]) for row in scored), 6),
        "mean_readiness_score": round(mean(float(row["readiness_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "no_go_cases": sum(1 for row in no_go_rows if row["no_go"]),
        "interpretation": "The future of algorithms depends on matching technical capability with governance maturity, contestability, evidence discipline, human judgment, and institutional responsibility.",
    }

    write_csv(TABLES / "future_algorithmic_domains.csv", domains)
    write_csv(TABLES / "future_algorithmic_systems_map.csv", scored)
    write_csv(TABLES / "future_algorithmic_cautions.csv", cautions)
    write_csv(TABLES / "no_go_examples.csv", no_go_rows)
    write_csv(TABLES / "future_algorithmic_systems_summary.csv", [summary])

    write_json(JSON_DIR / "future_algorithms_config.json", asdict(config))
    write_json(JSON_DIR / "future_algorithmic_systems_map.json", scored)
    write_json(JSON_DIR / "future_algorithmic_cautions.json", cautions)
    write_json(JSON_DIR / "no_go_examples.json", no_go_rows)
    write_json(JSON_DIR / "future_algorithmic_systems_summary.json", summary)

    print("Future algorithmic systems map complete.")
    print(TABLES / "future_algorithmic_systems_summary.csv")


if __name__ == "__main__":
    main()
