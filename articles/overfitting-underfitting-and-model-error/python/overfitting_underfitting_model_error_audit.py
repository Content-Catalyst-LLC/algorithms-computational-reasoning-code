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
class ModelErrorAuditConfig:
    experiment_name: str
    seed: int
    train_n: int
    test_n: int
    shifted_test_n: int
    learning_rate: float
    epochs: int


@dataclass(frozen=True)
class PolynomialModelSpec:
    model_name: str
    degree: int
    ridge_penalty: float
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


def default_config() -> ModelErrorAuditConfig:
    return ModelErrorAuditConfig(
        experiment_name="overfitting_underfitting_model_error_audit",
        seed=2026,
        train_n=90,
        test_n=300,
        shifted_test_n=300,
        learning_rate=0.030,
        epochs=900,
    )


def true_signal(x: float) -> float:
    return 0.45 + 1.15 * x - 0.85 * (x ** 2) + 0.22 * math.sin(4.0 * math.pi * x)


def generate_split(split: str, n: int, rng: random.Random) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for i in range(n):
        if split == "train":
            x = rng.uniform(-1.0, 1.0)
            noise_sd = 0.18
        elif split == "test":
            x = rng.uniform(-1.0, 1.0)
            noise_sd = 0.18
        else:
            x = rng.uniform(-0.15, 1.15)
            noise_sd = 0.22
        group = "lower_region" if x < -0.20 else ("middle_region" if x <= 0.55 else "upper_region")
        y_signal = true_signal(x)
        y_observed = y_signal + rng.gauss(0.0, noise_sd)
        rows.append({
            "row_id": f"{split}_{i + 1:04d}",
            "split": split,
            "x": round(x, 6),
            "group": group,
            "true_signal": round(y_signal, 6),
            "observed_y": round(y_observed, 6),
            "noise_sd": noise_sd,
            "interpretation": "Synthetic continuous outcome for model-error and generalization diagnostics.",
        })
    return rows


def powers(x: float, degree: int) -> list[float]:
    return [x ** p for p in range(degree + 1)]


def predict(weights: list[float], x: float) -> float:
    return sum(weight * (x ** p) for p, weight in enumerate(weights))


def mse(weights: list[float], rows: list[dict[str, object]]) -> float:
    return mean((predict(weights, float(row["x"])) - float(row["observed_y"])) ** 2 for row in rows)


def mae(weights: list[float], rows: list[dict[str, object]]) -> float:
    return mean(abs(predict(weights, float(row["x"])) - float(row["observed_y"])) for row in rows)


def train_polynomial(rows: list[dict[str, object]], degree: int, ridge: float, learning_rate: float, epochs: int) -> list[float]:
    weights = [0.0 for _ in range(degree + 1)]
    n = float(len(rows))
    for _ in range(epochs):
        gradients = [0.0 for _ in weights]
        for row in rows:
            x = float(row["x"])
            y = float(row["observed_y"])
            features = powers(x, degree)
            error = sum(weight * feature for weight, feature in zip(weights, features)) - y
            for j, feature in enumerate(features):
                gradients[j] += (2.0 / n) * error * feature
        for j in range(len(weights)):
            penalty = 0.0 if j == 0 else 2.0 * ridge * weights[j]
            weights[j] -= learning_rate * (gradients[j] + penalty)
    return weights


def model_specs() -> list[PolynomialModelSpec]:
    return [
        PolynomialModelSpec("constant_underfit", 0, 0.000, "Very low capacity; useful for showing underfitting."),
        PolynomialModelSpec("linear_underfit", 1, 0.000, "Low capacity; misses curvature and periodic structure."),
        PolynomialModelSpec("moderate_polynomial", 4, 0.000, "Moderate capacity intended to capture stable structure."),
        PolynomialModelSpec("high_degree_overfit", 12, 0.000, "High capacity; can follow sample noise and unstable edges."),
        PolynomialModelSpec("regularized_high_degree", 12, 0.020, "High capacity constrained by ridge regularization."),
    ]


def classify_pattern(train_error: float, test_error: float, shifted_error: float) -> str:
    gap = test_error - train_error
    if train_error > 0.090 and test_error > 0.100:
        return "underfitting_risk"
    if gap > 0.055 or shifted_error > test_error * 1.80:
        return "overfitting_or_shift_risk"
    if test_error < 0.070 and gap < 0.055:
        return "comparatively_stable"
    return "needs_review"


