from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean
import csv
import json
import math
import random

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"
LOGS = ARTICLE_ROOT / "outputs" / "logs"


@dataclass(frozen=True)
class InterventionConfig:
    seed: int = 20260621
    n: int = 900
    baseline_threshold: float = 0.55
    cost_weight: float = 0.35
    risk_penalty_weight: float = 0.15


@dataclass(frozen=True)
class InterventionScenario:
    intervention_name: str
    support_delta: float
    barrier_delta: float
    quality_delta: float
    implementation_cost: float
    governance_risk: float
    description: str


def timestamp_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def sigmoid(value: float) -> float:
    return 1.0 / (1.0 + math.exp(-value))


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
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def default_scenarios() -> list[InterventionScenario]:
    return [
        InterventionScenario("increase_support", 0.16, 0.00, 0.02, 0.18, 0.07, "Increase support intensity while leaving barriers largely unchanged."),
        InterventionScenario("reduce_access_barrier", 0.02, -0.18, 0.03, 0.22, 0.05, "Reduce access barriers through institutional redesign."),
        InterventionScenario("improve_service_quality", 0.03, -0.03, 0.18, 0.20, 0.04, "Improve service quality and implementation reliability."),
        InterventionScenario("combined_policy", 0.12, -0.14, 0.10, 0.34, 0.10, "Combine support, access, and quality improvements."),
        InterventionScenario("threshold_rule_change", 0.00, 0.00, 0.00, 0.05, 0.14, "Change the action threshold without changing underlying conditions."),
    ]


def generate_cases(config: InterventionConfig) -> list[dict[str, object]]:
    rng = random.Random(config.seed)
    rows: list[dict[str, object]] = []
    for case_id in range(1, config.n + 1):
        baseline_need = rng.random()
        access_barrier = clamp(rng.gauss(0.42 + 0.32 * baseline_need, 0.18))
        service_quality = clamp(rng.gauss(0.62 - 0.16 * access_barrier, 0.14))
        support_intensity = clamp(rng.gauss(0.38 + 0.10 * baseline_need - 0.08 * access_barrier, 0.16))
        implementation_cost = clamp(rng.gauss(0.20 + 0.16 * support_intensity + 0.12 * access_barrier, 0.08))
        baseline_outcome = clamp(sigmoid(-0.65 + 0.95 * support_intensity + 0.80 * service_quality - 0.95 * access_barrier + 0.35 * baseline_need))
        baseline_decision_score = clamp(0.45 * baseline_outcome + 0.25 * support_intensity + 0.20 * service_quality - 0.10 * access_barrier)
        baseline_decision = "act" if baseline_decision_score >= config.baseline_threshold else "monitor"
        rows.append({
            "case_id": case_id,
            "baseline_need": round(baseline_need, 6),
            "access_barrier": round(access_barrier, 6),
            "service_quality": round(service_quality, 6),
            "support_intensity": round(support_intensity, 6),
            "implementation_cost": round(implementation_cost, 6),
            "baseline_outcome": round(baseline_outcome, 6),
            "baseline_decision_score": round(baseline_decision_score, 6),
            "baseline_decision": baseline_decision,
            "interpretation": "Synthetic case generated for intervention modeling; not operational evidence.",
        })
    return rows


def apply_scenario(case: dict[str, object], scenario: InterventionScenario, config: InterventionConfig) -> dict[str, object]:
    support = clamp(float(case["support_intensity"]) + scenario.support_delta)
    barrier = clamp(float(case["access_barrier"]) + scenario.barrier_delta)
    quality = clamp(float(case["service_quality"]) + scenario.quality_delta)
    baseline_need = float(case["baseline_need"])
    outcome = clamp(sigmoid(-0.65 + 0.95 * support + 0.80 * quality - 0.95 * barrier + 0.35 * baseline_need))
    effect = outcome - float(case["baseline_outcome"])
    score = clamp(0.45 * outcome + 0.25 * support + 0.20 * quality - 0.10 * barrier)
    threshold = config.baseline_threshold - 0.06 if scenario.intervention_name == "threshold_rule_change" else config.baseline_threshold
    decision = "act" if score >= threshold else "monitor"
    net_benefit = effect - config.cost_weight * scenario.implementation_cost - config.risk_penalty_weight * scenario.governance_risk
    return {
        "case_id": case["case_id"],
        "intervention_name": scenario.intervention_name,
        "description": scenario.description,
        "modeled_support_intensity": round(support, 6),
        "modeled_access_barrier": round(barrier, 6),
        "modeled_service_quality": round(quality, 6),
        "baseline_outcome": case["baseline_outcome"],
        "intervention_outcome": round(outcome, 6),
        "estimated_effect": round(effect, 6),
        "baseline_decision": case["baseline_decision"],
        "intervention_decision": decision,
        "decision_changed": decision != case["baseline_decision"],
        "implementation_cost": round(scenario.implementation_cost, 6),
        "governance_risk": round(scenario.governance_risk, 6),
        "net_benefit": round(net_benefit, 6),
        "interpretation": "Scenario outcome is modeled under explicit assumptions; it is not proof of real-world causal effect.",
    }


