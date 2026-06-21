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

FEATURE_COLUMNS = ["prior_signal", "measurement_quality", "context_pressure", "historical_access"]


@dataclass(frozen=True)
class MLInferenceConfig:
    experiment_name: str
    seed: int
    n: int
    train_fraction: float
    learning_rate: float
    epochs: int
    default_threshold: float


@dataclass(frozen=True)
class ModelCoefficients:
    intercept: float
    prior_signal: float
    measurement_quality: float
    context_pressure: float
    historical_access: float


def default_config() -> MLInferenceConfig:
    return MLInferenceConfig(
        experiment_name="machine_learning_as_algorithmic_inference",
        seed=2026,
        n=1000,
        train_fraction=0.70,
        learning_rate=0.12,
        epochs=900,
        default_threshold=0.50,
    )


def timestamp_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def sigmoid(value: float) -> float:
    if value < -40:
        return 0.0
    if value > 40:
        return 1.0
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


def generate_synthetic_data(config: MLInferenceConfig) -> list[dict[str, object]]:
    rng = random.Random(config.seed)
    rows: list[dict[str, object]] = []
    for unit_id in range(1, config.n + 1):
        prior_signal = rng.random()
        measurement_quality = max(0.0, min(1.0, rng.gauss(0.55 + 0.20 * prior_signal, 0.18)))
        context_pressure = max(0.0, min(1.0, rng.gauss(0.50 + 0.30 * prior_signal - 0.10 * measurement_quality, 0.20)))
        historical_access = max(0.0, min(1.0, rng.gauss(0.48 + 0.15 * measurement_quality - 0.12 * context_pressure, 0.18)))
        group = "high_context_pressure" if context_pressure >= 0.58 else "lower_context_pressure"
        latent_score = (
            -1.10
            + 1.45 * prior_signal
            - 1.05 * measurement_quality
            + 1.15 * context_pressure
            - 0.55 * historical_access
            + (0.22 if group == "high_context_pressure" else -0.05)
        )
        true_probability = sigmoid(latent_score)
        label = 1 if rng.random() < true_probability else 0
        rows.append({
            "unit_id": unit_id,
            "split_key": rng.random(),
            "group": group,
            "prior_signal": round(prior_signal, 6),
            "measurement_quality": round(measurement_quality, 6),
            "context_pressure": round(context_pressure, 6),
            "historical_access": round(historical_access, 6),
            "true_probability": round(true_probability, 6),
            "label": label,
            "label_note": "Synthetic label generated from a known process; real labels are often proxy measurements and require review.",
        })
    return rows


def train_test_split(rows: list[dict[str, object]], train_fraction: float) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    sorted_rows = sorted(rows, key=lambda row: float(row["split_key"]))
    cut = int(len(sorted_rows) * train_fraction)
    return sorted_rows[:cut], sorted_rows[cut:]


def features(row: dict[str, object]) -> list[float]:
    return [float(row[column]) for column in FEATURE_COLUMNS]


def train_logistic_regression(rows: list[dict[str, object]], config: MLInferenceConfig) -> ModelCoefficients:
    weights = [0.0 for _ in FEATURE_COLUMNS]
    intercept = 0.0
    n = max(1, len(rows))
    for _ in range(config.epochs):
        gradient_intercept = 0.0
        gradient_weights = [0.0 for _ in FEATURE_COLUMNS]
        for row in rows:
            x = features(row)
            y = float(row["label"])
            prediction = sigmoid(intercept + sum(w * value for w, value in zip(weights, x)))
            error = prediction - y
            gradient_intercept += error
            for i, value in enumerate(x):
                gradient_weights[i] += error * value
        intercept -= config.learning_rate * gradient_intercept / n
        for i in range(len(weights)):
            weights[i] -= config.learning_rate * gradient_weights[i] / n
    return ModelCoefficients(
        intercept=round(intercept, 8),
        prior_signal=round(weights[0], 8),
        measurement_quality=round(weights[1], 8),
        context_pressure=round(weights[2], 8),
        historical_access=round(weights[3], 8),
    )


def score_row(row: dict[str, object], coefficients: ModelCoefficients) -> float:
    value = (
        coefficients.intercept
        + coefficients.prior_signal * float(row["prior_signal"])
        + coefficients.measurement_quality * float(row["measurement_quality"])
        + coefficients.context_pressure * float(row["context_pressure"])
        + coefficients.historical_access * float(row["historical_access"])
    )
    return sigmoid(value)


