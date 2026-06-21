#!/usr/bin/env python3
"""Dependency-light sensitivity analysis audit for algorithms and models."""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
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
LOGS = ARTICLE_ROOT / "outputs" / "logs"


@dataclass(frozen=True)
class ModelConfig:
    name: str
    demand_growth: float
    capacity_investment: float
    failure_rate: float
    adaptation_rate: float
    threshold: float
    noise_scale: float
    seed: int


def timestamp_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def run_model(config: ModelConfig, periods: int = 40) -> dict[str, object]:
    rng = random.Random(config.seed)
    pressure = 0.45 + config.demand_growth * 0.20 - config.capacity_investment * 0.12
    resilience = 0.55 + config.capacity_investment * 0.18 + config.adaptation_rate * 0.12
    cumulative_risk = 0.0
    threshold_crossings = 0

    for _period in range(1, periods + 1):
        shock = rng.gauss(0.0, config.noise_scale)
        pressure = clamp(
            pressure
            + config.demand_growth * 0.018
            + config.failure_rate * 0.030
            - config.adaptation_rate * 0.014
            + shock,
            0.0,
            1.5,
        )
        resilience = clamp(
            resilience
            + config.capacity_investment * 0.010
            + config.adaptation_rate * 0.012
            - config.failure_rate * 0.006,
            0.0,
            1.5,
        )
        risk = clamp(pressure - resilience + 0.50, 0.0, 1.0)
        cumulative_risk += risk
        if risk >= config.threshold:
            threshold_crossings += 1

    average_risk = cumulative_risk / periods
    stability_margin = config.threshold - average_risk

    return {
        "name": config.name,
        "seed": config.seed,
        "demand_growth": config.demand_growth,
        "capacity_investment": config.capacity_investment,
        "failure_rate": config.failure_rate,
        "adaptation_rate": config.adaptation_rate,
        "threshold": config.threshold,
        "noise_scale": config.noise_scale,
        "periods": periods,
        "average_risk": round(average_risk, 6),
        "threshold_crossings": threshold_crossings,
        "stability_margin": round(stability_margin, 6),
        "interpretation": "Outputs depend on demand, capacity, failure, adaptation, threshold, noise, and random seed.",
    }


def baseline_config() -> ModelConfig:
    return ModelConfig(
        name="baseline",
        demand_growth=0.45,
        capacity_investment=0.35,
        failure_rate=0.25,
        adaptation_rate=0.30,
        threshold=0.60,
        noise_scale=0.015,
        seed=2026,
    )


def one_at_a_time_sweeps(base: ModelConfig) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    parameter_values = {
        "demand_growth": [0.20, 0.35, 0.45, 0.60, 0.75],
        "capacity_investment": [0.10, 0.25, 0.35, 0.50, 0.70],
        "failure_rate": [0.05, 0.15, 0.25, 0.40, 0.60],
        "adaptation_rate": [0.05, 0.20, 0.30, 0.45, 0.65],
        "noise_scale": [0.000, 0.010, 0.015, 0.030, 0.050],
    }

    for parameter, values in parameter_values.items():
        for value in values:
            updated = replace(base, name=f"oat_{parameter}_{value}", **{parameter: value})
            result = run_model(updated)
            result["sweep_type"] = "one_at_a_time"
            result["varied_parameter"] = parameter
            result["varied_value"] = value
            rows.append(result)

    return rows


def scenario_runs(base: ModelConfig) -> list[dict[str, object]]:
    scenarios = [
        replace(base, name="baseline"),
        replace(base, name="high_demand", demand_growth=0.75),
        replace(base, name="low_capacity", capacity_investment=0.10),
        replace(base, name="high_failure", failure_rate=0.60),
        replace(base, name="rapid_adaptation", adaptation_rate=0.65),
        replace(base, name="stress_case", demand_growth=0.80, capacity_investment=0.10, failure_rate=0.65, adaptation_rate=0.10),
        replace(base, name="resilience_case", demand_growth=0.30, capacity_investment=0.70, failure_rate=0.10, adaptation_rate=0.70),
    ]

    rows: list[dict[str, object]] = []
    for scenario in scenarios:
        result = run_model(scenario)
        result["sweep_type"] = "scenario"
        rows.append(result)
    return rows


def threshold_sweep(base: ModelConfig) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for threshold in [0.35, 0.45, 0.55, 0.60, 0.65, 0.75, 0.85]:
        updated = replace(base, name=f"threshold_{threshold}", threshold=threshold)
        result = run_model(updated)
        result["sweep_type"] = "threshold_sweep"
        result["varied_parameter"] = "threshold"
        result["varied_value"] = threshold
        rows.append(result)
    return rows


def repeated_seed_runs(base: ModelConfig) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for seed in range(1, 41):
        updated = replace(base, name="seed_ensemble", seed=seed)
        result = run_model(updated)
        result["sweep_type"] = "seed_ensemble"
        rows.append(result)
    return rows


