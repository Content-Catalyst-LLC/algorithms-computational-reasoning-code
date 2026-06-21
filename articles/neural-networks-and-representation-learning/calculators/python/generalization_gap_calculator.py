from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a generalization gap from train and test loss.")
    parser.add_argument("--train-loss", type=float, required=True)
    parser.add_argument("--test-loss", type=float, required=True)
    args = parser.parse_args()
    gap = args.test_loss - args.train_loss
    print(f"train_loss={args.train_loss:.6f}")
    print(f"test_loss={args.test_loss:.6f}")
    print(f"generalization_gap={gap:.6f}")


if __name__ == "__main__":
    main()
