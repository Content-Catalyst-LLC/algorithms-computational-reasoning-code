from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute weighted multi-criteria decision score.")
    parser.add_argument("--effectiveness", type=float, required=True)
    parser.add_argument("--equity", type=float, required=True)
    parser.add_argument("--feasibility", type=float, required=True)
    parser.add_argument("--reversibility", type=float, required=True)
    parser.add_argument("--legitimacy", type=float, required=True)
    parser.add_argument("--weights", type=str, default="0.25,0.25,0.20,0.15,0.15")
    args = parser.parse_args()

    weights = [float(part.strip()) for part in args.weights.split(",")]
    values = [args.effectiveness, args.equity, args.feasibility, args.reversibility, args.legitimacy]
    if len(weights) != len(values):
        raise SystemExit("weights must contain exactly five comma-separated values")
    weight_sum = sum(weights)
    if weight_sum <= 0:
        raise SystemExit("weights must sum to a positive value")
    normalized = [weight / weight_sum for weight in weights]
    score = sum(weight * value for weight, value in zip(normalized, values))
    print(f"multi_criteria_decision_score={score:.6f}")


if __name__ == "__main__":
    main()
