from __future__ import annotations
import argparse
import math


def sigmoid(value: float) -> float:
    return 1.0 / (1.0 + math.exp(-value))


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a simple neural-style representation score.")
    parser.add_argument("--x1", type=float, required=True)
    parser.add_argument("--x2", type=float, required=True)
    parser.add_argument("--x3", type=float, required=True)
    parser.add_argument("--w1", type=float, default=0.9)
    parser.add_argument("--w2", type=float, default=-0.7)
    parser.add_argument("--w3", type=float, default=0.35)
    parser.add_argument("--bias", type=float, default=0.0)
    args = parser.parse_args()
    linear = args.w1 * args.x1 + args.w2 * args.x2 + args.w3 * args.x3 + args.bias
    score = sigmoid(linear)
    print(f"linear_signal={linear:.6f}")
    print(f"representation_score={score:.6f}")


if __name__ == "__main__":
    main()
