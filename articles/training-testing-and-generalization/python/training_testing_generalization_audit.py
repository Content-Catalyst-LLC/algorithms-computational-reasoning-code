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


@dataclass(frozen=True)
class GeneralizationAuditConfig:
    experiment_name: str
    seed: int
    train_n: int
    test_n: int
    shifted_test_n: int
    learning_rate: float
    epochs: int
    threshold: float


@dataclass(frozen=True)
class ModelWeights:
    intercept: float
    feature_signal: float
    feature_context: float
    feature_noise_proxy: float


def timestamp_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def sigmoid(value: float) -> float:
    if value >= 0:
        z = math.exp(-value)
        return 1.0 / (1.0 + z)
    z = math.exp(value)
    return z / (1.0 + z)


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


def default_config() -> GeneralizationAuditConfig:
    return GeneralizationAuditConfig(
        experiment_name="training_testing_generalization_audit",
        seed=2026,
        train_n=520,
        test_n=260,
        shifted_test_n=260,
        learning_rate=0.18,
        epochs=520,
        threshold=0.50,
    )


def generate_split(split: str, n: int, rng: random.Random) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for i in range(n):
        group = "A" if rng.random() < (0.58 if split != "shifted_test" else 0.43) else "B"
        shift = 0.0 if split != "shifted_test" else 0.32
        feature_signal = rng.gauss(0.05 + shift + (0.10 if group == "A" else -0.06), 1.00)
        feature_context = rng.gauss(-0.02 + 0.15 * shift + (0.06 if group == "B" else 0.0), 1.00)
        feature_noise_proxy = rng.gauss(0.30 * feature_signal + (0.45 if split == "train" else 0.08), 1.00)
        linear_truth = -0.18 + 1.15 * feature_signal + 0.75 * feature_context - 0.10 * feature_noise_proxy
        if group == "B":
            linear_truth -= 0.12
        probability = sigmoid(linear_truth)
        target = 1 if rng.random() < probability else 0
        rows.append({
            "row_id": f"{split}_{i+1:04d}",
            "split": split,
            "group": group,
            "feature_signal": round(feature_signal, 6),
            "feature_context": round(feature_context, 6),
            "feature_noise_proxy": round(feature_noise_proxy, 6),
            "true_probability": round(probability, 6),
            "target": target,
            "interpretation": "Synthetic record for demonstrating training, testing, generalization, shift, and leakage review.",
        })
    return rows


def generate_dataset(config: GeneralizationAuditConfig) -> list[dict[str, object]]:
    rng = random.Random(config.seed)
    return (
        generate_split("train", config.train_n, rng)
        + generate_split("test", config.test_n, rng)
        + generate_split("shifted_test", config.shifted_test_n, rng)
    )


def features(row: dict[str, object]) -> tuple[float, float, float]:
    return (
        float(row["feature_signal"]),
        float(row["feature_context"]),
        float(row["feature_noise_proxy"]),
    )


def fit_logistic(rows: list[dict[str, object]], config: GeneralizationAuditConfig) -> ModelWeights:
    intercept = 0.0
    w_signal = 0.0
    w_context = 0.0
    w_noise = 0.0
    n = max(1, len(rows))
    for _ in range(config.epochs):
        g0 = g1 = g2 = g3 = 0.0
        for row in rows:
            x1, x2, x3 = features(row)
            y = int(row["target"])
            p = sigmoid(intercept + w_signal * x1 + w_context * x2 + w_noise * x3)
            error = p - y
            g0 += error
            g1 += error * x1
            g2 += error * x2
            g3 += error * x3
        intercept -= config.learning_rate * g0 / n
        w_signal -= config.learning_rate * g1 / n
        w_context -= config.learning_rate * g2 / n
        w_noise -= config.learning_rate * g3 / n
    return ModelWeights(intercept, w_signal, w_context, w_noise)


def predict_probability(row: dict[str, object], weights: ModelWeights) -> float:
    x1, x2, x3 = features(row)
    return sigmoid(weights.intercept + weights.feature_signal * x1 + weights.feature_context * x2 + weights.feature_noise_proxy * x3)


