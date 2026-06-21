from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean, pstdev
import csv
import json
import math
import random
from datetime import datetime, timezone

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class CausalAuditConfig:
    experiment_name: str
    seed: int
    n: int
    true_effect: float
    treatment_threshold: float


@dataclass(frozen=True)
class CausalAssumption:
    assumption: str
    description: str
    review_question: str
    status: str


def timestamp_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


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
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def default_config() -> CausalAuditConfig:
    return CausalAuditConfig(
        experiment_name="causal_inference_computational_reasoning",
        seed=2026,
        n=800,
        true_effect=0.18,
        treatment_threshold=0.50,
    )


def generate_synthetic_data(config: CausalAuditConfig) -> list[dict[str, object]]:
    rng = random.Random(config.seed)
    rows: list[dict[str, object]] = []
    for unit_id in range(1, config.n + 1):
        prior_risk = rng.random()
        institutional_access = max(0.0, min(1.0, rng.gauss(0.55 + 0.25 * prior_risk, 0.18)))
        baseline_capacity = max(0.0, min(1.0, rng.gauss(0.50 - 0.20 * prior_risk + 0.15 * institutional_access, 0.16)))
        treatment_probability = sigmoid(-0.80 + 1.80 * prior_risk + 0.90 * institutional_access - 0.60 * baseline_capacity)
        treatment = 1 if rng.random() < treatment_probability else 0
        noise = rng.gauss(0.0, 0.08)
        untreated_outcome = 0.25 + 0.42 * prior_risk - 0.22 * baseline_capacity + 0.10 * institutional_access + noise
        treated_outcome = untreated_outcome + config.true_effect
        observed_outcome = treated_outcome if treatment == 1 else untreated_outcome
        rows.append({
            "unit_id": unit_id,
            "prior_risk": round(prior_risk, 6),
            "institutional_access": round(institutional_access, 6),
            "baseline_capacity": round(baseline_capacity, 6),
            "treatment_probability": round(treatment_probability, 6),
            "treatment": treatment,
            "potential_outcome_control": round(untreated_outcome, 6),
            "potential_outcome_treated": round(treated_outcome, 6),
            "observed_outcome": round(observed_outcome, 6),
            "true_effect": config.true_effect,
            "interpretation": "Synthetic data include confounding because prior risk and access affect both treatment probability and outcome.",
        })
    return rows


def group_mean(rows: list[dict[str, object]], column: str, treatment: int | None = None) -> float:
    selected = rows if treatment is None else [row for row in rows if int(row["treatment"]) == treatment]
    return mean(float(row[column]) for row in selected)


def naive_effect(rows: list[dict[str, object]]) -> dict[str, object]:
    treated_mean = group_mean(rows, "observed_outcome", 1)
    control_mean = group_mean(rows, "observed_outcome", 0)
    return {
        "estimate_type": "naive_difference_in_means",
        "treated_mean": round(treated_mean, 6),
        "control_mean": round(control_mean, 6),
        "estimated_effect": round(treated_mean - control_mean, 6),
        "interpretation": "Naive comparison may be biased because treatment assignment is confounded.",
    }


def stratified_adjusted_effect(rows: list[dict[str, object]], strata: int = 5) -> dict[str, object]:
    sorted_rows = sorted(rows, key=lambda row: float(row["prior_risk"]))
    stratum_size = len(sorted_rows) // strata
    effects: list[float] = []
    weights: list[int] = []
    for stratum in range(strata):
        start = stratum * stratum_size
        end = len(sorted_rows) if stratum == strata - 1 else (stratum + 1) * stratum_size
        subset = sorted_rows[start:end]
        treated = [row for row in subset if int(row["treatment"]) == 1]
        control = [row for row in subset if int(row["treatment"]) == 0]
        if treated and control:
            effect = mean(float(row["observed_outcome"]) for row in treated) - mean(float(row["observed_outcome"]) for row in control)
            effects.append(effect)
            weights.append(len(subset))
    weighted_effect = sum(effect * weight for effect, weight in zip(effects, weights)) / sum(weights)
    return {
        "estimate_type": "stratified_adjustment_by_prior_risk",
        "strata": strata,
        "usable_strata": len(effects),
        "estimated_effect": round(weighted_effect, 6),
        "interpretation": "Stratified adjustment reduces confounding by comparing treated and control units within risk strata.",
    }


def propensity_score(row: dict[str, object]) -> float:
    return sigmoid(-0.80 + 1.80 * float(row["prior_risk"]) + 0.90 * float(row["institutional_access"]) - 0.60 * float(row["baseline_capacity"]))


def inverse_probability_weighted_effect(rows: list[dict[str, object]]) -> dict[str, object]:
    treated_weighted_outcomes: list[float] = []
    treated_weights: list[float] = []
    control_weighted_outcomes: list[float] = []
    control_weights: list[float] = []
    for row in rows:
        p = max(0.05, min(0.95, propensity_score(row)))
        y = float(row["observed_outcome"])
        if int(row["treatment"]) == 1:
            weight = 1.0 / p
            treated_weighted_outcomes.append(weight * y)
            treated_weights.append(weight)
        else:
            weight = 1.0 / (1.0 - p)
            control_weighted_outcomes.append(weight * y)
            control_weights.append(weight)
    treated_mean = sum(treated_weighted_outcomes) / sum(treated_weights)
    control_mean = sum(control_weighted_outcomes) / sum(control_weights)
    return {
        "estimate_type": "inverse_probability_weighted_effect",
        "treated_weighted_mean": round(treated_mean, 6),
        "control_weighted_mean": round(control_mean, 6),
        "estimated_effect": round(treated_mean - control_mean, 6),
        "interpretation": "IPW estimates the effect after weighting by treatment probability under measured-confounding assumptions.",
    }