def influence_ranking(oat_rows: list[dict[str, object]], base_result: dict[str, object]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    base_risk = float(base_result["average_risk"])

    for parameter in sorted(set(str(row["varied_parameter"]) for row in oat_rows)):
        subset = [row for row in oat_rows if row["varied_parameter"] == parameter]
        risks = [float(row["average_risk"]) for row in subset]
        crossings = [float(row["threshold_crossings"]) for row in subset]
        rows.append(
            {
                "parameter": parameter,
                "tested_values": len(subset),
                "min_average_risk": round(min(risks), 6),
                "max_average_risk": round(max(risks), 6),
                "risk_range": round(max(risks) - min(risks), 6),
                "max_absolute_change_from_baseline": round(max(abs(value - base_risk) for value in risks), 6),
                "threshold_crossing_range": round(max(crossings) - min(crossings), 6),
                "interpretation": "Larger ranges indicate stronger influence on outputs across tested values.",
            }
        )

    rows.sort(key=lambda row: float(row["risk_range"]), reverse=True)
    return rows


def robustness_summary(all_rows: list[dict[str, object]]) -> dict[str, object]:
    risks = [float(row["average_risk"]) for row in all_rows]
    crossings = [float(row["threshold_crossings"]) for row in all_rows]
    high_risk_runs = [row for row in all_rows if float(row["average_risk"]) >= float(row["threshold"])]
    return {
        "runs_reviewed": len(all_rows),
        "min_average_risk": round(min(risks), 6),
        "max_average_risk": round(max(risks), 6),
        "mean_average_risk": round(mean(risks), 6),
        "std_average_risk": round(pstdev(risks), 6),
        "min_threshold_crossings": int(min(crossings)),
        "max_threshold_crossings": int(max(crossings)),
        "high_risk_run_count": len(high_risk_runs),
        "high_risk_run_share": round(len(high_risk_runs) / len(all_rows), 6),
        "interpretation": "Robustness review compares whether conclusions remain stable across sweeps, scenarios, thresholds, and seeds.",
    }


def review_checklist() -> list[dict[str, object]]:
    return [
        {"check": "baseline_defined", "status": "complete", "question": "Is the reference case documented?"},
        {"check": "parameters_identified", "status": "complete", "question": "Are inputs, parameters, thresholds, and assumptions listed?"},
        {"check": "ranges_justified", "status": "partial", "question": "Are tested ranges tied to evidence, uncertainty, or plausible scenarios?"},
        {"check": "one_at_a_time_sweep_completed", "status": "complete", "question": "Was a first-pass parameter sweep performed?"},
        {"check": "scenario_comparison_completed", "status": "complete", "question": "Were structured scenarios compared?"},
        {"check": "threshold_sensitivity_completed", "status": "complete", "question": "Were decision cutoffs tested?"},
        {"check": "seed_sensitivity_completed", "status": "complete", "question": "Were stochastic runs repeated across seeds?"},
        {"check": "structural_sensitivity_reviewed", "status": "needs_review", "question": "Were alternative model structures compared?"},
        {"check": "governance_implications_documented", "status": "partial", "question": "Are sensitivity findings tied to monitoring, use limits, or decision governance?"},
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


def main() -> None:
    LOGS.mkdir(parents=True, exist_ok=True)
    base = baseline_config()
    base_result = run_model(base)
    oat_rows = one_at_a_time_sweeps(base)
    scenario_rows = scenario_runs(base)
    threshold_rows = threshold_sweep(base)
    seed_rows = repeated_seed_runs(base)
    influence_rows = influence_ranking(oat_rows, base_result)
    all_run_rows = [base_result] + oat_rows + scenario_rows + threshold_rows + seed_rows
    robustness = robustness_summary(all_run_rows)
    checklist_rows = review_checklist()

    audit_summary = {
        "article": "sensitivity_analysis_for_algorithms_and_models",
        "timestamp_utc": timestamp_utc(),
        "baseline_average_risk": base_result["average_risk"],
        "baseline_threshold_crossings": base_result["threshold_crossings"],
        "most_influential_parameter": influence_rows[0]["parameter"],
        "most_influential_parameter_risk_range": influence_rows[0]["risk_range"],
        "runs_reviewed": robustness["runs_reviewed"],
        "high_risk_run_share": robustness["high_risk_run_share"],
        "review_items_needing_attention": sum(1 for row in checklist_rows if row["status"] in {"partial", "needs_review"}),
        "interpretation": "Sensitivity analysis identifies which assumptions drive results, which conclusions remain robust, and which choices require governance review.",
    }

    write_csv(TABLES / "baseline_result.csv", [base_result])
    write_csv(TABLES / "one_at_a_time_sensitivity.csv", oat_rows)
    write_csv(TABLES / "scenario_sensitivity.csv", scenario_rows)
    write_csv(TABLES / "threshold_sensitivity.csv", threshold_rows)
    write_csv(TABLES / "seed_sensitivity.csv", seed_rows)
    write_csv(TABLES / "parameter_influence_ranking.csv", influence_rows)
    write_csv(TABLES / "robustness_summary.csv", [robustness])
    write_csv(TABLES / "sensitivity_review_checklist.csv", checklist_rows)
    write_csv(TABLES / "sensitivity_analysis_audit_summary.csv", [audit_summary])

    write_json(JSON_DIR / "baseline_config.json", asdict(base))
    write_json(JSON_DIR / "baseline_result.json", base_result)
    write_json(JSON_DIR / "one_at_a_time_sensitivity.json", oat_rows)
    write_json(JSON_DIR / "scenario_sensitivity.json", scenario_rows)
    write_json(JSON_DIR / "threshold_sensitivity.json", threshold_rows)
    write_json(JSON_DIR / "seed_sensitivity.json", seed_rows)
    write_json(JSON_DIR / "parameter_influence_ranking.json", influence_rows)
    write_json(JSON_DIR / "robustness_summary.json", robustness)
    write_json(JSON_DIR / "sensitivity_review_checklist.json", checklist_rows)
    write_json(JSON_DIR / "sensitivity_analysis_audit_summary.json", audit_summary)

    (LOGS / "sensitivity_analysis_run.log").write_text(
        f"{timestamp_utc()} | sensitivity analysis audit complete\n", encoding="utf-8"
    )
    print("Sensitivity analysis audit complete.")
    print(TABLES / "sensitivity_analysis_audit_summary.csv")


if __name__ == "__main__":
    main()