def evaluate(rows: list[dict[str, object]], weights: ModelWeights, split_name: str, threshold: float) -> dict[str, object]:
    predictions = []
    for row in rows:
        p = predict_probability(row, weights)
        y = int(row["target"])
        pred = 1 if p >= threshold else 0
        predictions.append((p, y, pred))
    tp = sum(1 for _, y, pred in predictions if y == 1 and pred == 1)
    tn = sum(1 for _, y, pred in predictions if y == 0 and pred == 0)
    fp = sum(1 for _, y, pred in predictions if y == 0 and pred == 1)
    fn = sum(1 for _, y, pred in predictions if y == 1 and pred == 0)
    n = len(predictions)
    eps = 1e-12
    accuracy = (tp + tn) / n
    precision = tp / max(1, tp + fp)
    recall = tp / max(1, tp + fn)
    brier = mean((p - y) ** 2 for p, y, _ in predictions)
    log_loss = mean(-(y * math.log(max(eps, p)) + (1 - y) * math.log(max(eps, 1 - p))) for p, y, _ in predictions)
    return {
        "split": split_name,
        "n": n,
        "accuracy": round(accuracy, 6),
        "precision": round(precision, 6),
        "recall": round(recall, 6),
        "brier_score": round(brier, 6),
        "log_loss": round(log_loss, 6),
        "true_positive": tp,
        "true_negative": tn,
        "false_positive": fp,
        "false_negative": fn,
        "interpretation": "Held-out performance estimates how well the fitted model transfers beyond the data used to fit it.",
    }


def group_metrics(rows: list[dict[str, object]], weights: ModelWeights, split_name: str, threshold: float) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for group in sorted({str(row["group"]) for row in rows}):
        subset = [row for row in rows if row["group"] == group]
        item = evaluate(subset, weights, split_name, threshold)
        item["group"] = group
        item["interpretation"] = "Group-level metrics can reveal uneven generalization and evaluation risk."
        out.append(item)
    return out


def cross_validation(rows: list[dict[str, object]], config: GeneralizationAuditConfig, folds: int = 5) -> list[dict[str, object]]:
    ordered = list(rows)
    rng = random.Random(config.seed + 99)
    rng.shuffle(ordered)
    fold_rows: list[dict[str, object]] = []
    for fold in range(folds):
        validation = [row for i, row in enumerate(ordered) if i % folds == fold]
        training = [row for i, row in enumerate(ordered) if i % folds != fold]
        weights = fit_logistic(training, config)
        metrics = evaluate(validation, weights, f"cv_fold_{fold+1}", config.threshold)
        metrics["fold"] = fold + 1
        metrics["interpretation"] = "Cross-validation estimates stability across repeated development splits."
        fold_rows.append(metrics)
    return fold_rows


def prediction_rows(rows: list[dict[str, object]], weights: ModelWeights, threshold: float) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for row in rows:
        p = predict_probability(row, weights)
        pred = 1 if p >= threshold else 0
        out.append({
            "row_id": row["row_id"],
            "split": row["split"],
            "group": row["group"],
            "target": row["target"],
            "predicted_probability": round(p, 6),
            "predicted_label": pred,
            "correct": int(pred == int(row["target"])),
        })
    return out