def balance_diagnostics(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    diagnostics: list[dict[str, object]] = []
    for column in ["prior_risk", "institutional_access", "baseline_capacity"]:
        treated = [float(row[column]) for row in rows if int(row["treatment"]) == 1]
        control = [float(row[column]) for row in rows if int(row["treatment"]) == 0]
        treated_mean = mean(treated)
        control_mean = mean(control)
        pooled_sd = math.sqrt((pstdev(treated) ** 2 + pstdev(control) ** 2) / 2.0)
        standardized_difference = 0.0 if pooled_sd == 0 else (treated_mean - control_mean) / pooled_sd
        diagnostics.append({
            "covariate": column,
            "treated_mean": round(treated_mean, 6),
            "control_mean": round(control_mean, 6),
            "standardized_difference": round(standardized_difference, 6),
            "absolute_standardized_difference": round(abs(standardized_difference), 6),
            "interpretation": "Large standardized differences suggest imbalance and possible confounding.",
        })
    return diagnostics


def causal_assumptions() -> list[dict[str, object]]:
    assumptions = [
        CausalAssumption("clear_intervention", "The treatment or intervention is defined precisely enough to compare against an alternative.", "Is the treatment operationally clear?", "complete"),
        CausalAssumption("exchangeability", "After adjustment, treated and untreated units are comparable on potential outcomes.", "Are relevant confounders measured and adjusted?", "partial"),
        CausalAssumption("positivity_overlap", "Comparable treated and untreated cases exist across covariate values.", "Is there adequate overlap between groups?", "partial"),
        CausalAssumption("consistency", "Observed outcomes correspond to the defined treatment condition.", "Does treatment mean the same thing across units?", "needs_review"),
        CausalAssumption("no_post_treatment_adjustment", "Adjustment does not condition on variables caused by treatment.", "Are mediators and post-treatment variables excluded from confounder adjustment?", "complete"),
        CausalAssumption("external_validity", "The estimated effect applies only within a defined population and setting.", "Where should the estimate not be generalized?", "needs_review"),
    ]
    return [asdict(item) for item in assumptions]


def sensitivity_rows(estimates: list[dict[str, object]], true_effect: float) -> list[dict[str, object]]:
    return [{
        "estimate_type": estimate["estimate_type"],
        "estimated_effect": round(float(estimate["estimated_effect"]), 6),
        "true_synthetic_effect": round(true_effect, 6),
        "absolute_error_from_synthetic_truth": round(abs(float(estimate["estimated_effect"]) - true_effect), 6),
        "interpretation": "Synthetic truth is known here for teaching; real causal inference usually lacks direct counterfactual truth.",
    } for estimate in estimates]


def main() -> None:
    config = default_config()
    data_rows = generate_synthetic_data(config)
    naive = naive_effect(data_rows)
    stratified = stratified_adjusted_effect(data_rows)
    weighted = inverse_probability_weighted_effect(data_rows)
    estimates = [naive, stratified, weighted]
    balance_rows = balance_diagnostics(data_rows)
    assumption_rows = causal_assumptions()
    sensitivity = sensitivity_rows(estimates, config.true_effect)
    treated_count = sum(1 for row in data_rows if int(row["treatment"]) == 1)
    control_count = len(data_rows) - treated_count
    audit_summary = {
        "article": "causal_inference_and_computational_reasoning",
        "timestamp_utc": timestamp_utc(),
        "n": config.n,
        "treated_count": treated_count,
        "control_count": control_count,
        "true_synthetic_effect": config.true_effect,
        "naive_estimate": naive["estimated_effect"],
        "stratified_estimate": stratified["estimated_effect"],
        "weighted_estimate": weighted["estimated_effect"],
        "largest_covariate_imbalance": max(float(row["absolute_standardized_difference"]) for row in balance_rows),
        "assumption_items_needing_review": sum(1 for row in assumption_rows if row["status"] in {"partial", "needs_review"}),
        "interpretation": "Causal inference workflows should separate predictive association from intervention effects, document assumptions, check imbalance, compare estimators, and report interpretation limits.",
    }
    write_csv(TABLES / "causal_synthetic_observations.csv", data_rows)
    write_csv(TABLES / "causal_effect_estimates.csv", estimates)
    write_csv(TABLES / "causal_balance_diagnostics.csv", balance_rows)
    write_csv(TABLES / "causal_assumption_register.csv", assumption_rows)
    write_csv(TABLES / "causal_estimator_sensitivity.csv", sensitivity)
    write_csv(TABLES / "causal_inference_audit_summary.csv", [audit_summary])
    write_json(JSON_DIR / "causal_audit_config.json", asdict(config))
    write_json(JSON_DIR / "causal_synthetic_observations.json", data_rows)
    write_json(JSON_DIR / "causal_effect_estimates.json", estimates)
    write_json(JSON_DIR / "causal_balance_diagnostics.json", balance_rows)
    write_json(JSON_DIR / "causal_assumption_register.json", assumption_rows)
    write_json(JSON_DIR / "causal_estimator_sensitivity.json", sensitivity)
    write_json(JSON_DIR / "causal_inference_audit_summary.json", audit_summary)
    print("Causal inference audit complete.")
    print(TABLES / "causal_inference_audit_summary.csv")


if __name__ == "__main__":
    main()
