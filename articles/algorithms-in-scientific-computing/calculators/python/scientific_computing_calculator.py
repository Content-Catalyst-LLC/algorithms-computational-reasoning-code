# scientific_computing_calculator.py
# Self-contained educational calculators for algorithms in scientific computing.

from __future__ import annotations

from pathlib import Path
import csv
import json
import math
import random

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "calculators" / "outputs"
OUT.mkdir(parents=True, exist_ok=True)


def finite_difference_derivative(x: float = 1.0, h: float = 1e-4) -> dict[str, float]:
    estimate = (math.sin(x + h) - math.sin(x - h)) / (2.0 * h)
    true_value = math.cos(x)
    return {"x": x, "h": h, "estimate": estimate, "true_value": true_value, "absolute_error": abs(estimate - true_value)}


def trapezoid_integral(n: int = 200) -> dict[str, float]:
    a, b = 0.0, math.pi
    h = (b - a) / n
    total = 0.5 * (math.sin(a) + math.sin(b))
    for i in range(1, n):
        total += math.sin(a + i * h)
    estimate = h * total
    return {"n": n, "estimate": estimate, "true_value": 2.0, "absolute_error": abs(estimate - 2.0)}


def rk4_growth(y0: float = 1.0, rate: float = 0.4, h: float = 0.125, t_end: float = 5.0) -> dict[str, float]:
    def rhs(t: float, y: float) -> float:
        return rate * y

    t, y = 0.0, y0
    while t < t_end - 1e-12:
        step = min(h, t_end - t)
        k1 = rhs(t, y)
        k2 = rhs(t + 0.5 * step, y + 0.5 * step * k1)
        k3 = rhs(t + 0.5 * step, y + 0.5 * step * k2)
        k4 = rhs(t + step, y + step * k3)
        y += (step / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        t += step
    true_value = y0 * math.exp(rate * t_end)
    return {"estimate": y, "true_value": true_value, "absolute_error": abs(y - true_value), "h": h, "t_end": t_end}


def monte_carlo_pi(samples: int = 10000, seed: int = 42) -> dict[str, float]:
    rng = random.Random(seed)
    inside = 0
    for _ in range(samples):
        x, y = rng.random(), rng.random()
        if x * x + y * y <= 1.0:
            inside += 1
    estimate = 4.0 * inside / samples
    return {"samples": samples, "seed": seed, "estimate": estimate, "true_value": math.pi, "absolute_error": abs(estimate - math.pi)}


def main() -> None:
    results = {
        "finite_difference_derivative": finite_difference_derivative(),
        "trapezoid_integral": trapezoid_integral(),
        "rk4_growth": rk4_growth(),
        "monte_carlo_pi": monte_carlo_pi(),
    }
    (OUT / "scientific_computing_calculator_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    with (OUT / "scientific_computing_calculator_results.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["calculator", "metric", "value"])
        for calculator, metrics in results.items():
            for metric, value in metrics.items():
                writer.writerow([calculator, metric, value])
    print("Scientific computing calculators complete.")


if __name__ == "__main__":
    main()
