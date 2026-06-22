from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute automation reliance score.")
    parser.add_argument("--automated-final-actions", type=float, required=True)
    parser.add_argument("--total-decisions", type=float, required=True)
    args = parser.parse_args()

    score = 0.0 if args.total_decisions == 0 else args.automated_final_actions / args.total_decisions
    print(f"automation_reliance_score={score:.6f}")


if __name__ == "__main__":
    main()
