#!/usr/bin/env python3
"""Self-contained calculator for Pareto and weighted-score trade-off reasoning."""

from __future__ import annotations

from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "calculators" / "outputs"
OUT.mkdir(parents=True, exist_ok=True)

ALTERNATIVES = [
    {"alternative": "A", "cost": 72, "risk": 34, "service_quality": 82},
    {"alternative": "B", "cost": 64, "risk": 41, "service_quality": 76},
    {"alternative": "C", "cost": 81, "risk": 26, "service_quality": 88},
    {"alternative": "D", "cost": 58, "risk": 52, "service_quality": 69},
]


def normalize_min(value: float, values: list[float]) -> float:
    return (max(values) - value) / (max(values) - min(values)) if max(values) != min(values) else 1.0


def normalize_max(value: float, values: list[float]) -> float:
    return (value - min(values)) / (max(values) - min(values)) if max(values) != min(values) else 1.0


def main() -> None:
    costs = [float(row["cost"]) for row in ALTERNATIVES]
    risks = [float(row["risk"]) for row in ALTERNATIVES]
    qualities = [float(row["service_quality"]) for row in ALTERNATIVES]
    rows = []
    for row in ALTERNATIVES:
        score = (
            0.35 * normalize_min(float(row["cost"]), costs)
            + 0.30 * normalize_min(float(row["risk"]), risks)
            + 0.35 * normalize_max(float(row["service_quality"]), qualities)
        )
        rows.append({**row, "weighted_score": round(score, 6)})

    rows.sort(key=lambda item: item["weighted_score"], reverse=True)
    with (OUT / "tradeoff_calculator_weighted_scores.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    (OUT / "tradeoff_calculator_weighted_scores.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")
    print("Top alternative:", rows[0]["alternative"])


if __name__ == "__main__":
    main()
