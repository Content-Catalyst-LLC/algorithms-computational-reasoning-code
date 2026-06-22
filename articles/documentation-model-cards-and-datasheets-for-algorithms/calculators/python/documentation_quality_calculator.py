from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute documentation quality.")
    parser.add_argument("--accuracy", type=float, required=True)
    parser.add_argument("--completeness", type=float, required=True)
    parser.add_argument("--specificity", type=float, required=True)
    parser.add_argument("--timeliness", type=float, required=True)
    parser.add_argument("--accessibility", type=float, required=True)
    parser.add_argument("--actionability", type=float, required=True)
    args = parser.parse_args()

    score = (
        args.accuracy
        + args.completeness
        + args.specificity
        + args.timeliness
        + args.accessibility
        + args.actionability
    ) / 6.0
    print(f"documentation_quality_score={score:.6f}")


if __name__ == "__main__":
    main()
