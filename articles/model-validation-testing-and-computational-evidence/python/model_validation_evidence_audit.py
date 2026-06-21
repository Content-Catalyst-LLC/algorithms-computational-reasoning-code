#!/usr/bin/env python3
"""Dependency-light model validation, testing, and computational evidence audit."""

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
DATA_DIR = ARTICLE_ROOT / "data"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"
LOGS = ARTICLE_ROOT / "outputs" / "logs"


@dataclass(frozen=True)
class ValidationConfig:
    experiment_name: str = "model_validation_testing_computational_evidence"
    seed: int = 2026
    sample_size: int = 1200
    noise_scale: float = 5.5
    drift_strength: float = 2.0
    high_risk_threshold: float = 50.0


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


def generate_validation_data(config: ValidationConfig) -> list[dict[str, object]]:
    rng = random.Random(config.seed)
    rows: list[dict[str, object]] = []
    for unit_id in range(1, config.sample_size + 1):
        segment = "A" if unit_id % 3 != 0 else "B"
        exposure = rng.uniform(0, 100)
        capacity = rng.uniform(20, 90)
        vulnerability = rng.uniform(0, 1)
        segment_shift = 6.0 if segment == "B" else 0.0
        observed = (
            12.0
            + 0.42 * exposure
            - 0.24 * capacity
            + 18.0 * vulnerability
            + segment_shift
            + rng.gauss(0.0, config.noise_scale)
        )
        baseline_prediction = mean([exposure, capacity])
        candidate_prediction = (
            11.0
            + 0.40 * exposure
            - 0.22 * capacity
            + 15.0 * vulnerability
            + config.drift_strength * (1 if segment == "A" else -1)
        )
        rows.append(
            {
                "unit_id": unit_id,
                "segment": segment,
                "exposure": round(exposure, 6),
                "capacity": round(capacity, 6),
                "vulnerability": round(vulnerability, 6),
                "observed": round(observed, 6),
                "baseline_prediction": round(baseline_prediction, 6),
                "candidate_prediction": round(candidate_prediction, 6),
                "high_risk_threshold": config.high_risk_threshold,
                "observed_high_risk": int(observed >= config.high_risk_threshold),
                "candidate_high_risk": int(candidate_prediction >= config.high_risk_threshold),
            }
        )
    return rows


def residuals(rows: list[dict[str, object]], prediction_key: str) -> list[float]:
    return [float(row["observed"]) - float(row[prediction_key]) for row in rows]


def rmse(rows: list[dict[str, object]], prediction_key: str) -> float:
    errs = residuals(rows, prediction_key)
    return math.sqrt(mean([err * err for err in errs]))


def mae(rows: list[dict[str, object]], prediction_key: str) -> float:
    return mean([abs(err) for err in residuals(rows, prediction_key)])


def bias(rows: list[dict[str, object]], prediction_key: str) -> float:
    return mean(residuals(rows, prediction_key))


def correlation(xs: list[float], ys: list[float]) -> float:
    xbar = mean(xs)
    ybar = mean(ys)
    numerator = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys))
    xden = math.sqrt(sum((x - xbar) ** 2 for x in xs))
    yden = math.sqrt(sum((y - ybar) ** 2 for y in ys))
    if xden == 0 or yden == 0:
        return 0.0
    return numerator / (xden * yden)


def simple_calibration(rows: list[dict[str, object]], prediction_key: str) -> dict[str, float]:
    preds = [float(row[prediction_key]) for row in rows]
    obs = [float(row["observed"]) for row in rows]
    xbar = mean(preds)
    ybar = mean(obs)
    denom = sum((x - xbar) ** 2 for x in preds)
    slope = 0.0 if denom == 0 else sum((x - xbar) * (y - ybar) for x, y in zip(preds, obs)) / denom
    intercept = ybar - slope * xbar
    return {
        "calibration_intercept": intercept,
        "calibration_slope": slope,
        "prediction_observed_correlation": correlation(preds, obs),
    }


