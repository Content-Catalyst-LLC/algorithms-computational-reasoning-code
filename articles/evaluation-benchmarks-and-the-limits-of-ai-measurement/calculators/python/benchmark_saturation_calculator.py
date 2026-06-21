from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Flag benchmark saturation.")
    parser.add_argument("--score", type=float, required=True)
    parser.add_argument("--threshold", type=float, default=0.90)
    args = parser.parse_args()

    saturated = int(args.score >= args.threshold)
    print(f"score={args.score:.6f}")
    print(f"threshold={args.threshold:.6f}")
    print(f"saturated={saturated}")


if __name__ == "__main__":
    main()
