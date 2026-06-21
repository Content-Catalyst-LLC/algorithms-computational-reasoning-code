from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean, pstdev
import csv
import hashlib
import json
import platform
import random
import sys
from datetime import datetime, timezone

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ARTICLE_ROOT / "data"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"
LOGS = ARTICLE_ROOT / "outputs" / "logs"


@dataclass(frozen=True)
class ExperimentConfig:
    experiment_name: str
    scenario: str
    seed: int
    sample_size: int
    treatment_effect: float
    noise_scale: float
    threshold: float
    notes: str


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


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()


def generate_synthetic_data(config: ExperimentConfig) -> list[dict[str, object]]:
    rng = random.Random(config.seed)
    rows: list[dict[str, object]] = []
    for unit_id in range(1, config.sample_size + 1):
        baseline = rng.gauss(50.0, 10.0)
        treatment = 1 if rng.random() < 0.5 else 0
        noise = rng.gauss(0.0, config.noise_scale)
        outcome = baseline + treatment * config.treatment_effect + noise
        rows.append({
            "experiment_name": config.experiment_name,
            "scenario": config.scenario,
            "seed": config.seed,
            "unit_id": unit_id,
            "baseline": round(baseline, 6),
            "treatment": treatment,
            "outcome": round(outcome, 6),
            "threshold": config.threshold,
            "above_threshold": int(outcome >= config.threshold),
        })
    return rows


def analyze_experiment(rows: list[dict[str, object]], config: ExperimentConfig) -> dict[str, object]:
    treatment_outcomes = [float(row["outcome"]) for row in rows if int(row["treatment"]) == 1]
    control_outcomes = [float(row["outcome"]) for row in rows if int(row["treatment"]) == 0]
    all_outcomes = [float(row["outcome"]) for row in rows]
    threshold_hits = [int(row["above_threshold"]) for row in rows]
    treatment_mean = mean(treatment_outcomes)
    control_mean = mean(control_outcomes)
    estimated_effect = treatment_mean - control_mean
    return {
        "experiment_name": config.experiment_name,
        "scenario": config.scenario,
        "seed": config.seed,
        "sample_size": config.sample_size,
        "treatment_effect_parameter": config.treatment_effect,
        "noise_scale": config.noise_scale,
        "threshold": config.threshold,
        "mean_outcome": round(mean(all_outcomes), 6),
        "std_outcome": round(pstdev(all_outcomes), 6),
        "treatment_mean": round(treatment_mean, 6),
        "control_mean": round(control_mean, 6),
        "estimated_effect": round(estimated_effect, 6),
        "threshold_rate": round(sum(threshold_hits) / len(threshold_hits), 6),
        "interpretation": "Scenario output depends on preserved data, parameters, seed, code, and runtime context.",
    }


def scenario_configs() -> list[ExperimentConfig]:
    return [
        ExperimentConfig("reproducible_scenario_experiment", "baseline", 101, 1000, 2.0, 6.0, 60.0, "Baseline scenario."),
        ExperimentConfig("reproducible_scenario_experiment", "higher_effect", 101, 1000, 5.0, 6.0, 60.0, "Changes treatment effect only."),
        ExperimentConfig("reproducible_scenario_experiment", "higher_noise", 101, 1000, 2.0, 12.0, 60.0, "Changes noise only."),
        ExperimentConfig("reproducible_scenario_experiment", "threshold_stress", 101, 1000, 2.0, 6.0, 70.0, "Changes decision threshold only."),
    ]


def sensitivity_runs() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for effect in [0.0, 1.0, 2.0, 4.0, 8.0]:
        for seed in range(1, 11):
            config = ExperimentConfig(
                "effect_sensitivity_experiment",
                f"effect_{effect}",
                seed,
                800,
                effect,
                8.0,
                60.0,
                "Sensitivity run varying treatment effect across repeated seeds.",
            )
            rows.append(analyze_experiment(generate_synthetic_data(config), config))

    aggregated: list[dict[str, object]] = []
    for effect in sorted(set(float(row["treatment_effect_parameter"]) for row in rows)):
        subset = [row for row in rows if float(row["treatment_effect_parameter"]) == effect]
        estimated_effects = [float(row["estimated_effect"]) for row in subset]
        threshold_rates = [float(row["threshold_rate"]) for row in subset]
        aggregated.append({
            "treatment_effect_parameter": effect,
            "runs": len(subset),
            "mean_estimated_effect": round(mean(estimated_effects), 6),
            "std_estimated_effect": round(pstdev(estimated_effects), 6),
            "mean_threshold_rate": round(mean(threshold_rates), 6),
            "std_threshold_rate": round(pstdev(threshold_rates), 6),
            "interpretation": "Repeated-seed sensitivity runs show how outputs change across parameter values.",
        })
    return aggregated


