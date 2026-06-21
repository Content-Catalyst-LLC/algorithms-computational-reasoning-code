from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean, pstdev
import csv
import json
import math
import random

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class MonteCarloEstimate:
    experiment: str
    samples: int
    seed: int
    estimate: float
    standard_error: float
    lower_95: float
    upper_95: float
    interpretation: str


def percentile(values: list[float], probability: float) -> float:
    if not values:
        return float("nan")
    ordered = sorted(values)
    index = probability * (len(ordered) - 1)
    lower = math.floor(index)
    upper = math.ceil(index)
    if lower == upper:
        return ordered[int(index)]
    weight = index - lower
    return ordered[lower] * (1.0 - weight) + ordered[upper] * weight


def confidence_interval_mean(values: list[float]) -> tuple[float, float, float, float]:
    n = len(values)
    if n == 0:
        return float("nan"), float("nan"), float("nan"), float("nan")
    estimate = mean(values)
    sd = pstdev(values) if n > 1 else 0.0
    se = sd / math.sqrt(n) if n > 1 else 0.0
    return estimate, se, estimate - 1.96 * se, estimate + 1.96 * se


def monte_carlo_pi(samples: int, seed: int) -> dict[str, object]:
    rng = random.Random(seed)
    inside = 0
    scaled_indicator_values: list[float] = []
    for _ in range(samples):
        x = rng.random()
        y = rng.random()
        indicator = 1.0 if x * x + y * y <= 1.0 else 0.0
        inside += int(indicator)
        scaled_indicator_values.append(4.0 * indicator)
    estimate, se, lower, upper = confidence_interval_mean(scaled_indicator_values)
    row = asdict(MonteCarloEstimate(
        experiment="pi_area_ratio",
        samples=samples,
        seed=seed,
        estimate=round(estimate, 10),
        standard_error=round(se, 10),
        lower_95=round(lower, 10),
        upper_95=round(upper, 10),
        interpretation="Pi is estimated by sampling points in a square and counting the fraction inside a quarter circle."
    ))
    row.update({
        "reference_value": round(math.pi, 10),
        "absolute_error": round(abs(estimate - math.pi), 10),
        "inside_count": inside,
    })
    return row


def project_cost_trial(rng: random.Random) -> float:
    base_cost = rng.triangular(900_000.0, 1_100_000.0, 1_000_000.0)
    labor_multiplier = max(0.75, rng.gauss(1.0, 0.08))
    delay_cost = max(0.0, rng.gauss(60_000.0, 35_000.0))
    contingency = rng.uniform(20_000.0, 120_000.0)
    return base_cost * labor_multiplier + delay_cost + contingency


def project_cost_risk(samples: int, seed: int, threshold: float = 1_250_000.0) -> tuple[dict[str, object], list[dict[str, object]]]:
    rng = random.Random(seed)
    costs: list[float] = []
    exceedances: list[float] = []
    trial_rows: list[dict[str, object]] = []
    for trial in range(1, samples + 1):
        cost = project_cost_trial(rng)
        exceeds = 1.0 if cost > threshold else 0.0
        costs.append(cost)
        exceedances.append(exceeds)
        if trial <= 500:
            trial_rows.append({
                "experiment": "project_cost_risk",
                "seed": seed,
                "trial": trial,
                "cost": round(cost, 2),
                "threshold": threshold,
                "exceeds_threshold": int(exceeds),
            })
    mean_cost, mean_se, mean_lower, mean_upper = confidence_interval_mean(costs)
    risk, risk_se, risk_lower, risk_upper = confidence_interval_mean(exceedances)
    summary = {
        "experiment": "project_cost_risk",
        "samples": samples,
        "seed": seed,
        "mean_cost": round(mean_cost, 2),
        "mean_cost_standard_error": round(mean_se, 2),
        "mean_cost_lower_95": round(mean_lower, 2),
        "mean_cost_upper_95": round(mean_upper, 2),
        "threshold": threshold,
        "threshold_probability": round(risk, 6),
        "threshold_probability_standard_error": round(risk_se, 6),
        "threshold_probability_lower_95": round(risk_lower, 6),
        "threshold_probability_upper_95": round(risk_upper, 6),
        "cost_p05": round(percentile(costs, 0.05), 2),
        "cost_p50": round(percentile(costs, 0.50), 2),
        "cost_p95": round(percentile(costs, 0.95), 2),
        "interpretation": "Monte Carlo cost simulation estimates both expected cost and probability of threshold exceedance.",
    }
    return summary, trial_rows


