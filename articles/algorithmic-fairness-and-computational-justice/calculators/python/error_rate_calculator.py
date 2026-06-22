from __future__ import annotations

import argparse


def safe_rate(numerator: float, denominator: float) -> float:
    return 0.0 if denominator == 0 else numerator / denominator


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute error rates.")
    parser.add_argument("--tp", type=float, required=True)
    parser.add_argument("--fp", type=float, required=True)
    parser.add_argument("--fn", type=float, required=True)
    parser.add_argument("--tn", type=float, required=True)
    args = parser.parse_args()

    actual_positive = args.tp + args.fn
    actual_negative = args.fp + args.tn
    print(f"false_positive_rate={safe_rate(args.fp, actual_negative):.6f}")
    print(f"false_negative_rate={safe_rate(args.fn, actual_positive):.6f}")
    print(f"true_positive_rate={safe_rate(args.tp, actual_positive):.6f}")


if __name__ == "__main__":
    main()
