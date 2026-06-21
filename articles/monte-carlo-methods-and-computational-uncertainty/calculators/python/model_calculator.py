#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
import random
from statistics import mean, pstdev


def ci(values: list[float]) -> tuple[float, float, float, float]:
    n = len(values)
    estimate = mean(values)
    sd = pstdev(values) if n > 1 else 0.0
    se = sd / math.sqrt(n) if n > 1 else 0.0
    return estimate, se, estimate - 1.96 * se, estimate + 1.96 * se


def pi_estimate(samples: int, seed: int) -> None:
    rng = random.Random(seed)
    vals = []
    for _ in range(samples):
        x = rng.random(); y = rng.random()
        vals.append(4.0 if x * x + y * y <= 1.0 else 0.0)
    estimate, se, lower, upper = ci(vals)
    print(f"pi_estimate={estimate:.8f}")
    print(f"standard_error={se:.8f}")
    print(f"lower_95={lower:.8f}")
    print(f"upper_95={upper:.8f}")
    print(f"absolute_error={abs(estimate - math.pi):.8f}")


def threshold_risk(samples: int, seed: int, threshold: float) -> None:
    rng = random.Random(seed)
    vals = []
    for _ in range(samples):
        base = rng.triangular(900000, 1100000, 1000000)
        labor = max(0.75, rng.gauss(1.0, 0.08))
        delay = max(0.0, rng.gauss(60000, 35000))
        contingency = rng.uniform(20000, 120000)
        vals.append(1.0 if base * labor + delay + contingency > threshold else 0.0)
    estimate, se, lower, upper = ci(vals)
    print(f"threshold_probability={estimate:.6f}")
    print(f"standard_error={se:.6f}")
    print(f"lower_95={lower:.6f}")
    print(f"upper_95={upper:.6f}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Monte Carlo uncertainty calculator")
    parser.add_argument("mode", choices=["pi", "threshold"])
    parser.add_argument("--samples", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--threshold", type=float, default=1250000)
    args = parser.parse_args()
    if args.mode == "pi":
        pi_estimate(args.samples, args.seed)
    else:
        threshold_risk(args.samples, args.seed, args.threshold)


if __name__ == "__main__":
    main()
