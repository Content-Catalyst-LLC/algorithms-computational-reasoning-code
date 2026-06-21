from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from datetime import datetime, timezone
import csv
import json
import random

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"
LOGS = ARTICLE_ROOT / "outputs" / "logs"


@dataclass(frozen=True)
class RiskWorkflowConfig:
    article: str
    seed: int
    n_cases: int
    action_threshold: float
    high_risk_threshold: float


@dataclass(frozen=True)
class DecisionOption:
    option_name: str
    risk_reduction: float
    benefit_multiplier: float
    cost_multiplier: float
    governance_burden: str


def timestamp_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fields = sorted({key for row in rows for key in row.keys()})
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def default_config() -> RiskWorkflowConfig:
    return RiskWorkflowConfig(
        article="decision_under_uncertainty_and_computational_risk",
        seed=20260621,
        n_cases=300,
        action_threshold=0.08,
        high_risk_threshold=0.65,
    )


def decision_options() -> list[DecisionOption]:
    return [
        DecisionOption("monitor_only", 0.00, 0.00, 0.00, "low"),
        DecisionOption("light_touch_support", 0.10, 0.55, 0.35, "moderate"),
        DecisionOption("targeted_intervention", 0.22, 0.85, 0.65, "high"),
        DecisionOption("intensive_review", 0.34, 1.05, 1.10, "very_high"),
    ]


def generate_cases(config: RiskWorkflowConfig) -> list[dict[str, object]]:
    rng = random.Random(config.seed)
    rows: list[dict[str, object]] = []
    for case_id in range(1, config.n_cases + 1):
        baseline_risk = max(0.01, min(0.95, rng.betavariate(2.2, 3.4)))
        uncertainty = max(0.02, min(0.25, rng.gauss(0.08 + 0.10 * baseline_risk, 0.03)))
        benefit_if_success = max(20.0, rng.gauss(100.0 + 80.0 * baseline_risk, 25.0))
        loss_if_failure = max(40.0, rng.gauss(120.0 + 140.0 * baseline_risk, 40.0))
        intervention_cost = max(5.0, rng.gauss(25.0 + 35.0 * baseline_risk, 8.0))
        confidence_score = max(0.05, min(0.98, rng.gauss(0.82 - 0.35 * uncertainty, 0.07)))
        rows.append({
            "case_id": case_id,
            "baseline_risk": round(baseline_risk, 6),
            "risk_uncertainty": round(uncertainty, 6),
            "risk_lower": round(max(0.0, baseline_risk - uncertainty), 6),
            "risk_upper": round(min(1.0, baseline_risk + uncertainty), 6),
            "benefit_if_success": round(benefit_if_success, 6),
            "loss_if_failure": round(loss_if_failure, 6),
            "intervention_cost": round(intervention_cost, 6),
            "confidence_score": round(confidence_score, 6),
            "risk_band": "high" if baseline_risk >= config.high_risk_threshold else "moderate" if baseline_risk >= 0.35 else "low",
            "interpretation": "Synthetic case for comparing decision rules under uncertainty.",
        })
    return rows


def score_option(case: dict[str, object], option: DecisionOption) -> dict[str, object]:
    baseline_risk = float(case["baseline_risk"])
    risk_upper = float(case["risk_upper"])
    benefit = float(case["benefit_if_success"])
    loss = float(case["loss_if_failure"])
    cost = float(case["intervention_cost"]) * option.cost_multiplier
    post_risk = max(0.0, baseline_risk * (1.0 - option.risk_reduction))
    expected_benefit = option.benefit_multiplier * benefit * baseline_risk
    expected_loss = post_risk * loss
    expected_net_value = expected_benefit - expected_loss - cost
    downside_exposure = max(0.0, risk_upper * loss + cost - expected_benefit)
    return {
        "case_id": int(case["case_id"]),
        "option_name": option.option_name,
        "baseline_risk": round(baseline_risk, 6),
        "post_intervention_risk": round(post_risk, 6),
        "risk_reduction": round(option.risk_reduction, 6),
        "expected_benefit": round(expected_benefit, 6),
        "expected_loss": round(expected_loss, 6),
        "intervention_cost": round(cost, 6),
        "expected_net_value": round(expected_net_value, 6),
        "downside_exposure": round(downside_exposure, 6),
        "confidence_score": float(case["confidence_score"]),
        "governance_burden": option.governance_burden,
        "interpretation": "Expected value is conditional on synthetic assumptions and is not a complete ethical decision rule.",
    }


def build_metrics(cases: list[dict[str, object]], options: list[DecisionOption]) -> list[dict[str, object]]:
    metrics = [score_option(case, option) for case in cases for option in options]
    by_case: dict[int, list[dict[str, object]]] = {}
    for row in metrics:
        by_case.setdefault(int(row["case_id"]), []).append(row)
    enriched: list[dict[str, object]] = []
    for _, rows in by_case.items():
        best_value = max(float(row["expected_net_value"]) for row in rows)
        for row in rows:
            row = dict(row)
            row["regret"] = round(best_value - float(row["expected_net_value"]), 6)
            row["max_regret_reference"] = round(best_value, 6)
            enriched.append(row)
    return enriched


