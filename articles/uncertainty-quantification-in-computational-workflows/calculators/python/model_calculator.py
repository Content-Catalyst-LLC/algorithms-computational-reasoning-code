#!/usr/bin/env python3
"""Self-contained uncertainty quantification calculator."""

from __future__ import annotations

import argparse
import json
import random
from statistics import mean, pstdev
from pathlib import Path


def bounded_normal(rng: random.Random, center: float, spread: float) -> float:
    return max(0.0, min(1.0, rng.gauss(center, spread)))


def model(demand: float, capacity: float, failure_rate: float, adaptation_rate: float, noise: float = 0.0) -> float:
    return max(0.0, min(1.0, 0.42 + 0.38 * demand - 0.31 * capacity + 0.27 * failure_rate - 0.18 * adaptation_rate + noise))


def run_ensemble(runs: int, threshold: float, seed: int) -> dict[str, float | int]:
    rng = random.Random(seed)
    values: list[float] = []
    for _ in range(runs):
        demand = bounded_normal(rng, 0.55, 0.12)
        capacity = bounded_normal(rng, 0.50, 0.10)
        failure_rate = bounded_normal(rng, 0.22, 0.08)
        adaptation_rate = bounded_normal(rng, 0.30, 0.10)
        noise = rng.gauss(0.0, 0.035)
        values.append(model(demand, capacity, failure_rate, adaptation_rate, noise))
    return {
        "runs": runs,
        "threshold": threshold,
        "mean": round(mean(values), 6),
        "std": round(pstdev(values), 6),
        "min": round(min(values), 6),
        "max": round(max(values), 6),
        "exceedance_probability": round(sum(v >= threshold for v in values) / runs, 6),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["single", "ensemble"], default="ensemble")
    parser.add_argument("--runs", type=int, default=1000)
    parser.add_argument("--threshold", type=float, default=0.62)
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument("--demand", type=float, default=0.55)
    parser.add_argument("--capacity", type=float, default=0.50)
    parser.add_argument("--failure-rate", type=float, default=0.22)
    parser.add_argument("--adaptation-rate", type=float, default=0.30)
    args = parser.parse_args()

    if args.mode == "single":
        payload = {"risk_score": round(model(args.demand, args.capacity, args.failure_rate, args.adaptation_rate), 6)}
    else:
        payload = run_ensemble(args.runs, args.threshold, args.seed)

    out_dir = Path(__file__).resolve().parents[1] / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "python_calculator_result.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
