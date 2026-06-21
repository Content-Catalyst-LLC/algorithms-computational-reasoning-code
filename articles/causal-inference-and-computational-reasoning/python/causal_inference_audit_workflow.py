from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean, pstdev
import csv
import json
import math
import random

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"
LOGS = ARTICLE_ROOT / "outputs" / "logs"


@dataclass(frozen=True)
class CausalAuditConfig:
    experiment_name: str = "causal_inference_computational_reasoning"
    seed: int = 2026
    n: int = 1200
    true_effect: float = 0.18
    strata: int = 6


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


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = sorted({key for row in rows for key in row})
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def generate_synthetic_data(config: CausalAuditConfig) -> list[dict[str, object]]:
    rng = random.Random(config.seed)
    rows: list[dict[str, object]] = []

    for unit_id in range(1, config.n + 1):
        prior_risk = rng.random()
        institutional_access = clamp(rng.gauss(0.55 + 0.23 * prior_risk, 0.18))
        baseline_capacity = clamp(rng.gauss(0.50 - 0.22 * prior_risk + 0.16 * institutional_access, 0.17))
        hidden_need = clamp(rng.gauss(0.45 + 0.30 * prior_risk - 0.12 * baseline_capacity, 0.16))

        treatment_probability = sigmoid(
            -0.95
            + 1.65 * prior_risk
            + 0.85 * institutional_access
            - 0.55 * baseline_capacity
            + 0.35 * hidden_need
        )
        treatment = 1 if rng.random() < treatment_probability else 0

        noise = rng.gauss(0.0, 0.075)
        potential_outcome_control = (
            0.28
            + 0.38 * prior_risk
            + 0.12 * institutional_access
            - 0.24 * baseline_capacity
            + 0.10 * hidden_need
            + noise
        )
        heterogeneous_modifier = 0.04 * (1.0 - prior_risk) + 0.03 * baseline_capacity
        individual_effect = config.true_effect + heterogeneous_modifier
        potential_outcome_treated = potential_outcome_control + individual_effect
        observed_outcome = potential_outcome_treated if treatment else potential_outcome_control

        rows.append(
            {
                "unit_id": unit_id,
                "prior_risk": round(prior_risk, 6),
                "institutional_access": round(institutional_access, 6),
                "baseline_capacity": round(baseline_capacity, 6),
                "hidden_need_unobserved_in_real_study": round(hidden_need, 6),
                "treatment_probability": round(treatment_probability, 6),
                "treatment": treatment,
                "potential_outcome_control": round(potential_outcome_control, 6),
                "potential_outcome_treated": round(potential_outcome_treated, 6),
                "individual_true_effect": round(individual_effect, 6),
                "observed_outcome": round(observed_outcome, 6),
                "interpretation": "Synthetic observational data with measured and hidden confounding for teaching causal review.",
            }
        )
    return rows


def column_values(rows: list[dict[str, object]], column: str, treatment: int | None = None) -> list[float]:
    selected = rows if treatment is None else [row for row in rows if int(row["treatment"]) == treatment]
    return [float(row[column]) for row in selected]


def safe_mean(values: list[float]) -> float:
    return mean(values) if values else float("nan")


def naive_effect(rows: list[dict[str, object]]) -> dict[str, object]:
    treated_mean = safe_mean(column_values(rows, "observed_outcome", 1))
    control_mean = safe_mean(column_values(rows, "observed_outcome", 0))
    return {
        "estimate_type": "naive_difference_in_means",
        "estimated_effect": round(treated_mean - control_mean, 6),
        "treated_mean": round(treated_mean, 6),
        "control_mean": round(control_mean, 6),
        "identification_warning": "Association only; treatment assignment is confounded.",
    }


