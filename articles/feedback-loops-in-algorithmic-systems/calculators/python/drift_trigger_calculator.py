from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Flag distribution-shift review.")
    parser.add_argument("--distance", type=float, required=True)
    parser.add_argument("--threshold", type=float, default=0.25)
    args = parser.parse_args()

    review = int(args.distance > args.threshold)
    print(f"distribution_distance={args.distance:.6f}")
    print(f"threshold={args.threshold:.6f}")
    print(f"review_trigger={review}")


if __name__ == "__main__":
    main()