def workflow_checklist() -> list[dict[str, object]]:
    return [
        {"check": "question_defined", "status": "complete", "question": "Is the computational experiment tied to an explicit question?"},
        {"check": "raw_data_preserved", "status": "complete", "question": "Are raw or generated inputs preserved separately from processed outputs?"},
        {"check": "parameters_recorded", "status": "complete", "question": "Are scenario parameters, thresholds, and sample sizes recorded?"},
        {"check": "random_seed_recorded", "status": "complete", "question": "Are stochastic seeds recorded for reproducibility?"},
        {"check": "environment_recorded", "status": "complete", "question": "Is runtime environment information captured?"},
        {"check": "outputs_linked_to_inputs", "status": "complete", "question": "Are output files linked to data, code, and parameters?"},
        {"check": "sensitivity_analysis_included", "status": "complete", "question": "Are key assumptions varied and compared?"},
        {"check": "validation_evidence_included", "status": "partial", "question": "Are results checked against theory, benchmarks, observed data, or expert expectations?"},
        {"check": "interpretation_limits_stated", "status": "complete", "question": "Are limitations and intended-use boundaries documented?"},
    ]


def collect_file_manifest(paths: list[Path]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for path in paths:
        if path.exists() and path.is_file():
            rows.append({
                "relative_path": str(path.relative_to(ARTICLE_ROOT)),
                "size_bytes": path.stat().st_size,
                "sha256": file_sha256(path),
            })
    return rows


def runtime_environment() -> dict[str, object]:
    return {
        "python_version": sys.version,
        "platform": platform.platform(),
        "processor": platform.processor(),
        "machine": platform.machine(),
        "timestamp_utc": timestamp_utc(),
    }


def main() -> None:
    LOGS.mkdir(parents=True, exist_ok=True)
    run_log = LOGS / "reproducible_workflow_run.log"
    log_rows: list[str] = []

    def log(message: str) -> None:
        line = f"{timestamp_utc()} | {message}"
        log_rows.append(line)
        print(line)

    log("Starting reproducible workflow audit.")
    configs = scenario_configs()
    config_rows = [asdict(config) for config in configs]
    write_csv(DATA_DIR / "experiment_configurations.csv", config_rows)
    write_json(JSON_DIR / "experiment_configurations.json", config_rows)

    all_data_rows: list[dict[str, object]] = []
    scenario_summaries: list[dict[str, object]] = []
    for config in configs:
        data_rows = generate_synthetic_data(config)
        all_data_rows.extend(data_rows)
        scenario_summaries.append(analyze_experiment(data_rows, config))

    write_csv(DATA_DIR / "synthetic_experiment_data.csv", all_data_rows)
    write_csv(TABLES / "scenario_experiment_summaries.csv", scenario_summaries)
    write_json(JSON_DIR / "scenario_experiment_summaries.json", scenario_summaries)

    sensitivity_summary = sensitivity_runs()
    write_csv(TABLES / "sensitivity_experiment_summary.csv", sensitivity_summary)
    write_json(JSON_DIR / "sensitivity_experiment_summary.json", sensitivity_summary)

    checklist_rows = workflow_checklist()
    write_csv(TABLES / "reproducible_workflow_checklist.csv", checklist_rows)
    write_json(JSON_DIR / "reproducible_workflow_checklist.json", checklist_rows)

    environment = runtime_environment()
    write_json(JSON_DIR / "runtime_environment.json", environment)

    produced_paths = [
        DATA_DIR / "experiment_configurations.csv",
        DATA_DIR / "synthetic_experiment_data.csv",
        TABLES / "scenario_experiment_summaries.csv",
        TABLES / "sensitivity_experiment_summary.csv",
        TABLES / "reproducible_workflow_checklist.csv",
        JSON_DIR / "experiment_configurations.json",
        JSON_DIR / "scenario_experiment_summaries.json",
        JSON_DIR / "sensitivity_experiment_summary.json",
        JSON_DIR / "reproducible_workflow_checklist.json",
        JSON_DIR / "runtime_environment.json",
    ]
    manifest_rows = collect_file_manifest(produced_paths)
    write_csv(TABLES / "output_manifest.csv", manifest_rows)
    write_json(JSON_DIR / "output_manifest.json", manifest_rows)

    review_attention = sum(1 for row in checklist_rows if row["status"] in {"partial", "needs_review"})
    audit_summary = {
        "experiment_name": "computational_experiments_and_reproducible_workflows",
        "scenario_count": len(configs),
        "synthetic_data_rows": len(all_data_rows),
        "sensitivity_rows": len(sensitivity_summary),
        "manifest_files": len(manifest_rows),
        "review_items_needing_attention": review_attention,
        "timestamp_utc": timestamp_utc(),
        "interpretation": "A computational experiment becomes auditable when code, data, parameters, environment, outputs, logs, and interpretation limits are preserved together.",
    }
    write_csv(TABLES / "reproducible_experiment_audit_summary.csv", [audit_summary])
    write_json(JSON_DIR / "reproducible_experiment_audit_summary.json", audit_summary)

    run_log.write_text("\n".join(log_rows) + "\n", encoding="utf-8")
    log("Computational experiments and reproducible workflows audit complete.")


if __name__ == "__main__":
    main()
