from __future__ import annotations

from machine_learning_algorithmic_inference_audit import (
    default_config,
    generate_synthetic_data,
    train_test_split,
    train_logistic_regression,
    attach_predictions,
    metrics,
    calibration_bins,
)


def assert_between(value: float, low: float, high: float, label: str) -> None:
    if not (low <= value <= high):
        raise AssertionError(f"{label}={value} outside [{low}, {high}]")


def main() -> None:
    config = default_config()
    rows = generate_synthetic_data(config)
    if len(rows) != config.n:
        raise AssertionError("Synthetic data row count does not match config.n")
    train, test = train_test_split(rows, config.train_fraction)
    if not train or not test:
        raise AssertionError("Train/test split should produce non-empty partitions")
    model = train_logistic_regression(train, config)
    test_predictions = attach_predictions(test, model, "test")
    for row in test_predictions[:25]:
        assert_between(float(row["model_score"]), 0.0, 1.0, "model_score")
    result = metrics(test_predictions, 0.50, "test")
    assert_between(float(result["accuracy"]), 0.0, 1.0, "accuracy")
    assert_between(float(result["false_positive_rate"]), 0.0, 1.0, "false_positive_rate")
    assert_between(float(result["false_negative_rate"]), 0.0, 1.0, "false_negative_rate")
    bins = calibration_bins(test_predictions)
    if not bins:
        raise AssertionError("Calibration bins should not be empty")
    print("Machine learning workflow tests passed.")


if __name__ == "__main__":
    main()