def threshold_review(metrics: list[dict[str, object]], config: RiskWorkflowConfig) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    by_case: dict[int, list[dict[str, object]]] = {}
    for row in metrics:
        by_case.setdefault(int(row["case_id"]), []).append(row)
    for case_id, options in by_case.items():
        best = max(options, key=lambda row: float(row["expected_net_value"]))
        risk = float(best["baseline_risk"])
        value = float(best["expected_net_value"])
        confidence = float(best["confidence_score"])
        if value >= config.action_threshold and risk >= 0.35 and confidence >= 0.55:
            decision = "act_with_review"
        elif risk >= config.high_risk_threshold and confidence < 0.55:
            decision = "escalate_uncertainty"
        elif value < config.action_threshold:
            decision = "defer_or_monitor"
        else:
            decision = "human_review_required"
        rows.append({
            "case_id": case_id,
            "recommended_option": best["option_name"],
            "baseline_risk": round(risk, 6),
            "best_expected_net_value": round(value, 6),
            "confidence_score": round(confidence, 6),
            "decision": decision,
            "threshold_rule": "act if expected net value exceeds action threshold, risk is moderate/high, and confidence is adequate",
            "review_note": "Threshold rules must be justified by governance, not only optimized numerically.",
        })
    return rows


def risk_register(metrics: list[dict[str, object]], threshold_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    decisions = {int(row["case_id"]): row for row in threshold_rows}
    rows: list[dict[str, object]] = []
    for row in metrics:
        if row["option_name"] != decisions[int(row["case_id"])]["recommended_option"]:
            continue
        downside = float(row["downside_exposure"])
        confidence = float(row["confidence_score"])
        if downside > 180 or confidence < 0.5:
            severity = "high"
        elif downside > 100 or confidence < 0.65:
            severity = "medium"
        else:
            severity = "low"
        rows.append({
            "case_id": row["case_id"],
            "risk_item": "decision_uncertainty_exposure",
            "recommended_option": row["option_name"],
            "downside_exposure": round(downside, 6),
            "confidence_score": round(confidence, 6),
            "severity": severity,
            "mitigation": "escalate high-severity cases; document threshold rationale; provide contestability pathway",
        })
    return rows


def summarize(cases: list[dict[str, object]], metrics: list[dict[str, object]], thresholds: list[dict[str, object]], risks: list[dict[str, object]], config: RiskWorkflowConfig) -> dict[str, object]:
    acted = [row for row in thresholds if row["decision"] == "act_with_review"]
    escalated = [row for row in thresholds if row["decision"] == "escalate_uncertainty"]
    high_risks = [row for row in risks if row["severity"] == "high"]
    best_values = [float(row["best_expected_net_value"]) for row in thresholds]
    return {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "case_count": len(cases),
        "option_count": len(decision_options()),
        "metric_rows": len(metrics),
        "action_threshold": config.action_threshold,
        "act_with_review_count": len(acted),
        "escalate_uncertainty_count": len(escalated),
        "high_risk_register_count": len(high_risks),
        "mean_best_expected_net_value": round(mean(best_values), 6),
        "mean_baseline_risk": round(mean(float(row["baseline_risk"]) for row in cases), 6),
        "interpretation": "Decision recommendations are threshold-dependent and must be reviewed for uncertainty, utility assumptions, downside risk, and governance legitimacy.",
    }


def main() -> None:
    config = default_config()
    options = decision_options()
    cases = generate_cases(config)
    option_rows = [asdict(option) for option in options]
    metrics = build_metrics(cases, options)
    thresholds = threshold_review(metrics, config)
    risks = risk_register(metrics, thresholds)
    summary = summarize(cases, metrics, thresholds, risks, config)

    write_csv(TABLES / "synthetic_decision_cases.csv", cases)
    write_csv(TABLES / "decision_options.csv", option_rows)
    write_csv(TABLES / "decision_metrics.csv", metrics)
    write_csv(TABLES / "threshold_review.csv", thresholds)
    write_csv(TABLES / "risk_register.csv", risks)
    write_csv(TABLES / "decision_risk_audit_summary.csv", [summary])
    write_json(JSON_DIR / "decision_options.json", option_rows)
    write_json(JSON_DIR / "decision_risk_audit_summary.json", summary)
    write_json(LOGS / "workflow_manifest.json", {
        "generated_by": Path(__file__).name,
        "timestamp_utc": timestamp_utc(),
        "outputs": [
            "synthetic_decision_cases.csv",
            "decision_options.csv",
            "decision_metrics.csv",
            "threshold_review.csv",
            "risk_register.csv",
            "decision_risk_audit_summary.csv",
        ],
    })
    print("Decision under uncertainty workflow complete.")
    print(TABLES / "decision_risk_audit_summary.csv")


if __name__ == "__main__":
    main()
