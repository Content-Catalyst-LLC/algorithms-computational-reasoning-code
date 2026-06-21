#!/usr/bin/env python3
"""
Dependency-light workflow for uncertainty inventory, propagation,
intervals, ensemble summaries, threshold exceedance, and audit trails.
"""

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
class UQConfig:
    experiment_name: str
    seed: int
    ensemble_size: int
    threshold: float
    baseline_demand: float
    baseline_capacity: float
    baseline_failure_rate: float
    baseline_adaptation_rate: float


@dataclass(frozen=True)
class UncertainInput:
    name: str
    center: float
    spread: float
    distribution: str
    source: str
    interpretation: str


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


def quantile(values: list[float], q: float) -> float:
    if not values:
        raise ValueError("Cannot compute quantile of an empty list.")
    ordered = sorted(values)
    position = (len(ordered) - 1) * q
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[int(position)]
    weight = position - lower
    return ordered[lower] * (1.0 - weight) + ordered[upper] * weight


def default_config() -> UQConfig:
    return UQConfig(
        experiment_name="uncertainty_quantification_computational_workflows",
        seed=2026,
        ensemble_size=3000,
        threshold=0.62,
        baseline_demand=0.55,
        baseline_capacity=0.50,
        baseline_failure_rate=0.22,
        baseline_adaptation_rate=0.30,
    )


def uncertainty_inventory(config: UQConfig) -> list[UncertainInput]:
    return [
        UncertainInput("demand", config.baseline_demand, 0.12, "bounded_normal", "forecast_input", "Future demand is uncertain and affects system pressure."),
        UncertainInput("capacity", config.baseline_capacity, 0.10, "bounded_normal", "planning_assumption", "Available capacity is uncertain because staffing, infrastructure, and resources vary."),
        UncertainInput("failure_rate", config.baseline_failure_rate, 0.08, "bounded_normal", "estimated_parameter", "Failure rate is estimated from limited evidence and may shift under stress."),
        UncertainInput("adaptation_rate", config.baseline_adaptation_rate, 0.10, "bounded_normal", "behavioral_parameter", "Adaptation rate represents uncertain response and learning behavior."),
        UncertainInput("measurement_noise", 0.00, 0.035, "normal", "measurement_error", "Measurement and reporting noise affect observed signals."),
    ]


def bounded_normal(rng: random.Random, center: float, spread: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, rng.gauss(center, spread)))


def sample_uncertain_inputs(rng: random.Random, inventory: list[UncertainInput]) -> dict[str, float]:
    sample: dict[str, float] = {}
    for item in inventory:
        if item.distribution == "bounded_normal":
            sample[item.name] = bounded_normal(rng, item.center, item.spread)
        elif item.distribution == "normal":
            sample[item.name] = rng.gauss(item.center, item.spread)
        else:
            raise ValueError(f"Unsupported distribution: {item.distribution}")
    return sample


def computational_model(sample: dict[str, float]) -> float:
    risk_score = (
        0.42
        + 0.38 * sample["demand"]
        - 0.31 * sample["capacity"]
        + 0.27 * sample["failure_rate"]
        - 0.18 * sample["adaptation_rate"]
        + sample["measurement_noise"]
    )
    return max(0.0, min(1.0, risk_score))


def run_uncertainty_ensemble(config: UQConfig) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    rng = random.Random(config.seed)
    inventory = uncertainty_inventory(config)
    rows: list[dict[str, object]] = []
    for run_id in range(1, config.ensemble_size + 1):
        sample = sample_uncertain_inputs(rng, inventory)
        output = computational_model(sample)
        rows.append({
            "experiment_name": config.experiment_name,
            "run_id": run_id,
            "seed": config.seed,
            "demand": round(sample["demand"], 6),
            "capacity": round(sample["capacity"], 6),
            "failure_rate": round(sample["failure_rate"], 6),
            "adaptation_rate": round(sample["adaptation_rate"], 6),
            "measurement_noise": round(sample["measurement_noise"], 6),
            "risk_score": round(output, 6),
            "threshold": config.threshold,
            "exceeds_threshold": int(output >= config.threshold),
        })
    return rows, [asdict(item) for item in inventory]


