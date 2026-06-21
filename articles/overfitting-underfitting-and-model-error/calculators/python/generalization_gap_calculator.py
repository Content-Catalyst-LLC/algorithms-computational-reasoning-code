from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a generalization gap from train and test error.")
    parser.add_argument("--train-error", type=float, required=True)
    parser.add_argument("--test-error", type=float, required=True)
    args = parser.parse_args()
    gap = args.test_error - args.train_error
    ratio = args.test_error / args.train_error if args.train_error != 0 else float("inf")
    print(f"train_error={args.train_error:.6f}")
    print(f"test_error={args.test_error:.6f}")
    print(f"generalization_gap={gap:.6f}")
    print(f"test_to_train_ratio={ratio:.6f}")


if __name__ == "__main__":
    main()
