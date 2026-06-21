from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Estimate feature change needed to cross a decision threshold.")
    parser.add_argument("--score", type=float, required=True)
    parser.add_argument("--threshold", type=float, required=True)
    parser.add_argument("--feature-weight", type=float, required=True)
    args = parser.parse_args()
    gap = args.threshold - args.score
    required_delta = 0.0 if gap <= 0 else gap / args.feature_weight
    print(f"score={args.score:.6f}")
    print(f"threshold={args.threshold:.6f}")
    print(f"gap={gap:.6f}")
    print(f"required_delta={required_delta:.6f}")


if __name__ == "__main__":
    main()
