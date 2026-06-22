from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute calibration gap.")
    parser.add_argument("--mean-score", type=float, required=True)
    parser.add_argument("--observed-rate", type=float, required=True)
    args = parser.parse_args()

    gap = abs(args.mean_score - args.observed_rate)
    print(f"calibration_gap={gap:.6f}")


if __name__ == "__main__":
    main()
