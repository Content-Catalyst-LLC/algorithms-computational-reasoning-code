from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Combine delta, unit cost, and feasibility into a review score.")
    parser.add_argument("--delta", type=float, required=True)
    parser.add_argument("--unit-cost", type=float, required=True)
    parser.add_argument("--feasibility", type=float, required=True, help="0 to 1 feasibility rating")
    args = parser.parse_args()
    burden = abs(args.delta) * args.unit_cost
    feasibility = max(0.0, min(1.0, args.feasibility))
    score = feasibility / (1.0 + burden)
    print(f"burden={burden:.6f}")
    print(f"feasibility={feasibility:.6f}")
    print(f"review_score={score:.6f}")


if __name__ == "__main__":
    main()