def evaluate_models(train_rows: list[dict[str, object]], test_rows: list[dict[str, object]], shifted_rows: list[dict[str, object]], config: ModelErrorAuditConfig) -> tuple[list[dict[str, object]], dict[str, list[float]]]:
    metrics: list[dict[str, object]] = []
    fitted: dict[str, list[float]] = {}
    for spec in model_specs():
        lr = config.learning_rate if spec.degree <= 4 else config.learning_rate * 0.55
        weights = train_polynomial(train_rows, spec.degree, spec.ridge_penalty, lr, config.epochs)
        fitted[spec.model_name] = weights
        train_mse = mse(weights, train_rows)
        test_mse = mse(weights, test_rows)
        shifted_mse = mse(weights, shifted_rows)
        metrics.append({
            "model_name": spec.model_name,
            "degree": spec.degree,
            "ridge_penalty": spec.ridge_penalty,
            "train_mse": round(train_mse, 6),
            "test_mse": round(test_mse, 6),
            "shifted_test_mse": round(shifted_mse, 6),
            "train_mae": round(mae(weights, train_rows), 6),
            "test_mae": round(mae(weights, test_rows), 6),
            "generalization_gap_mse": round(test_mse - train_mse, 6),
            "shift_penalty_mse": round(shifted_mse - test_mse, 6),
            "pattern_classification": classify_pattern(train_mse, test_mse, shifted_mse),
            "weight_count": len(weights),
            "interpretation": spec.interpretation,
        })
    return metrics, fitted


def residual_diagnostics(rows: list[dict[str, object]], weights: list[float], split_name: str) -> list[dict[str, object]]:
    grouped: dict[str, list[float]] = {}
    for row in rows:
        group = str(row["group"])
        residual = float(row["observed_y"]) - predict(weights, float(row["x"]))
        grouped.setdefault(group, []).append(residual)
    diagnostics: list[dict[str, object]] = []
    for group, residuals in grouped.items():
        diagnostics.append({
            "split": split_name,
            "group": group,
            "count": len(residuals),
            "mean_residual": round(mean(residuals), 6),
            "mean_absolute_residual": round(mean(abs(value) for value in residuals), 6),
            "residual_sd": round(pstdev(residuals), 6) if len(residuals) > 1 else 0.0,
            "interpretation": "Residual patterns can reveal regions where error is systematic rather than random.",
        })
    return diagnostics