def uncertainty_propagation_trial(rng: random.Random) -> dict[str, float]:
    input_a = rng.gauss(10.0, 1.5)
    input_b = rng.uniform(2.0, 5.0)
    input_c = rng.triangular(0.8, 1.4, 1.0)
    output = input_c * (input_a ** 2) / input_b
    return {"input_a": input_a, "input_b": input_b, "input_c": input_c, "output": output}


def uncertainty_propagation(samples: int, seed: int) -> tuple[dict[str, object], list[dict[str, object]]]:
    rng = random.Random(seed)
    outputs: list[float] = []
    rows: list[dict[str, object]] = []
    for trial in range(1, samples + 1):
        result = uncertainty_propagation_trial(rng)
        outputs.append(result["output"])
        if trial <= 500:
            rows.append({
                "experiment": "uncertainty_propagation",
                "seed": seed,
                "trial": trial,
                "input_a": round(result["input_a"], 6),
                "input_b": round(result["input_b"], 6),
                "input_c": round(result["input_c"], 6),
                "output": round(result["output"], 6),
            })
    estimate, se, lower, upper = confidence_interval_mean(outputs)
    summary = {
        "experiment": "uncertainty_propagation",
        "samples": samples,
        "seed": seed,
        "mean_output": round(estimate, 6),
        "standard_error": round(se, 6),
        "lower_95": round(lower, 6),
        "upper_95": round(upper, 6),
        "output_p05": round(percentile(outputs, 0.05), 6),
        "output_p50": round(percentile(outputs, 0.50), 6),
        "output_p95": round(percentile(outputs, 0.95), 6),
        "interpretation": "Input uncertainty is propagated through a nonlinear model to estimate the output distribution.",
    }
    return summary, rows


def convergence_study() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for samples in [100, 500, 1000, 5000, 10000, 50000]:
        pi_estimates: list[float] = []
        risk_estimates: list[float] = []
        for seed in range(1, 11):
            pi_row = monte_carlo_pi(samples, seed)
            pi_estimates.append(float(pi_row["estimate"]))
            risk_summary, _ = project_cost_risk(samples, seed)
            risk_estimates.append(float(risk_summary["threshold_probability"]))
        rows.append({
            "samples": samples,
            "pi_mean_estimate": round(mean(pi_estimates), 10),
            "pi_run_to_run_std": round(pstdev(pi_estimates), 10),
            "pi_mean_absolute_error": round(mean(abs(value - math.pi) for value in pi_estimates), 10),
            "threshold_probability_mean": round(mean(risk_estimates), 6),
            "threshold_probability_run_to_run_std": round(pstdev(risk_estimates), 6),
            "seeds": len(pi_estimates),
            "interpretation": "Convergence should be assessed across sample sizes and repeated seeds.",
        })
    return rows


def monte_carlo_review_checklist() -> list[dict[str, object]]:
    return [
        {"check": "quantity_of_interest_defined", "status": "complete", "question": "Is the estimated probability, expectation, quantile, risk, or distribution clearly stated?"},
        {"check": "input_distributions_documented", "status": "complete", "question": "Are uncertain inputs, distributions, parameters, and sources documented?"},
        {"check": "dependencies_reviewed", "status": "partial", "question": "Are correlations or dependencies among uncertain inputs considered?"},
        {"check": "sample_size_justified", "status": "complete", "question": "Is the number of trials justified by convergence or uncertainty requirements?"},
        {"check": "random_seed_recorded", "status": "complete", "question": "Are random seeds and generator assumptions documented?"},
        {"check": "sampling_error_reported", "status": "complete", "question": "Are standard errors, confidence intervals, or repeated-seed diagnostics reported?"},
        {"check": "tail_risk_reviewed", "status": "partial", "question": "Are rare, extreme, or threshold outcomes adequately sampled and communicated?"},
        {"check": "interpretation_limits_stated", "status": "complete", "question": "Are results described as conditional on assumptions rather than direct prediction?"},
    ]


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


