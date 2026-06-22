from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute automation reliance score.")
    parser.add_argument("--accepted-recommendations", type=float, required=True)
    parser.add_argument("--total-recommendations", type=float, required=True)
    args = parser.parse_args()

    score = 0.0 if args.total_recommendations == 0 else args.accepted_recommendations / args.total_recommendations
    print(f"reliance_score={score:.6f}")


if __name__ == "__main__":
    main()
