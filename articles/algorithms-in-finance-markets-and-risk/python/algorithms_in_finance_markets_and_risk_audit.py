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
class FinancialAlgorithmConfig:
    article: str = "algorithms_in_finance_markets_and_risk"
    high_financial_risk_threshold: float = 0.70
    low_governance_threshold: float = 0.65
    high_consumer_impact_threshold: float = 0.80
    high_market_impact_threshold: float = 0.80


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


def financial_systems() -> list[dict[str, object]]:
    return [
        {"system_id": "consumer_credit_scorecard", "market_impact": 0.34, "consumer_impact": 0.92, "model_risk": 0.68, "transparency": 0.58, "human_review": 0.62, "validation": 0.70, "monitoring": 0.66, "governance": 0.64, "liquidity_risk": 0.20},
        {"system_id": "payment_fraud_detector", "market_impact": 0.30, "consumer_impact": 0.78, "model_risk": 0.72, "transparency": 0.46, "human_review": 0.58, "validation": 0.68, "monitoring": 0.74, "governance": 0.60, "liquidity_risk": 0.18},
        {"system_id": "high_frequency_market_maker", "market_impact": 0.90, "consumer_impact": 0.28, "model_risk": 0.82, "transparency": 0.42, "human_review": 0.54, "validation": 0.76, "monitoring": 0.80, "governance": 0.62, "liquidity_risk": 0.88},
        {"system_id": "portfolio_stress_test_engine", "market_impact": 0.62, "consumer_impact": 0.30, "model_risk": 0.64, "transparency": 0.76, "human_review": 0.78, "validation": 0.84, "monitoring": 0.82, "governance": 0.80, "liquidity_risk": 0.70},
    ]


def score_system(row: dict[str, object], config: FinancialAlgorithmConfig) -> dict[str, object]:
    governance_readiness = mean([
        float(row["transparency"]),
        float(row["human_review"]),
        float(row["validation"]),
        float(row["monitoring"]),
        float(row["governance"]),
    ])
    impact = mean([
        float(row["market_impact"]),
        float(row["consumer_impact"]),
        float(row["liquidity_risk"]),
    ])
    financial_algorithm_risk = mean([
        float(row["model_risk"]),
        impact,
        1.0 - governance_readiness,
    ])

    recommendation = "governed_use_with_monitoring"
    if financial_algorithm_risk >= config.high_financial_risk_threshold and governance_readiness < config.low_governance_threshold:
        recommendation = "redesign_controls_before_scaling"
    elif float(row["consumer_impact"]) >= config.high_consumer_impact_threshold and governance_readiness < 0.75:
        recommendation = "consumer_protection_review_required"
    elif float(row["market_impact"]) >= config.high_market_impact_threshold and governance_readiness < 0.75:
        recommendation = "market_stability_review_required"
    elif governance_readiness < config.low_governance_threshold:
        recommendation = "model_governance_review_required"
    elif financial_algorithm_risk >= config.high_financial_risk_threshold:
        recommendation = "use_with_strong_risk_limits"

    return {
        "system_id": row["system_id"],
        "market_impact": round(float(row["market_impact"]), 6),
        "consumer_impact": round(float(row["consumer_impact"]), 6),
        "model_risk": round(float(row["model_risk"]), 6),
        "transparency": round(float(row["transparency"]), 6),
        "human_review": round(float(row["human_review"]), 6),
        "validation": round(float(row["validation"]), 6),
        "monitoring": round(float(row["monitoring"]), 6),
        "governance": round(float(row["governance"]), 6),
        "liquidity_risk": round(float(row["liquidity_risk"]), 6),
        "impact_score": round(impact, 6),
        "governance_readiness_score": round(governance_readiness, 6),
        "financial_algorithm_risk_score": round(financial_algorithm_risk, 6),
        "recommendation": recommendation,
    }


def financial_governance_register() -> list[dict[str, str]]:
    return [
        {"control": "model_inventory", "review_question": "Is the financial algorithm recorded with owner, purpose, scope, status, and decision role?", "status": "required"},
        {"control": "validation_report", "review_question": "Have conceptual soundness, data quality, implementation, backtesting, and limitations been reviewed?", "status": "required"},
        {"control": "consumer_protection_review", "review_question": "Are explanations, adverse-action reasons, correction, appeal, and fair-access effects reviewed?", "status": "required"},
        {"control": "market_stability_review", "review_question": "Are liquidity, market impact, feedback loops, and kill switches reviewed?", "status": "required"},
        {"control": "stress_testing", "review_question": "Are adverse scenarios, tail events, liquidity shocks, and model failure cases tested?", "status": "required"},
        {"control": "audit_trail", "review_question": "Can inputs, outputs, thresholds, overrides, decisions, changes, and incidents be reconstructed?", "status": "required"},
        {"control": "stop_rule", "review_question": "Can the system be paused, limited, rolled back, or retired when unsafe?", "status": "required"},
    ]


def main() -> None:
    config = FinancialAlgorithmConfig()
    systems = financial_systems()
    audit = [score_system(row, config) for row in systems]
    controls = financial_governance_register()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "systems_reviewed": len(audit),
        "systems_requiring_control_redesign": sum(1 for row in audit if row["recommendation"] == "redesign_controls_before_scaling"),
        "systems_requiring_consumer_protection_review": sum(1 for row in audit if row["recommendation"] == "consumer_protection_review_required"),
        "systems_requiring_market_stability_review": sum(1 for row in audit if row["recommendation"] == "market_stability_review_required"),
        "systems_requiring_model_governance_review": sum(1 for row in audit if row["recommendation"] == "model_governance_review_required"),
        "mean_financial_algorithm_risk_score": round(mean(float(row["financial_algorithm_risk_score"]) for row in audit), 6),
        "mean_governance_readiness_score": round(mean(float(row["governance_readiness_score"]) for row in audit), 6),
        "mean_impact_score": round(mean(float(row["impact_score"]) for row in audit), 6),
        "governance_controls": len(controls),
        "interpretation": "Financial algorithm governance should connect market impact, consumer impact, model risk, validation, transparency, human review, monitoring, liquidity risk, audit trails, stress testing, and stop authority.",
    }

    write_csv(TABLES / "financial_systems.csv", systems)
    write_csv(TABLES / "financial_algorithm_risk_audit.csv", audit)
    write_csv(TABLES / "financial_governance_register.csv", controls)
    write_csv(TABLES / "financial_algorithm_summary.csv", [summary])

    write_json(JSON_DIR / "financial_algorithm_config.json", asdict(config))
    write_json(JSON_DIR / "financial_algorithm_risk_audit.json", audit)
    write_json(JSON_DIR / "financial_governance_register.json", controls)
    write_json(JSON_DIR / "financial_algorithm_summary.json", summary)

    print("Algorithms in finance, markets, and risk audit complete.")
    print(TABLES / "financial_algorithm_summary.csv")


if __name__ == "__main__":
    main()
