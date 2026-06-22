from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute accountability capacity score.")
    parser.add_argument("--explanation-quality", type=float, required=True)
    parser.add_argument("--transparency-capacity", type=float, required=True)
    parser.add_argument("--contestability", type=float, required=True)
    parser.add_argument("--governance", type=float, required=True)
    args = parser.parse_args()

    score = (args.explanation_quality + args.transparency_capacity + args.contestability + args.governance) / 4.0
    print(f"accountability_capacity_score={score:.6f}")


if __name__ == "__main__":
    main()
