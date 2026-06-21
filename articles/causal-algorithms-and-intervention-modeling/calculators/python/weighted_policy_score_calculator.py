from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a simple weighted policy score for intervention review.")
    parser.add_argument("--effect", type=float, required=True)
    parser.add_argument("--equity", type=float, required=True)
    parser.add_argument("--feasibility", type=float, required=True)
    parser.add_argument("--cost", type=float, required=True)
    args = parser.parse_args()
    score = 0.40 * args.effect + 0.25 * args.equity + 0.25 * args.feasibility - 0.10 * args.cost
    print(f"weighted_policy_score={score:.6f}")


if __name__ == "__main__":
    main()
