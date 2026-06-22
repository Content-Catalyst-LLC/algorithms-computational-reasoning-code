from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute calibration gap.")
    parser.add_argument("--accuracy", type=float, required=True)
    parser.add_argument("--confidence", type=float, required=True)
    args = parser.parse_args()

    gap = abs(args.confidence - args.accuracy)
    print(f"accuracy={args.accuracy:.6f}")
    print(f"confidence={args.confidence:.6f}")
    print(f"calibration_gap={gap:.6f}")


if __name__ == "__main__":
    main()