def summarize_outputs(rows: list[dict[str, object]]) -> dict[str, object]:
    values = [float(row["risk_score"]) for row in rows]
    threshold = float(rows[0]["threshold"])
    exceed = [int(row["exceeds_threshold"]) for row in rows]
    return {
        "runs": len(rows),
        "threshold": threshold,
        "mean_risk_score": round(mean(values), 6),
        "std_risk_score": round(pstdev(values), 6),
        "min_risk_score": round(min(values), 6),
        "p05_risk_score": round(quantile(values, 0.05), 6),
        "p25_risk_score": round(quantile(values, 0.25), 6),
        "median_risk_score": round(quantile(values, 0.50), 6),
        "p75_risk_score": round(quantile(values, 0.75), 6),
        "p95_risk_score": round(quantile(values, 0.95), 6),
        "max_risk_score": round(max(values), 6),
        "threshold_exceedance_probability": round(sum(exceed) / len(exceed), 6),
        "interpretation": "The ensemble summarizes output uncertainty from sampled inputs, parameters, and measurement noise.",
    }


def correlation(xs: list[float], ys: list[float]) -> float:
    xbar = mean(xs)
    ybar = mean(ys)
    numerator = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys))
    xden = math.sqrt(sum((x - xbar) ** 2 for x in xs))
    yden = math.sqrt(sum((y - ybar) ** 2 for y in ys))
    if xden == 0 or yden == 0:
        return 0.0
    return numerator / (xden * yden)


