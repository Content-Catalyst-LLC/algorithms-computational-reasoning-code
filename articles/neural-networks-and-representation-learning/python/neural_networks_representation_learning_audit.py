from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from datetime import datetime, timezone
import csv
import json
import math
import random

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"
LOGS = ARTICLE_ROOT / "outputs" / "logs"


@dataclass(frozen=True)
class RepresentationConfig:
    experiment_name: str = "neural_networks_representation_learning"
    seed: int = 2026
    n: int = 420
    train_fraction: float = 0.70
    learning_rate: float = 0.08
    epochs: int = 220
    threshold: float = 0.50


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


def generate_data(config: RepresentationConfig) -> list[dict[str, object]]:
    rng = random.Random(config.seed)
    rows: list[dict[str, object]] = []
    for unit_id in range(1, config.n + 1):
        x1 = rng.gauss(0.0, 1.0)
        x2 = rng.gauss(0.0, 1.0)
        x3 = rng.gauss(0.0, 1.0)
        group_marker = "context_a" if rng.random() < 0.55 else "context_b"
        context_shift = 0.20 if group_marker == "context_b" else -0.05
        latent_signal = 0.95 * x1 - 0.70 * x2 + 0.45 * x1 * x3 + context_shift
        probability = sigmoid(latent_signal)
        label = 1 if rng.random() < probability else 0
        rows.append({
            "unit_id": unit_id,
            "x1": round(x1, 6),
            "x2": round(x2, 6),
            "x3": round(x3, 6),
            "interaction_x1_x3": round(x1 * x3, 6),
            "context": group_marker,
            "latent_signal": round(latent_signal, 6),
            "label_probability": round(probability, 6),
            "label": label,
            "interpretation": "Synthetic row for representation-learning audit; label is generated from a known latent rule."
        })
    return rows


def train_test_split(rows: list[dict[str, object]], config: RepresentationConfig):
    split = int(len(rows) * config.train_fraction)
    return rows[:split], rows[split:]


def row_features(row: dict[str, object]) -> list[float]:
    return [
        float(row["x1"]),
        float(row["x2"]),
        float(row["x3"]),
        float(row["interaction_x1_x3"]),
        1.0,
    ]


def representation_score(row: dict[str, object], weights: list[float]) -> float:
    return sigmoid(sum(weight * feature for weight, feature in zip(weights, row_features(row))))


def binary_cross_entropy(prediction: float, label: int) -> float:
    p = min(0.999999, max(0.000001, prediction))
    return -(label * math.log(p) + (1 - label) * math.log(1 - p))


def train_model(train_rows: list[dict[str, object]], config: RepresentationConfig):
    rng = random.Random(config.seed + 101)
    weights = [rng.uniform(-0.25, 0.25) for _ in range(5)]
    history: list[dict[str, object]] = []

    for epoch in range(1, config.epochs + 1):
        gradients = [0.0 for _ in weights]
        losses: list[float] = []
        for row in train_rows:
            features = row_features(row)
            pred = representation_score(row, weights)
            label = int(row["label"])
            error = pred - label
            losses.append(binary_cross_entropy(pred, label))
            for j, feature in enumerate(features):
                gradients[j] += error * feature / len(train_rows)

        for j in range(len(weights)):
            weights[j] -= config.learning_rate * gradients[j]

        if epoch == 1 or epoch % 20 == 0 or epoch == config.epochs:
            history.append({
                "epoch": epoch,
                "training_loss": round(mean(losses), 6),
                "weight_norm": round(math.sqrt(sum(w * w for w in weights)), 6),
                "interpretation": "Loss decline shows optimization behavior; it does not prove external validity."
            })

    return weights, history


def evaluate(rows: list[dict[str, object]], weights: list[float], split_name: str, threshold: float):
    predictions: list[dict[str, object]] = []
    losses: list[float] = []
    correct = 0
    for row in rows:
        pred = representation_score(row, weights)
        label = int(row["label"])
        predicted_label = 1 if pred >= threshold else 0
        correct += int(predicted_label == label)
        losses.append(binary_cross_entropy(pred, label))
        predictions.append({
            "unit_id": int(row["unit_id"]),
            "split": split_name,
            "context": row["context"],
            "label": label,
            "representation_score": round(pred, 6),
            "predicted_label": predicted_label,
            "absolute_error": round(abs(pred - label), 6),
            "interpretation": "Representation score is a learned numerical transformation, not a direct explanation."
        })
    return {
        "split": split_name,
        "n": len(rows),
        "accuracy": round(correct / len(rows), 6),
        "mean_loss": round(mean(losses), 6),
        "threshold": threshold,
        "interpretation": "Evaluation should be compared across splits and contexts."
    }, predictions


def representation_diagnostics(predictions: list[dict[str, object]]) -> dict[str, object]:
    positive_scores = [float(row["representation_score"]) for row in predictions if int(row["label"]) == 1]
    negative_scores = [float(row["representation_score"]) for row in predictions if int(row["label"]) == 0]
    context_rows: list[dict[str, object]] = []
    for context in sorted({str(row["context"]) for row in predictions}):
        subset = [row for row in predictions if row["context"] == context]
        accuracy = mean(int(row["label"]) == int(row["predicted_label"]) for row in subset)
        mean_error = mean(float(row["absolute_error"]) for row in subset)
        context_rows.append({
            "context": context,
            "n": len(subset),
            "accuracy": round(accuracy, 6),
            "mean_absolute_error": round(mean_error, 6),
            "interpretation": "Context-level diagnostics show whether representation performance varies across conditions."
        })
    return {
        "positive_mean_representation_score": round(mean(positive_scores), 6),
        "negative_mean_representation_score": round(mean(negative_scores), 6),
        "representation_gap": round(mean(positive_scores) - mean(negative_scores), 6),
        "context_rows": context_rows,
        "interpretation": "A representation gap suggests separation, but it does not prove validity, fairness, causality, or safe deployment."
    }


