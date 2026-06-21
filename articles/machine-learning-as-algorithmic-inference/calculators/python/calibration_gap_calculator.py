from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute calibration gap for a probability bin.")
    parser.add_argument("--average-score", type=float, required=True)
    parser.add_argument("--observed-rate", type=float, required=True)
    args = parser.parse_args()
    gap = abs(args.average_score - args.observed_rate)
    print(f"average_score={args.average_score:.6f}")
    print(f"observed_rate={args.observed_rate:.6f}")
    print(f"absolute_calibration_gap={gap:.6f}")


if __name__ == "__main__":
    main()