def build_scenario_rows(cases: list[dict[str, object]], scenarios: list[InterventionScenario], config: InterventionConfig) -> list[dict[str, object]]:
    return [apply_scenario(case, scenario, config) for case in cases for scenario in scenarios]


def estimate_effects(scenario_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    names = sorted({str(row["intervention_name"]) for row in scenario_rows})
    estimates: list[dict[str, object]] = []
    for name in names:
        rows = [row for row in scenario_rows if row["intervention_name"] == name]
        effects = [float(row["estimated_effect"]) for row in rows]
        net = [float(row["net_benefit"]) for row in rows]
        changed = [row for row in rows if row["decision_changed"]]
        estimates.append({
            "intervention_name": name,
            "mean_estimated_effect": round(mean(effects), 6),
            "min_estimated_effect": round(min(effects), 6),
            "max_estimated_effect": round(max(effects), 6),
            "mean_net_benefit": round(mean(net), 6),
            "decision_change_rate": round(len(changed) / len(rows), 6),
            "cases_evaluated": len(rows),
            "interpretation": "Compare modeled effect with net benefit and decision-change rate before recommending action.",
        })
    return estimates


def feasibility_review(estimates: list[dict[str, object]]) -> list[dict[str, object]]:
    review: list[dict[str, object]] = []
    for row in estimates:
        effect = float(row["mean_estimated_effect"])
        net = float(row["mean_net_benefit"])
        change_rate = float(row["decision_change_rate"])
        if effect > 0.035 and net > 0.0 and change_rate < 0.65:
            status = "candidate_for_review"
        elif effect > 0.025 and net <= 0.0:
            status = "benefit_cost_tension"
        elif change_rate >= 0.65:
            status = "high_rule_disruption"
        else:
            status = "weak_or_uncertain"
        review.append({
            "intervention_name": row["intervention_name"],
            "mean_estimated_effect": row["mean_estimated_effect"],
            "mean_net_benefit": row["mean_net_benefit"],
            "decision_change_rate": row["decision_change_rate"],
            "feasibility_status": status,
            "review_question": "Should this intervention move forward after causal, ethical, operational, and stakeholder review?",
        })
    return review


def audit_summary(config: InterventionConfig, cases: list[dict[str, object]], estimates: list[dict[str, object]], feasibility: list[dict[str, object]]) -> dict[str, object]:
    best_effect = max(estimates, key=lambda row: float(row["mean_estimated_effect"]))
    best_net = max(estimates, key=lambda row: float(row["mean_net_benefit"]))
    return {
        "article": "causal_algorithms_and_intervention_modeling",
        "timestamp_utc": timestamp_utc(),
        "synthetic_cases": len(cases),
        "interventions_compared": len(estimates),
        "baseline_threshold": config.baseline_threshold,
        "best_mean_effect_intervention": best_effect["intervention_name"],
        "best_mean_effect": best_effect["mean_estimated_effect"],
        "best_net_benefit_intervention": best_net["intervention_name"],
        "best_mean_net_benefit": best_net["mean_net_benefit"],
        "items_requiring_feasibility_review": sum(1 for row in feasibility if row["feasibility_status"] != "weak_or_uncertain"),
        "interpretation": "Intervention modeling compares conditional action scenarios, but causal validity and responsible use depend on assumptions, feasibility, sensitivity, and governance review.",
    }


def main() -> None:
    config = InterventionConfig()
    scenarios = default_scenarios()
    cases = generate_cases(config)
    scenario_rows = build_scenario_rows(cases, scenarios, config)
    estimates = estimate_effects(scenario_rows)
    feasibility = feasibility_review(estimates)
    summary = audit_summary(config, cases, estimates, feasibility)

    write_csv(TABLES / "synthetic_intervention_cases.csv", cases)
    write_csv(TABLES / "intervention_scenarios.csv", scenario_rows)
    write_csv(TABLES / "intervention_effect_estimates.csv", estimates)
    write_csv(TABLES / "intervention_feasibility_review.csv", feasibility)
    write_json(JSON_DIR / "intervention_config.json", asdict(config))
    write_json(JSON_DIR / "intervention_scenarios.json", [asdict(s) for s in scenarios])
    write_json(JSON_DIR / "intervention_effect_estimates.json", estimates)
    write_json(JSON_DIR / "intervention_modeling_audit_summary.json", summary)
    write_json(LOGS / "workflow_manifest.json", {
        "workflow": "intervention_modeling_workflow",
        "timestamp_utc": timestamp_utc(),
        "outputs": [
            "synthetic_intervention_cases.csv",
            "intervention_scenarios.csv",
            "intervention_effect_estimates.csv",
            "intervention_feasibility_review.csv",
            "intervention_modeling_audit_summary.json",
        ],
    })
    print("Causal algorithms and intervention modeling workflow complete.")
    print(TABLES / "intervention_effect_estimates.csv")


if __name__ == "__main__":
    main()