def embedding_similarity_rows() -> list[dict[str, object]]:
    examples = [
        ("document_a", [0.60, 0.20, 0.10, 0.40]),
        ("document_b", [0.55, 0.25, 0.12, 0.38]),
        ("document_c", [-0.10, 0.70, 0.50, 0.05]),
        ("document_d", [0.20, -0.40, 0.80, 0.10]),
    ]
    rows: list[dict[str, object]] = []
    for i, (left_name, left_vec) in enumerate(examples):
        for right_name, right_vec in examples[i + 1:]:
            dot = sum(a * b for a, b in zip(left_vec, right_vec))
            left_norm = math.sqrt(sum(a * a for a in left_vec))
            right_norm = math.sqrt(sum(b * b for b in right_vec))
            similarity = dot / (left_norm * right_norm)
            rows.append({
                "left_item": left_name,
                "right_item": right_name,
                "cosine_similarity": round(similarity, 6),
                "interpretation": "Cosine similarity is a computational comparison; semantic relevance still requires validation."
            })
    return rows


def governance_register() -> list[dict[str, object]]:
    return [
        {"item": "input_representation", "review_question": "What do the inputs omit, compress, or proxy?", "status": "needs_review"},
        {"item": "label_validity", "review_question": "Do labels reflect the construct being modeled?", "status": "needs_review"},
        {"item": "loss_function", "review_question": "Does the optimization target match the institutional purpose?", "status": "partial"},
        {"item": "generalization", "review_question": "Does performance hold beyond training conditions?", "status": "partial"},
        {"item": "context_performance", "review_question": "Are errors different across contexts or groups?", "status": "needs_review"},
        {"item": "interpretability", "review_question": "Can relevant audiences understand and challenge outputs?", "status": "needs_review"},
        {"item": "use_boundary", "review_question": "Where should the model not be used?", "status": "needs_review"},
    ]


def main() -> None:
    config = RepresentationConfig()
    rows = generate_data(config)
    train_rows, test_rows = train_test_split(rows, config)
    weights, history = train_model(train_rows, config)

    train_summary, train_predictions = evaluate(train_rows, weights, "train", config.threshold)
    test_summary, test_predictions = evaluate(test_rows, weights, "test", config.threshold)
    all_predictions = train_predictions + test_predictions
    diagnostics = representation_diagnostics(test_predictions)
    context_rows = diagnostics.pop("context_rows")
    embedding_rows = embedding_similarity_rows()
    governance_rows = governance_register()

    summary = {
        "article": "neural_networks_and_representation_learning",
        "timestamp_utc": timestamp_utc(),
        "n": config.n,
        "train_n": len(train_rows),
        "test_n": len(test_rows),
        "train_accuracy": train_summary["accuracy"],
        "test_accuracy": test_summary["accuracy"],
        "train_loss": train_summary["mean_loss"],
        "test_loss": test_summary["mean_loss"],
        "generalization_gap_loss": round(float(test_summary["mean_loss"]) - float(train_summary["mean_loss"]), 6),
        "representation_gap": diagnostics["representation_gap"],
        "governance_items_needing_review": sum(1 for row in governance_rows if row["status"] in {"partial", "needs_review"}),
        "interpretation": "Representation learning should be evaluated through performance, robustness, validity, interpretability, context behavior, and use-boundary review."
    }

    write_csv(TABLES / "synthetic_representation_records.csv", rows)
    write_csv(TABLES / "training_history.csv", history)
    write_csv(TABLES / "representation_predictions.csv", all_predictions)
    write_csv(TABLES / "model_evaluation_summary.csv", [train_summary, test_summary])
    write_csv(TABLES / "representation_diagnostics.csv", [diagnostics])
    write_csv(TABLES / "context_performance_diagnostics.csv", context_rows)
    write_csv(TABLES / "embedding_similarity_examples.csv", embedding_rows)
    write_csv(TABLES / "representation_governance_register.csv", governance_rows)
    write_csv(TABLES / "representation_audit_summary.csv", [summary])

    write_json(JSON_DIR / "representation_config.json", asdict(config))
    write_json(JSON_DIR / "training_history.json", history)
    write_json(JSON_DIR / "representation_predictions.json", all_predictions)
    write_json(JSON_DIR / "model_evaluation_summary.json", [train_summary, test_summary])
    write_json(JSON_DIR / "representation_diagnostics.json", diagnostics)
    write_json(JSON_DIR / "context_performance_diagnostics.json", context_rows)
    write_json(JSON_DIR / "embedding_similarity_examples.json", embedding_rows)
    write_json(JSON_DIR / "representation_governance_register.json", governance_rows)
    write_json(JSON_DIR / "representation_audit_summary.json", summary)

    LOGS.mkdir(parents=True, exist_ok=True)
    (LOGS / "representation_audit.log").write_text(
        "Representation learning audit completed. Review summary, diagnostics, context metrics, and governance register.\n",
        encoding="utf-8"
    )

    print("Representation learning audit complete.")
    print(TABLES / "representation_audit_summary.csv")


if __name__ == "__main__":
    main()