def source_influence(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    output_values = [float(row["risk_score"]) for row in rows]
    input_names = ["demand", "capacity", "failure_rate", "adaptation_rate", "measurement_noise"]
    influence_rows: list[dict[str, object]] = []
    for name in input_names:
        input_values = [float(row[name]) for row in rows]
        corr = correlation(input_values, output_values)
        influence_rows.append({
            "uncertainty_source": name,
            "correlation_with_output": round(corr, 6),
            "absolute_correlation": round(abs(corr), 6),
            "input_min": round(min(input_values), 6),
            "input_max": round(max(input_values), 6),
            "input_std": round(pstdev(input_values), 6),
            "interpretation": "Higher absolute correlation indicates stronger association with output uncertainty in this audit.",
        })
    influence_rows.sort(key=lambda row: float(row["absolute_correlation"]), reverse=True)
    return influence_rows


def interval_coverage_check(rows: list[dict[str, object]], summary: dict[str, object]) -> dict[str, object]:
    values = [float(row["risk_score"]) for row in rows]
    lower = float(summary["p05_risk_score"])
    upper = float(summary["p95_risk_score"])
    inside = [1 for value in values if lower <= value <= upper]
    return {
        "interval_type": "central_90_percent_empirical_interval",
        "lower_bound": lower,
        "upper_bound": upper,
        "empirical_coverage": round(sum(inside) / len(values), 6),
        "interpretation": "Empirical ensemble coverage checks whether the reported interval matches the generated distribution.",
    }


def threshold_margin_summary(rows: list[dict[str, object]]) -> dict[str, object]:
    threshold = float(rows[0]["threshold"])
    values = [float(row["risk_score"]) for row in rows]
    near = [value for value in values if abs(value - threshold) <= 0.03]
    return {
        "threshold": threshold,
        "near_threshold_margin": 0.03,
        "near_threshold_count": len(near),
        "near_threshold_share": round(len(near) / len(values), 6),
        "interpretation": "Near-threshold cases may require caution because small uncertainty can change decision categories.",
    }


def review_checklist() -> list[dict[str, object]]:
    return [
        {"check": "uncertainty_inventory_created", "status": "complete", "question": "Are major uncertainty sources listed and described?"},
        {"check": "uncertainty_ranges_documented", "status": "partial", "question": "Are uncertainty ranges tied to evidence, calibration, or expert review?"},
        {"check": "propagation_method_documented", "status": "complete", "question": "Is the propagation method described?"},
        {"check": "ensemble_size_recorded", "status": "complete", "question": "Is the number of simulation runs recorded?"},
        {"check": "threshold_exceedance_reported", "status": "complete", "question": "Is decision-relevant threshold probability reported?"},
        {"check": "influential_sources_identified", "status": "complete", "question": "Are the main contributors to output uncertainty identified?"},
        {"check": "structural_uncertainty_reviewed", "status": "needs_review", "question": "Are alternative model structures compared?"},
        {"check": "uncertainty_communication_reviewed", "status": "partial", "question": "Are uncertainty summaries explained in plain language for intended users?"},
        {"check": "governance_implications_documented", "status": "partial", "question": "Are uncertainty findings tied to use limits, review triggers, or decision safeguards?"},
    ]


def main() -> None:
    config = default_config()
    ensemble_rows, inventory_rows = run_uncertainty_ensemble(config)
    summary = summarize_outputs(ensemble_rows)
    influence_rows = source_influence(ensemble_rows)
    coverage = interval_coverage_check(ensemble_rows, summary)
    threshold_margin = threshold_margin_summary(ensemble_rows)
    checklist_rows = review_checklist()
    audit_summary = {
        "article": "uncertainty_quantification_in_computational_workflows",
        "timestamp_utc": timestamp_utc(),
        "ensemble_size": config.ensemble_size,
        "mean_risk_score": summary["mean_risk_score"],
        "p05_risk_score": summary["p05_risk_score"],
        "p95_risk_score": summary["p95_risk_score"],
        "threshold": config.threshold,
        "threshold_exceedance_probability": summary["threshold_exceedance_probability"],
        "most_influential_uncertainty_source": influence_rows[0]["uncertainty_source"],
        "near_threshold_share": threshold_margin["near_threshold_share"],
        "review_items_needing_attention": sum(1 for row in checklist_rows if row["status"] in {"partial", "needs_review"}),
        "interpretation": "Uncertainty quantification supports responsible computational reasoning by documenting sources, propagation, intervals, exceedance probabilities, influential uncertainties, and governance implications.",
    }

    write_csv(TABLES / "uncertainty_inventory.csv", inventory_rows)
    write_csv(TABLES / "uncertainty_ensemble_runs.csv", ensemble_rows)
    write_csv(TABLES / "uncertainty_output_summary.csv", [summary])
    write_csv(TABLES / "uncertainty_source_influence.csv", influence_rows)
    write_csv(TABLES / "interval_coverage_check.csv", [coverage])
    write_csv(TABLES / "threshold_margin_summary.csv", [threshold_margin])
    write_csv(TABLES / "uncertainty_review_checklist.csv", checklist_rows)
    write_csv(TABLES / "uncertainty_quantification_audit_summary.csv", [audit_summary])

    write_json(JSON_DIR / "uq_config.json", asdict(config))
    write_json(JSON_DIR / "uncertainty_inventory.json", inventory_rows)
    write_json(JSON_DIR / "uncertainty_ensemble_runs.json", ensemble_rows)
    write_json(JSON_DIR / "uncertainty_output_summary.json", summary)
    write_json(JSON_DIR / "uncertainty_source_influence.json", influence_rows)
    write_json(JSON_DIR / "interval_coverage_check.json", coverage)
    write_json(JSON_DIR / "threshold_margin_summary.json", threshold_margin)
    write_json(JSON_DIR / "uncertainty_review_checklist.json", checklist_rows)
    write_json(JSON_DIR / "uncertainty_quantification_audit_summary.json", audit_summary)

    print("Uncertainty quantification audit complete.")
    print(TABLES / "uncertainty_quantification_audit_summary.csv")


if __name__ == "__main__":
    main()