def attach_predictions(rows: list[dict[str, object]], coefficients: ModelCoefficients, split: str) -> list[dict[str, object]]:
    enriched: list[dict[str, object]] = []
    for row in rows:
        score = score_row(row, coefficients)
        out = dict(row)
        out["split"] = split
        out["model_score"] = round(score, 6)
        out["predicted_label_0_50"] = 1 if score >= 0.50 else 0
        enriched.append(out)
    return enriched


def metrics(rows: list[dict[str, object]], threshold: float, split: str) -> dict[str, object]:
    tp = fp = tn = fn = 0
    losses: list[float] = []
    for row in rows:
        y = int(row["label"])
        score = float(row["model_score"])
        pred = 1 if score >= threshold else 0
        losses.append(-(y * math.log(max(score, 1e-9)) + (1 - y) * math.log(max(1 - score, 1e-9))))
        if pred == 1 and y == 1:
            tp += 1
        elif pred == 1 and y == 0:
            fp += 1
        elif pred == 0 and y == 0:
            tn += 1
        elif pred == 0 and y == 1:
            fn += 1
    total = max(1, len(rows))
    accuracy = (tp + tn) / total
    precision = tp / max(1, tp + fp)
    recall = tp / max(1, tp + fn)
    false_positive_rate = fp / max(1, fp + tn)
    false_negative_rate = fn / max(1, fn + tp)
    return {
        "split": split,
        "threshold": round(threshold, 4),
        "n": len(rows),
        "true_positive": tp,
        "false_positive": fp,
        "true_negative": tn,
        "false_negative": fn,
        "accuracy": round(accuracy, 6),
        "precision": round(precision, 6),
        "recall": round(recall, 6),
        "false_positive_rate": round(false_positive_rate, 6),
        "false_negative_rate": round(false_negative_rate, 6),
        "mean_log_loss": round(mean(losses), 6),
        "interpretation": "Classification metrics depend on threshold choice and should be reviewed before institutional use.",
    }


