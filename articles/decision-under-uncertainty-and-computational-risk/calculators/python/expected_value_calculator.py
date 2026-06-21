from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute expected net value under uncertainty.")
    parser.add_argument("--probability", type=float, required=True)
    parser.add_argument("--benefit", type=float, required=True)
    parser.add_argument("--loss", type=float, required=True)
    parser.add_argument("--cost", type=float, required=True)
    args = parser.parse_args()
    p = max(0.0, min(1.0, args.probability))
    expected_value = p * args.benefit - p * args.loss - args.cost
    print(f"probability={p:.6f}")
    print(f"expected_value={expected_value:.6f}")


if __name__ == "__main__":
    main()
