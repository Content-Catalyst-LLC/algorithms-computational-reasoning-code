#!/usr/bin/env python3
"""Self-contained sensitivity-analysis calculator."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(parents=True, exist_ok=True)


def model(x: float, demand: float, capacity: float, failure: float, adaptation: float) -> float:
    return max(0.0, min(1.0, 0.5 + 0.30 * demand + 0.25 * failure - 0.20 * capacity - 0.15 * adaptation + 0.05 * x))


def finite_difference(parameter: str, baseline: dict[str, float], h: float = 0.01) -> dict[str, float | str]:
    plus = dict(baseline)
    plus[parameter] += h
    y0 = model(**baseline)
    y1 = model(**plus)
    sensitivity = (y1 - y0) / h
    normalized = ((y1 - y0) / y0) / (h / baseline[parameter]) if y0 != 0 and baseline[parameter] != 0 else 0.0
    return {
        "parameter": parameter,
        "baseline_output": round(y0, 6),
        "perturbed_output": round(y1, 6),
        "local_sensitivity": round(sensitivity, 6),
        "normalized_sensitivity": round(normalized, 6),
    }


def main() -> None:
    baseline = {"x": 1.0, "demand": 0.45, "capacity": 0.35, "failure": 0.25, "adaptation": 0.30}
    rows = [finite_difference(param, baseline) for param in ["demand", "capacity", "failure", "adaptation"]]
    path = OUT / "python_sensitivity_calculator.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(path)


if __name__ == "__main__":
    main()