def threshold_sweep(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    return [metrics(rows, threshold / 100.0, "test") for threshold in range(20, 86, 5)]


def calibration_bins(rows: list[dict[str, object]], bins: int = 5) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for b in range(bins):
        lower = b / bins
        upper = (b + 1) / bins
        subset = [row for row in rows if lower <= float(row["model_score"]) < upper or (b == bins - 1 and float(row["model_score"]) == 1.0)]
        if not subset:
            continue
        avg_score = mean(float(row["model_score"]) for row in subset)
        observed_rate = mean(float(row["label"]) for row in subset)
        results.append({
            "bin": b + 1,
            "score_lower": round(lower, 3),
            "score_upper": round(upper, 3),
            "n": len(subset),
            "average_score": round(avg_score, 6),
            "observed_positive_rate": round(observed_rate, 6),
            "absolute_calibration_gap": round(abs(avg_score - observed_rate), 6),
            "interpretation": "Calibration compares model scores with observed rates inside score bands.",
        })
    return results


def group_error_diagnostics(rows: list[dict[str, object]], threshold: float) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for group in sorted({str(row["group"]) for row in rows}):
        subset = [row for row in rows if row["group"] == group]
        row = metrics(subset, threshold, f"test:{group}")
        row["group"] = group
        row["interpretation"] = "Subgroup diagnostics reveal whether error burdens differ across observed groups."
        out.append(row)
    return out


def feature_label_audit() -> list[dict[str, object]]:
    return [
        {"item": "features", "status": "review_required", "risk": "Input features may encode measurement choices, institutional history, or proxy variables.", "review_question": "Are features valid for the intended use?"},
        {"item": "labels", "status": "review_required", "risk": "Labels may reflect noisy, delayed, biased, or administratively produced outcomes.", "review_question": "Does the label measure the target construct?"},
        {"item": "train_test_split", "status": "complete", "risk": "Evaluation can be inflated if test data leak into training.", "review_question": "Is held-out evaluation preserved?"},
        {"item": "threshold", "status": "review_required", "risk": "Thresholds convert scores into decisions and encode trade-offs.", "review_question": "Who approved the threshold and why?"},
        {"item": "calibration", "status": "partial", "risk": "Scores may be misread as probabilities if not calibrated.", "review_question": "Do predicted scores match observed frequencies?"},
        {"item": "subgroup_error", "status": "partial", "risk": "Average performance can hide uneven error burdens.", "review_question": "Which groups face higher false positives or false negatives?"},
    ]


def governance_register(metrics_rows: list[dict[str, object]], calibration_rows: list[dict[str, object]], group_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    max_calibration_gap = max((float(row["absolute_calibration_gap"]) for row in calibration_rows), default=0.0)
    fpr_values = [float(row["false_positive_rate"]) for row in group_rows]
    fnr_values = [float(row["false_negative_rate"]) for row in group_rows]
    return [
        {"review_area": "generalization", "signal": "train_test_metric_comparison", "status": "review_required", "evidence": "Compare training and test metrics before using the model outside the synthetic exercise."},
        {"review_area": "threshold_tradeoff", "signal": "threshold_sweep", "status": "review_required", "evidence": "False positives and false negatives shift as threshold changes."},
        {"review_area": "calibration", "signal": f"max_gap={max_calibration_gap:.4f}", "status": "partial", "evidence": "Calibration should be checked before interpreting scores as probabilities."},
        {"review_area": "subgroup_error", "signal": f"fpr_range={max(fpr_values) - min(fpr_values):.4f}; fnr_range={max(fnr_values) - min(fnr_values):.4f}", "status": "review_required", "evidence": "Subgroup error differences should be reviewed before deployment."},
        {"review_area": "use_boundary", "signal": "educational_synthetic_only", "status": "complete", "evidence": "Outputs are not validated for real-world decision-making."},
    ]


def main() -> None:
    TABLES.mkdir(parents=True, exist_ok=True)
    JSON_DIR.mkdir(parents=True, exist_ok=True)
    LOGS.mkdir(parents=True, exist_ok=True)
    config = default_config()
    rows = generate_synthetic_data(config)
    train, test = train_test_split(rows, config.train_fraction)
    coefficients = train_logistic_regression(train, config)
    train_predictions = attach_predictions(train, coefficients, "train")
    test_predictions = attach_predictions(test, coefficients, "test")
    combined_predictions = train_predictions + test_predictions
    model_metrics = [
        metrics(train_predictions, config.default_threshold, "train"),
        metrics(test_predictions, config.default_threshold, "test"),
    ]
    sweep = threshold_sweep(test_predictions)
    calibration = calibration_bins(test_predictions)
    group_rows = group_error_diagnostics(test_predictions, config.default_threshold)
    feature_audit = feature_label_audit()
    governance = governance_register(model_metrics, calibration, group_rows)
    summary = {
        "article": "machine_learning_as_algorithmic_inference",
        "timestamp_utc": timestamp_utc(),
        "n_total": len(rows),
        "n_train": len(train_predictions),
        "n_test": len(test_predictions),
        "default_threshold": config.default_threshold,
        "test_accuracy": model_metrics[1]["accuracy"],
        "test_false_positive_rate": model_metrics[1]["false_positive_rate"],
        "test_false_negative_rate": model_metrics[1]["false_negative_rate"],
        "max_calibration_gap": max((row["absolute_calibration_gap"] for row in calibration), default=0.0),
        "governance_items_requiring_review": sum(1 for row in governance if row["status"] == "review_required"),
        "interpretation": "Machine learning inference requires data design, train/test separation, threshold review, calibration, subgroup diagnostics, and governance before institutional use.",
    }
    write_csv(TABLES / "ml_synthetic_observations.csv", rows)
    write_csv(TABLES / "ml_predictions.csv", combined_predictions)
    write_csv(TABLES / "ml_model_metrics.csv", model_metrics)
    write_csv(TABLES / "ml_threshold_sweep.csv", sweep)
    write_csv(TABLES / "ml_calibration_bins.csv", calibration)
    write_csv(TABLES / "ml_group_error_diagnostics.csv", group_rows)
    write_csv(TABLES / "ml_feature_label_audit.csv", feature_audit)
    write_csv(TABLES / "ml_inference_governance_register.csv", governance)
    write_csv(TABLES / "ml_inference_audit_summary.csv", [summary])
    write_json(JSON_DIR / "ml_inference_config.json", asdict(config))
    write_json(JSON_DIR / "ml_model_coefficients.json", asdict(coefficients))
    write_json(JSON_DIR / "ml_model_metrics.json", model_metrics)
    write_json(JSON_DIR / "ml_threshold_sweep.json", sweep)
    write_json(JSON_DIR / "ml_calibration_bins.json", calibration)
    write_json(JSON_DIR / "ml_group_error_diagnostics.json", group_rows)
    write_json(JSON_DIR / "ml_feature_label_audit.json", feature_audit)
    write_json(JSON_DIR / "ml_inference_governance_register.json", governance)
    write_json(JSON_DIR / "ml_inference_audit_summary.json", summary)
    (LOGS / "ml_inference_workflow.log").write_text("Machine learning inference audit complete.\n", encoding="utf-8")
    print("Machine learning inference audit complete.")
    print(TABLES / "ml_inference_audit_summary.csv")


if __name__ == "__main__":
    main()
