from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute selection-rate gap.")
    parser.add_argument("--rates", type=float, nargs="+", required=True)
    args = parser.parse_args()

    gap = max(args.rates) - min(args.rates)
    print(f"selection_gap={gap:.6f}")


if __name__ == "__main__":
    main()
