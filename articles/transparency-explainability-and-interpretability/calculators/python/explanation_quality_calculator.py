from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute explanation quality score.")
    parser.add_argument("--faithfulness", type=float, required=True)
    parser.add_argument("--stability", type=float, required=True)
    parser.add_argument("--understandability", type=float, required=True)
    parser.add_argument("--actionability", type=float, required=True)
    parser.add_argument("--uncertainty", type=float, required=True)
    args = parser.parse_args()

    score = (args.faithfulness + args.stability + args.understandability + args.actionability + args.uncertainty) / 5.0
    print(f"explanation_quality_score={score:.6f}")


if __name__ == "__main__":
    main()
