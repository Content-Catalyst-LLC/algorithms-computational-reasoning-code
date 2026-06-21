#!/usr/bin/env python3
"""Reusable probability calculators for probabilistic algorithm examples."""
from __future__ import annotations

import argparse
import json
import math
from statistics import mean, pstdev


def expected_value(values: list[float], probabilities: list[float]) -> float:
    if len(values) != len(probabilities):
        raise ValueError("values and probabilities must have the same length")
    total_p = sum(probabilities)
    if total_p <= 0:
        raise ValueError("probabilities must sum to a positive value")
    normalized = [p / total_p for p in probabilities]
    return sum(v * p for v, p in zip(values, normalized))


def variance(values: list[float], probabilities: list[float]) -> float:
    mu = expected_value(values, probabilities)
    total_p = sum(probabilities)
    normalized = [p / total_p for p in probabilities]
    return sum(((v - mu) ** 2) * p for v, p in zip(values, normalized))


def bernoulli_standard_error(p_hat: float, n: int) -> float:
    if n <= 0:
        raise ValueError("n must be positive")
    return math.sqrt(max(p_hat * (1.0 - p_hat), 0.0) / n)


def confidence_interval(p_hat: float, n: int, z: float = 1.96) -> tuple[float, float]:
    se = bernoulli_standard_error(p_hat, n)
    return max(0.0, p_hat - z * se), min(1.0, p_hat + z * se)


def repeated_failure_probability(p: float, k: int) -> float:
    return p ** k


def expected_loss(probability: float, loss_false_positive: float, loss_false_negative: float) -> dict[str, float | int]:
    act_loss = (1.0 - probability) * loss_false_positive
    no_act_loss = probability * loss_false_negative
    return {
        "expected_loss_if_act": act_loss,
        "expected_loss_if_do_not_act": no_act_loss,
        "choose_action": int(act_loss <= no_act_loss),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Probability calculator layer")
    parser.add_argument("--p-hat", type=float, default=0.57)
    parser.add_argument("--n", type=int, default=1000)
    parser.add_argument("--failure-probability", type=float, default=0.10)
    parser.add_argument("--trials", type=int, default=5)
    parser.add_argument("--event-probability", type=float, default=0.60)
    args = parser.parse_args()

    lower, upper = confidence_interval(args.p_hat, args.n)
    payload = {
        "p_hat": args.p_hat,
        "n": args.n,
        "standard_error": bernoulli_standard_error(args.p_hat, args.n),
        "confidence_interval_95": [lower, upper],
        "repeated_failure_probability": repeated_failure_probability(args.failure_probability, args.trials),
        "expected_loss_decision": expected_loss(args.event_probability, 1.0, 3.0),
        "example_expected_value": expected_value([0, 1, 2], [0.2, 0.5, 0.3]),
        "example_variance": variance([0, 1, 2], [0.2, 0.5, 0.3]),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
