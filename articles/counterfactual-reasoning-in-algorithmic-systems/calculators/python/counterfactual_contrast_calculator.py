from __future__ import annotations
import argparse


def label(score: float, threshold: float) -> str:
    return "favorable" if score >= threshold else "not_favorable"


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare original and counterfactual scores.")
    parser.add_argument("--original-score", type=float, required=True)
    parser.add_argument("--counterfactual-score", type=float, required=True)
    parser.add_argument("--threshold", type=float, required=True)
    args = parser.parse_args()
    original_label = label(args.original_score, args.threshold)
    counterfactual_label = label(args.counterfactual_score, args.threshold)
    print(f"original_label={original_label}")
    print(f"counterfactual_label={counterfactual_label}")
    print(f"score_change={args.counterfactual_score - args.original_score:.6f}")
    print(f"decision_flipped={original_label != counterfactual_label}")


if __name__ == "__main__":
    main()
