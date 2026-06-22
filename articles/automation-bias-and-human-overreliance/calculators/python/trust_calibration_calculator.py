from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute trust calibration error.")
    parser.add_argument("--reliance", type=float, required=True)
    parser.add_argument("--quality", type=float, required=True)
    args = parser.parse_args()

    gap = abs(args.reliance - args.quality)
    print(f"reliance={args.reliance:.6f}")
    print(f"quality={args.quality:.6f}")
    print(f"trust_calibration_error={gap:.6f}")


if __name__ == "__main__":
    main()