def classification_metrics(rows: list[dict[str, object]]) -> dict[str, float]:
    tp = sum(1 for row in rows if int(row["observed_high_risk"]) == 1 and int(row["candidate_high_risk"]) == 1)
    tn = sum(1 for row in rows if int(row["observed_high_risk"]) == 0 and int(row["candidate_high_risk"]) == 0)
    fp = sum(1 for row in rows if int(row["observed_high_risk"]) == 0 and int(row["candidate_high_risk"]) == 1)
    fn = sum(1 for row in rows if int(row["observed_high_risk"]) == 1 and int(row["candidate_high_risk"]) == 0)
    total = tp + tn + fp + fn
    return {
        "true_positive": tp,
        "true_negative": tn,
        "false_positive": fp,
        "false_negative": fn,
        "accuracy": (tp + tn) / total if total else 0.0,
        "false_positive_rate": fp / (fp + tn) if (fp + tn) else 0.0,
        "false_negative_rate": fn / (fn + tp) if (fn + tp) else 0.0,
        "precision": tp / (tp + fp) if (tp + fp) else 0.0,
        "recall": tp / (tp + fn) if (tp + fn) else 0.0,
    }


def validation_summary(rows: list[dict[str, object]], prediction_key: str, model_name: str) -> dict[str, object]:
    cal = simple_calibration(rows, prediction_key)
    errs = residuals(rows, prediction_key)
    return {
        "model_name": model_name,
        "prediction_key": prediction_key,
        "n": len(rows),
        "rmse": round(rmse(rows, prediction_key), 6),
        "mae": round(mae(rows, prediction_key), 6),
        "bias": round(bias(rows, prediction_key), 6),
        "residual_std": round(pstdev(errs), 6),
        "calibration_intercept": round(cal["calibration_intercept"], 6),
        "calibration_slope": round(cal["calibration_slope"], 6),
        "prediction_observed_correlation": round(cal["prediction_observed_correlation"], 6),
        "interpretation": "Validation metrics summarize error, bias, calibration, and association with observed outcomes.",
    }


def subgroup_summary(rows: list[dict[str, object]], prediction_key: str) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for segment in sorted(set(str(row["segment"]) for row in rows)):
        subset = [row for row in rows if row["segment"] == segment]
        out.append(
            {
                "segment": segment,
                "n": len(subset),
                "prediction_key": prediction_key,
                "rmse": round(rmse(subset, prediction_key), 6),
                "mae": round(mae(subset, prediction_key), 6),
                "bias": round(bias(subset, prediction_key), 6),
                "interpretation": "Subgroup diagnostics reveal performance differences hidden by aggregate metrics.",
            }
        )
    return out