def stratified_adjusted_effect(rows: list[dict[str, object]], strata: int) -> dict[str, object]:
    sorted_rows = sorted(rows, key=lambda row: float(row["prior_risk"]))
    stratum_size = max(1, len(sorted_rows) // strata)
    weighted_effects: list[tuple[float, int]] = []

    for stratum in range(strata):
        start = stratum * stratum_size
        end = len(sorted_rows) if stratum == strata - 1 else min(len(sorted_rows), (stratum + 1) * stratum_size)
        subset = sorted_rows[start:end]
        treated = [float(row["observed_outcome"]) for row in subset if int(row["treatment"]) == 1]
        control = [float(row["observed_outcome"]) for row in subset if int(row["treatment"]) == 0]
        if treated and control:
            weighted_effects.append((mean(treated) - mean(control), len(subset)))

    total_weight = sum(weight for _, weight in weighted_effects)
    effect = sum(effect * weight for effect, weight in weighted_effects) / total_weight
    return {
        "estimate_type": "stratified_adjustment_prior_risk",
        "estimated_effect": round(effect, 6),
        "strata_requested": strata,
        "usable_strata": len(weighted_effects),
        "identification_warning": "Adjusts one measured confounder only; remaining confounding may persist.",
    }


def propensity_score(row: dict[str, object]) -> float:
    return sigmoid(
        -0.95
        + 1.65 * float(row["prior_risk"])
        + 0.85 * float(row["institutional_access"])
        - 0.55 * float(row["baseline_capacity"])
    )


def inverse_probability_weighted_effect(rows: list[dict[str, object]]) -> dict[str, object]:
    treated_num = treated_den = control_num = control_den = 0.0
    clipped = 0
    for row in rows:
        p_raw = propensity_score(row)
        p = min(0.95, max(0.05, p_raw))
        if abs(p - p_raw) > 1e-12:
            clipped += 1
        y = float(row["observed_outcome"])
        if int(row["treatment"]) == 1:
            weight = 1.0 / p
            treated_num += weight * y
            treated_den += weight
        else:
            weight = 1.0 / (1.0 - p)
            control_num += weight * y
            control_den += weight
    effect = treated_num / treated_den - control_num / control_den
    return {
        "estimate_type": "inverse_probability_weighted_effect",
        "estimated_effect": round(effect, 6),
        "weight_clipping_rule": "0.05 <= p <= 0.95",
        "propensity_scores_clipped": clipped,
        "identification_warning": "Depends on measured-confounding and positivity assumptions.",
    }


def standardized_g_computation_effect(rows: list[dict[str, object]]) -> dict[str, object]:
    # Transparent teaching formula fitted from known synthetic structure, not a general estimator.
    predicted_control = []
    predicted_treated = []
    for row in rows:
        base = (
            0.28
            + 0.38 * float(row["prior_risk"])
            + 0.12 * float(row["institutional_access"])
            - 0.24 * float(row["baseline_capacity"])
        )
        modifier = 0.04 * (1.0 - float(row["prior_risk"])) + 0.03 * float(row["baseline_capacity"])
        predicted_control.append(base)
        predicted_treated.append(base + 0.18 + modifier)
    effect = mean(predicted_treated) - mean(predicted_control)
    return {
        "estimate_type": "standardized_g_computation_teaching_formula",
        "estimated_effect": round(effect, 6),
        "identification_warning": "Teaching formula; real g-computation requires model validation and assumptions.",
    }


def balance_diagnostics(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    diagnostics = []
    for column in ["prior_risk", "institutional_access", "baseline_capacity"]:
        treated = column_values(rows, column, 1)
        control = column_values(rows, column, 0)
        treated_mean = mean(treated)
        control_mean = mean(control)
        pooled_sd = math.sqrt((pstdev(treated) ** 2 + pstdev(control) ** 2) / 2.0)
        std_diff = 0.0 if pooled_sd == 0 else (treated_mean - control_mean) / pooled_sd
        diagnostics.append(
            {
                "covariate": column,
                "treated_mean": round(treated_mean, 6),
                "control_mean": round(control_mean, 6),
                "standardized_difference": round(std_diff, 6),
                "absolute_standardized_difference": round(abs(std_diff), 6),
                "review_flag": "review" if abs(std_diff) > 0.10 else "acceptable",
            }
        )
    return diagnostics


def assumption_register() -> list[dict[str, object]]:
    assumptions = [
        CausalAssumption("clear_intervention", "Treatment/intervention is precisely defined.", "What exactly is being changed?", "complete"),
        CausalAssumption("exchangeability", "After adjustment, treatment groups are comparable on potential outcomes.", "Are relevant confounders measured and adjusted?", "partial"),
        CausalAssumption("positivity_overlap", "Comparable treated and untreated units exist across covariate values.", "Is there adequate overlap?", "partial"),
        CausalAssumption("consistency", "Observed outcome corresponds to the defined treatment condition.", "Does treatment mean the same thing across units?", "needs_review"),
        CausalAssumption("no_post_treatment_adjustment", "Adjustment excludes variables caused by treatment.", "Are mediators excluded from confounder adjustment?", "complete"),
        CausalAssumption("external_validity", "Estimate applies only to bounded populations and settings.", "Where should this estimate not be applied?", "needs_review"),
    ]
    return [asdict(item) for item in assumptions]


def sensitivity_rows(estimates: list[dict[str, object]], synthetic_truth: float) -> list[dict[str, object]]:
    rows = []
    for estimate in estimates:
        effect = float(estimate["estimated_effect"])
        for hidden_bias in [0.00, 0.03, 0.06, 0.09, 0.12]:
            adjusted = effect - hidden_bias
            rows.append(
                {
                    "estimate_type": estimate["estimate_type"],
                    "reported_effect": round(effect, 6),
                    "hypothetical_unmeasured_confounding_bias": round(hidden_bias, 6),
                    "bias_adjusted_effect": round(adjusted, 6),
                    "distance_from_synthetic_truth": round(abs(adjusted - synthetic_truth), 6),
                    "interpretation": "Sensitivity row shows how a causal conclusion changes under hypothetical unmeasured confounding.",
                }
            )
    return rows


def main() -> None:
    config = CausalAuditConfig()
    rows = generate_synthetic_data(config)
    synthetic_truth = mean(float(row["individual_true_effect"]) for row in rows)
    estimates = [
        naive_effect(rows),
        stratified_adjusted_effect(rows, config.strata),
        inverse_probability_weighted_effect(rows),
        standardized_g_computation_effect(rows),
    ]
    balance = balance_diagnostics(rows)
    assumptions = assumption_register()
    sensitivity = sensitivity_rows(estimates, synthetic_truth)

    treated_count = sum(1 for row in rows if int(row["treatment"]) == 1)
    control_count = len(rows) - treated_count
    summary = {
        "article": "Causal Inference and Computational Reasoning",
        "timestamp_utc": timestamp_utc(),
        "n": len(rows),
        "treated_count": treated_count,
        "control_count": control_count,
        "synthetic_average_true_effect": round(synthetic_truth, 6),
        "largest_covariate_imbalance": max(float(item["absolute_standardized_difference"]) for item in balance),
        "estimates": estimates,
        "assumptions_needing_review": [item["assumption"] for item in assumptions if item["status"] != "complete"],
        "use_boundary": "Synthetic educational workflow; not a real-world causal claim.",
    }

    write_csv(TABLES / "synthetic_causal_observations.csv", rows)
    write_csv(TABLES / "causal_effect_estimates.csv", estimates)
    write_csv(TABLES / "covariate_balance_diagnostics.csv", balance)
    write_csv(TABLES / "causal_assumption_register.csv", assumptions)
    write_csv(TABLES / "sensitivity_analysis.csv", sensitivity)
    write_csv(TABLES / "causal_audit_summary.csv", [summary])

    write_json(JSON_DIR / "causal_audit_config.json", asdict(config))
    write_json(JSON_DIR / "causal_audit_summary.json", summary)
    write_json(JSON_DIR / "causal_effect_estimates.json", estimates)
    write_json(JSON_DIR / "covariate_balance_diagnostics.json", balance)
    write_json(JSON_DIR / "causal_assumption_register.json", assumptions)
    write_json(JSON_DIR / "sensitivity_analysis.json", sensitivity)
    write_json(LOGS / "workflow_manifest.json", {
        "generated_at_utc": timestamp_utc(),
        "workflow": "dependency-light causal audit",
        "outputs": [
            "synthetic_causal_observations.csv",
            "causal_effect_estimates.csv",
            "covariate_balance_diagnostics.csv",
            "causal_assumption_register.csv",
            "sensitivity_analysis.csv",
            "causal_audit_summary.json",
        ],
    })

    print("Causal inference audit workflow complete.")
    print(JSON_DIR / "causal_audit_summary.json")


if __name__ == "__main__":
    main()