def summarize(pi_rows: list[dict[str, object]], cost_summary: dict[str, object], propagation_summary: dict[str, object], convergence_rows: list[dict[str, object]], checklist_rows: list[dict[str, object]]) -> dict[str, object]:
    latest = convergence_rows[-1]
    review_attention = sum(1 for row in checklist_rows if row["status"] in {"partial", "needs_review"})
    return {
        "pi_experiments": len(pi_rows),
        "largest_convergence_sample_size": latest["samples"],
        "pi_mean_absolute_error_at_largest_sample_size": latest["pi_mean_absolute_error"],
        "project_cost_mean": cost_summary["mean_cost"],
        "project_cost_threshold_probability": cost_summary["threshold_probability"],
        "uncertainty_propagation_mean_output": propagation_summary["mean_output"],
        "uncertainty_propagation_p05": propagation_summary["output_p05"],
        "uncertainty_propagation_p95": propagation_summary["output_p95"],
        "review_items_needing_attention": review_attention,
        "interpretation": "Monte Carlo workflows estimate uncertainty through repeated sampling and require distribution review, convergence diagnostics, sampling-error reporting, reproducibility records, and interpretation limits.",
    }


def main() -> None:
    pi_rows = [monte_carlo_pi(samples, seed=42) for samples in [100, 1000, 10000, 50000]]
    cost_summary, cost_trials = project_cost_risk(samples=20000, seed=1001)
    propagation_summary, propagation_trials = uncertainty_propagation(samples=20000, seed=2002)
    convergence_rows = convergence_study()
    checklist_rows = monte_carlo_review_checklist()
    summary = summarize(pi_rows, cost_summary, propagation_summary, convergence_rows, checklist_rows)

    write_csv(TABLES / "monte_carlo_pi_estimates.csv", pi_rows)
    write_csv(TABLES / "project_cost_risk_summary.csv", [cost_summary])
    write_csv(TABLES / "project_cost_risk_trial_sample.csv", cost_trials)
    write_csv(TABLES / "uncertainty_propagation_summary.csv", [propagation_summary])
    write_csv(TABLES / "uncertainty_propagation_trial_sample.csv", propagation_trials)
    write_csv(TABLES / "monte_carlo_convergence_study.csv", convergence_rows)
    write_csv(TABLES / "monte_carlo_review_checklist.csv", checklist_rows)
    write_csv(TABLES / "monte_carlo_uncertainty_audit_summary.csv", [summary])

    write_json(JSON_DIR / "monte_carlo_pi_estimates.json", pi_rows)
    write_json(JSON_DIR / "project_cost_risk_summary.json", cost_summary)
    write_json(JSON_DIR / "project_cost_risk_trial_sample.json", cost_trials)
    write_json(JSON_DIR / "uncertainty_propagation_summary.json", propagation_summary)
    write_json(JSON_DIR / "uncertainty_propagation_trial_sample.json", propagation_trials)
    write_json(JSON_DIR / "monte_carlo_convergence_study.json", convergence_rows)
    write_json(JSON_DIR / "monte_carlo_review_checklist.json", checklist_rows)
    write_json(JSON_DIR / "monte_carlo_uncertainty_audit_summary.json", summary)

    print("Monte Carlo methods and computational uncertainty audit complete.")
    print(TABLES / "monte_carlo_uncertainty_audit_summary.csv")


if __name__ == "__main__":
    main()