def threshold_sweep(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for threshold in [35, 40, 45, 50, 55, 60, 65]:
        updated_rows = []
        for row in rows:
            updated = dict(row)
            updated["observed_high_risk"] = int(float(row["observed"]) >= threshold)
            updated["candidate_high_risk"] = int(float(row["candidate_prediction"]) >= threshold)
            updated_rows.append(updated)
        metrics = classification_metrics(updated_rows)
        out.append(
            {
                "threshold": threshold,
                "accuracy": round(metrics["accuracy"], 6),
                "false_positive_rate": round(metrics["false_positive_rate"], 6),
                "false_negative_rate": round(metrics["false_negative_rate"], 6),
                "precision": round(metrics["precision"], 6),
                "recall": round(metrics["recall"], 6),
                "interpretation": "Threshold diagnostics show how decisions change with cutoffs.",
            }
        )
    return out


def implementation_tests(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    required = {"observed", "baseline_prediction", "candidate_prediction", "segment"}
    missing = required.difference(rows[0].keys()) if rows else required
    finite = all(math.isfinite(float(row["observed"])) and math.isfinite(float(row["candidate_prediction"])) for row in rows)
    binary = all(int(row["observed_high_risk"]) in {0, 1} and int(row["candidate_high_risk"]) in {0, 1} for row in rows)
    return [
        {"test_name": "row_count_positive", "status": "pass" if rows else "fail", "detail": f"{len(rows)} rows available."},
        {"test_name": "required_fields_present", "status": "pass" if not missing else "fail", "detail": "All required fields present." if not missing else ", ".join(sorted(missing))},
        {"test_name": "numeric_outputs_finite", "status": "pass" if finite else "fail", "detail": "Observed and predicted values should be finite."},
        {"test_name": "classification_values_binary", "status": "pass" if binary else "fail", "detail": "High-risk indicators should be binary."},
    ]


def validation_checklist() -> list[dict[str, object]]:
    return [
        {"check": "intended_use_defined", "status": "complete", "question": "Is intended use explicitly documented?"},
        {"check": "data_quality_checked", "status": "complete", "question": "Are input data checked before model use?"},
        {"check": "implementation_tests_run", "status": "complete", "question": "Do tests support code correctness?"},
        {"check": "baseline_compared", "status": "complete", "question": "Is performance compared with a simple baseline?"},
        {"check": "diagnostics_reported", "status": "complete", "question": "Are error, calibration, and subgroup diagnostics reported?"},
        {"check": "thresholds_reviewed", "status": "complete", "question": "Are decision thresholds tested?"},
        {"check": "uncertainty_and_sensitivity_reviewed", "status": "partial", "question": "Are uncertainty and sensitivity reviewed?"},
        {"check": "governance_limits_documented", "status": "complete", "question": "Are use boundaries and review responsibilities documented?"},
    ]


def main() -> None:
    config = ValidationConfig()
    LOGS.mkdir(parents=True, exist_ok=True)
    rows = generate_validation_data(config)
    write_csv(DATA_DIR / "synthetic_validation_data.csv", rows)
    write_json(JSON_DIR / "validation_config.json", asdict(config))

    summaries = [
        validation_summary(rows, "baseline_prediction", "simple_baseline"),
        validation_summary(rows, "candidate_prediction", "candidate_model"),
    ]
    write_csv(TABLES / "model_validation_summary.csv", summaries)
    write_json(JSON_DIR / "model_validation_summary.json", summaries)

    subgroup_rows = subgroup_summary(rows, "candidate_prediction")
    write_csv(TABLES / "candidate_subgroup_diagnostics.csv", subgroup_rows)
    write_json(JSON_DIR / "candidate_subgroup_diagnostics.json", subgroup_rows)

    threshold_rows = threshold_sweep(rows)
    write_csv(TABLES / "threshold_sweep_diagnostics.csv", threshold_rows)
    write_json(JSON_DIR / "threshold_sweep_diagnostics.json", threshold_rows)

    test_rows = implementation_tests(rows)
    write_csv(TABLES / "implementation_test_results.csv", test_rows)
    write_json(JSON_DIR / "implementation_test_results.json", test_rows)

    checklist_rows = validation_checklist()
    write_csv(TABLES / "validation_review_checklist.csv", checklist_rows)
    write_json(JSON_DIR / "validation_review_checklist.json", checklist_rows)

    candidate = [row for row in summaries if row["model_name"] == "candidate_model"][0]
    baseline = [row for row in summaries if row["model_name"] == "simple_baseline"][0]
    audit_summary = {
        "experiment_name": config.experiment_name,
        "timestamp_utc": timestamp_utc(),
        "validation_rows": len(rows),
        "candidate_rmse": candidate["rmse"],
        "baseline_rmse": baseline["rmse"],
        "candidate_beats_baseline": float(candidate["rmse"]) < float(baseline["rmse"]),
        "implementation_test_failures": sum(1 for row in test_rows if row["status"] != "pass"),
        "review_items_needing_attention": sum(1 for row in checklist_rows if row["status"] in {"partial", "needs_review"}),
        "interpretation": "Validation evidence connects intended use, data quality, tests, diagnostics, thresholds, uncertainty, and governance limits.",
    }
    write_csv(TABLES / "model_validation_evidence_audit_summary.csv", [audit_summary])
    write_json(JSON_DIR / "model_validation_evidence_audit_summary.json", audit_summary)
    (LOGS / "model_validation_run.log").write_text(f"completed={timestamp_utc()}\n", encoding="utf-8")
    print("Model validation, testing, and computational evidence audit complete.")
    print(TABLES / "model_validation_evidence_audit_summary.csv")


if __name__ == "__main__":
    main()
