# Self-contained gradient descent calculator.
# Writes calculator outputs for learning-rate sensitivity and final parameter estimates.

from __future__ import annotations

from pathlib import Path
import csv
import json

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
OUTPUTS = ARTICLE_ROOT / "calculators" / "outputs"


def data() -> list[tuple[float, float]]:
    return [
        (-2.0, -2.85),
        (-1.5, -1.77),
        (-1.0, -0.67),
        (-0.5, 0.32),
        (0.0, 1.47),
        (0.5, 2.64),
        (1.0, 3.63),
        (1.5, 4.87),
        (2.0, 5.82),
    ]


def mse(weight: float, bias: float) -> float:
    rows = data()
    return sum((y - (weight * x + bias)) ** 2 for x, y in rows) / len(rows)


def step(weight: float, bias: float, rate: float) -> tuple[float, float]:
    rows = data()
    n = len(rows)
    grad_w = sum((2 / n) * ((weight * x + bias) - y) * x for x, y in rows)
    grad_b = sum((2 / n) * ((weight * x + bias) - y) for x, y in rows)
    return weight - rate * grad_w, bias - rate * grad_b


def train(rate: float = 0.08, steps: int = 80) -> list[dict[str, float]]:
    weight = 0.0
    bias = 0.0
    trace: list[dict[str, float]] = []

    for i in range(steps + 1):
        trace.append({
            "step": i,
            "learning_rate": rate,
            "weight": round(weight, 6),
            "bias": round(bias, 6),
            "loss": round(mse(weight, bias), 6),
        })
        if i < steps:
            weight, bias = step(weight, bias, rate)
    return trace


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = sorted({key for row in rows for key in row})
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    trace = train()
    sensitivity = []
    for rate in [0.005, 0.02, 0.08, 0.20, 0.50]:
        rate_trace = train(rate=rate, steps=40)
        sensitivity.append(rate_trace[-1])

    write_csv(OUTPUTS / "gradient_descent_calculator_trace.csv", trace)
    write_csv(OUTPUTS / "learning_rate_sensitivity_calculator.csv", sensitivity)
    (OUTPUTS / "gradient_descent_calculator_trace.json").write_text(json.dumps(trace, indent=2), encoding="utf-8")
    (OUTPUTS / "learning_rate_sensitivity_calculator.json").write_text(json.dumps(sensitivity, indent=2), encoding="utf-8")
    print("Gradient descent calculator complete.")


if __name__ == "__main__":
    main()
