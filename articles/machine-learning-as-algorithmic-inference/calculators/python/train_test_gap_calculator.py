from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a simple train/test performance gap.")
    parser.add_argument("--train-metric", type=float, required=True)
    parser.add_argument("--test-metric", type=float, required=True)
    parser.add_argument("--warning-gap", type=float, default=0.05)
    args = parser.parse_args()
    gap = args.train_metric - args.test_metric
    print(f"train_metric={args.train_metric:.6f}")
    print(f"test_metric={args.test_metric:.6f}")
    print(f"train_test_gap={gap:.6f}")
    print(f"review_flag={abs(gap) >= args.warning_gap}")


if __name__ == "__main__":
    main()