def calibration_rows(predictions: list[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for split in sorted({str(row["split"]) for row in predictions}):
        split_rows = [row for row in predictions if row["split"] == split]
        for bucket in range(10):
            low = bucket / 10
            high = (bucket + 1) / 10
            subset = [row for row in split_rows if low <= float(row["predicted_probability"]) < high or (bucket == 9 and float(row["predicted_probability"]) == 1.0)]
            if subset:
                rows.append({
                    "split": split,
                    "bucket": bucket,
                    "probability_range": f"[{low:.1f},{high:.1f})" if bucket < 9 else "[0.9,1.0]",
                    "n": len(subset),
                    "mean_predicted_probability": round(mean(float(row["predicted_probability"]) for row in subset), 6),
                    "observed_rate": round(mean(int(row["target"]) for row in subset), 6),
                    "interpretation": "Calibration compares confidence scores with observed outcome rates.",
                })
    return rows


def distribution_shift_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    train = [row for row in rows if row["split"] == "train"]
    shifted = [row for row in rows if row["split"] == "shifted_test"]
    out: list[dict[str, object]] = []
    for column in ["feature_signal", "feature_context", "feature_noise_proxy"]:
        train_values = [float(row[column]) for row in train]
        shifted_values = [float(row[column]) for row in shifted]
        pooled = math.sqrt((pstdev(train_values) ** 2 + pstdev(shifted_values) ** 2) / 2.0)
        standardized_shift = 0.0 if pooled == 0 else (mean(shifted_values) - mean(train_values)) / pooled
        out.append({
            "feature": column,
            "train_mean": round(mean(train_values), 6),
            "shifted_test_mean": round(mean(shifted_values), 6),
            "standardized_shift": round(standardized_shift, 6),
            "absolute_standardized_shift": round(abs(standardized_shift), 6),
            "interpretation": "Large shifts warn that held-out performance may not transfer to deployment conditions.",
        })
    return out


def risk_register(metrics: list[dict[str, object]], shift_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    by_split = {row["split"]: row for row in metrics}
    train_acc = float(by_split["train"]["accuracy"])
    test_acc = float(by_split["test"]["accuracy"])
    shifted_acc = float(by_split["shifted_test"]["accuracy"])
    gap = train_acc - test_acc
    shift_gap = test_acc - shifted_acc
    max_shift = max(float(row["absolute_standardized_shift"]) for row in shift_rows)
    return [
        {"risk": "generalization_gap", "value": round(gap, 6), "status": "review" if gap > 0.06 else "acceptable_for_teaching", "review_question": "Is the model performing materially worse on held-out data than on training data?", "interpretation": "A large train-test gap suggests overfitting, leakage, or unstable learning."},
        {"risk": "distribution_shift_gap", "value": round(shift_gap, 6), "status": "review" if shift_gap > 0.06 else "acceptable_for_teaching", "review_question": "Does performance decline when the data-generating conditions shift?", "interpretation": "A shifted-test decline warns that ordinary test performance may overstate deployment reliability."},
        {"risk": "feature_distribution_shift", "value": round(max_shift, 6), "status": "review" if max_shift > 0.30 else "acceptable_for_teaching", "review_question": "Are future or deployment cases distributed differently from training cases?", "interpretation": "Feature shift should be documented before generalization claims are made."},
        {"risk": "test_set_reuse", "value": 1, "status": "needs_process_control", "review_question": "Was the test set used repeatedly for model selection?", "interpretation": "Even a technically held-out test set can become contaminated if repeatedly used for tuning."},
    ]


def main() -> None:
    config = default_config()
    rows = generate_dataset(config)
    train_rows = [row for row in rows if row["split"] == "train"]
    test_rows = [row for row in rows if row["split"] == "test"]
    shifted_rows = [row for row in rows if row["split"] == "shifted_test"]
    weights = fit_logistic(train_rows, config)
    metrics = [
        evaluate(train_rows, weights, "train", config.threshold),
        evaluate(test_rows, weights, "test", config.threshold),
        evaluate(shifted_rows, weights, "shifted_test", config.threshold),
    ]
    cv = cross_validation(train_rows, config)
    group = group_metrics(test_rows, weights, "test", config.threshold) + group_metrics(shifted_rows, weights, "shifted_test", config.threshold)
    predictions = prediction_rows(rows, weights, config.threshold)
    calibration = calibration_rows(predictions)
    shift = distribution_shift_rows(rows)
    risks = risk_register(metrics, shift)
    cv_accuracies = [float(row["accuracy"]) for row in cv]
    summary = {
        "article": "training_testing_and_generalization",
        "timestamp_utc": timestamp_utc(),
        "train_n": config.train_n,
        "test_n": config.test_n,
        "shifted_test_n": config.shifted_test_n,
        "train_accuracy": metrics[0]["accuracy"],
        "test_accuracy": metrics[1]["accuracy"],
        "shifted_test_accuracy": metrics[2]["accuracy"],
        "generalization_gap_accuracy": round(float(metrics[0]["accuracy"]) - float(metrics[1]["accuracy"]), 6),
        "distribution_shift_gap_accuracy": round(float(metrics[1]["accuracy"]) - float(metrics[2]["accuracy"]), 6),
        "cross_validation_accuracy_mean": round(mean(cv_accuracies), 6),
        "cross_validation_accuracy_sd": round(pstdev(cv_accuracies), 6),
        "risks_needing_review": sum(1 for row in risks if row["status"] != "acceptable_for_teaching"),
        "interpretation": "Training, testing, and generalization workflows should separate fitting from evaluation, check stability, document uncertainty, and avoid treating benchmark performance as deployment proof.",
    }
    write_csv(TABLES / "synthetic_training_testing_records.csv", rows)
    write_csv(TABLES / "model_coefficients.csv", [asdict(weights)])
    write_csv(TABLES / "split_performance_metrics.csv", metrics)
    write_csv(TABLES / "cross_validation_metrics.csv", cv)
    write_csv(TABLES / "group_generalization_metrics.csv", group)
    write_csv(TABLES / "prediction_records.csv", predictions)
    write_csv(TABLES / "calibration_by_probability_bucket.csv", calibration)
    write_csv(TABLES / "distribution_shift_diagnostics.csv", shift)
    write_csv(TABLES / "generalization_risk_register.csv", risks)
    write_csv(TABLES / "training_testing_generalization_audit_summary.csv", [summary])
    write_json(JSON_DIR / "audit_config.json", asdict(config))
    write_json(JSON_DIR / "model_coefficients.json", asdict(weights))
    write_json(JSON_DIR / "split_performance_metrics.json", metrics)
    write_json(JSON_DIR / "cross_validation_metrics.json", cv)
    write_json(JSON_DIR / "group_generalization_metrics.json", group)
    write_json(JSON_DIR / "distribution_shift_diagnostics.json", shift)
    write_json(JSON_DIR / "generalization_risk_register.json", risks)
    write_json(JSON_DIR / "training_testing_generalization_audit_summary.json", summary)
    print("Training/testing/generalization audit complete.")
    print(TABLES / "training_testing_generalization_audit_summary.csv")

if __name__ == "__main__":
    main()