def validation_curve(train_rows: list[dict[str, object]], test_rows: list[dict[str, object]], config: ModelErrorAuditConfig) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for degree in range(0, 13):
        lr = config.learning_rate if degree <= 4 else config.learning_rate * 0.55
        weights = train_polynomial(train_rows, degree, 0.0, lr, max(420, config.epochs // 2))
        train_error = mse(weights, train_rows)
        test_error = mse(weights, test_rows)
        rows.append({
            "degree": degree,
            "train_mse": round(train_error, 6),
            "test_mse": round(test_error, 6),
            "gap_mse": round(test_error - train_error, 6),
            "interpretation": "Validation curves compare model complexity with train and held-out error.",
        })
    return rows


def learning_curve(train_rows: list[dict[str, object]], test_rows: list[dict[str, object]], config: ModelErrorAuditConfig) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    ordered = sorted(train_rows, key=lambda row: row["row_id"])
    for train_size in [20, 35, 50, 70, len(ordered)]:
        subset = ordered[:train_size]
        weights = train_polynomial(subset, 4, 0.0, config.learning_rate, max(420, config.epochs // 2))
        train_error = mse(weights, subset)
        test_error = mse(weights, test_rows)
        rows.append({
            "train_size": train_size,
            "model_name": "moderate_polynomial",
            "train_mse": round(train_error, 6),
            "test_mse": round(test_error, 6),
            "gap_mse": round(test_error - train_error, 6),
            "interpretation": "Learning curves show whether more data appears to reduce held-out error or close the generalization gap.",
        })
    return rows


def prediction_rows(source_rows: list[dict[str, object]], fitted: dict[str, list[float]]) -> list[dict[str, object]]:
    selected = source_rows[:40]
    rows: list[dict[str, object]] = []
    for row in selected:
        x = float(row["x"])
        item = {"row_id": row["row_id"], "split": row["split"], "x": row["x"], "observed_y": row["observed_y"], "true_signal": row["true_signal"]}
        for name, weights in fitted.items():
            item[f"prediction_{name}"] = round(predict(weights, x), 6)
        rows.append(item)
    return rows


def governance_review(metrics: list[dict[str, object]]) -> list[dict[str, object]]:
    best_by_test = min(metrics, key=lambda row: float(row["test_mse"]))
    return [
        {"review_item": "model_selection_boundary", "status": "needs_documentation", "evidence": f"Lowest test MSE in synthetic audit: {best_by_test['model_name']}", "review_question": "Was the model selected through a valid validation process rather than repeated test-set probing?"},
        {"review_item": "overfitting_check", "status": "complete", "evidence": "Generalization gaps are reported for each model complexity level.", "review_question": "Does a high-capacity model perform substantially better on training data than held-out data?"},
        {"review_item": "underfitting_check", "status": "complete", "evidence": "Constant and linear baselines are included for low-capacity comparison.", "review_question": "Does the model fail to learn stable structure visible in the data?"},
        {"review_item": "shift_review", "status": "needs_review", "evidence": "Shifted-test performance is reported separately from ordinary test performance.", "review_question": "Would future deployment cases differ from training and test data?"},
        {"review_item": "use_boundary", "status": "needs_review", "evidence": "Synthetic workflow cannot establish operational reliability.", "review_question": "Where should model-error evidence not be generalized?"},
    ]


def main() -> None:
    config = default_config()
    rng = random.Random(config.seed)
    train_rows = generate_split("train", config.train_n, rng)
    test_rows = generate_split("test", config.test_n, rng)
    shifted_rows = generate_split("shifted_test", config.shifted_test_n, rng)
    observations = train_rows + test_rows + shifted_rows
    metrics, fitted = evaluate_models(train_rows, test_rows, shifted_rows, config)
    selected_weights = fitted["moderate_polynomial"]
    residuals = residual_diagnostics(train_rows, selected_weights, "train") + residual_diagnostics(test_rows, selected_weights, "test") + residual_diagnostics(shifted_rows, selected_weights, "shifted_test")
    validation_rows = validation_curve(train_rows, test_rows, config)
    learning_rows = learning_curve(train_rows, test_rows, config)
    governance_rows = governance_review(metrics)
    predictions = prediction_rows(test_rows, fitted) + prediction_rows(shifted_rows, fitted)
    best_test = min(metrics, key=lambda row: float(row["test_mse"]))
    worst_gap = max(metrics, key=lambda row: float(row["generalization_gap_mse"]))
    audit_summary = {
        "article": "overfitting_underfitting_and_model_error",
        "timestamp_utc": timestamp_utc(),
        "train_n": config.train_n,
        "test_n": config.test_n,
        "shifted_test_n": config.shifted_test_n,
        "model_count": len(metrics),
        "best_test_model": best_test["model_name"],
        "best_test_mse": best_test["test_mse"],
        "largest_generalization_gap_model": worst_gap["model_name"],
        "largest_generalization_gap_mse": worst_gap["generalization_gap_mse"],
        "models_flagged_for_review": sum(1 for row in metrics if row["pattern_classification"] != "comparatively_stable"),
        "interpretation": "Model error review should compare underfitting, overfitting, regularization, residual patterns, and shifted-test fragility before trusting model performance claims.",
    }
    write_csv(TABLES / "model_error_synthetic_observations.csv", observations)
    write_csv(TABLES / "model_complexity_metrics.csv", metrics)
    write_csv(TABLES / "model_error_residual_diagnostics.csv", residuals)
    write_csv(TABLES / "model_error_validation_curve.csv", validation_rows)
    write_csv(TABLES / "model_error_learning_curve.csv", learning_rows)
    write_csv(TABLES / "model_error_predictions_sample.csv", predictions)
    write_csv(TABLES / "model_error_governance_review.csv", governance_rows)
    write_csv(TABLES / "model_error_audit_summary.csv", [audit_summary])
    write_json(JSON_DIR / "model_error_audit_config.json", asdict(config))
    write_json(JSON_DIR / "model_complexity_metrics.json", metrics)
    write_json(JSON_DIR / "model_error_residual_diagnostics.json", residuals)
    write_json(JSON_DIR / "model_error_validation_curve.json", validation_rows)
    write_json(JSON_DIR / "model_error_learning_curve.json", learning_rows)
    write_json(JSON_DIR / "model_error_governance_review.json", governance_rows)
    write_json(JSON_DIR / "model_error_audit_summary.json", audit_summary)
    print("Overfitting, underfitting, and model-error audit complete.")
    print(TABLES / "model_error_audit_summary.csv")


if __name__ == "__main__":
    main()
