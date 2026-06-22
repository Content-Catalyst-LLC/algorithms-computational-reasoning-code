from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute human review capacity score.")
    parser.add_argument("--time", type=float, required=True)
    parser.add_argument("--information", type=float, required=True)
    parser.add_argument("--authority", type=float, required=True)
    parser.add_argument("--training", type=float, required=True)
    parser.add_argument("--protection", type=float, required=True)
    args = parser.parse_args()

    score = (args.time + args.information + args.authority + args.training + args.protection) / 5.0
    print(f"review_capacity_score={score:.6f}")


if __name__ == "__main__":
    main()
