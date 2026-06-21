from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute train-test generalization gap.")
    parser.add_argument("--train-metric", type=float, required=True)
    parser.add_argument("--test-metric", type=float, required=True)
    args = parser.parse_args()
    gap = args.train_metric - args.test_metric
    print(f"train_metric={args.train_metric:.6f}")
    print(f"test_metric={args.test_metric:.6f}")
    print(f"generalization_gap={gap:.6f}")


if __name__ == "__main__":
    main()
