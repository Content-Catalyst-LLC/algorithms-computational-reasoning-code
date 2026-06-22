from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute link recommendation score.")
    parser.add_argument("--semantic-similarity", type=float, required=True)
    parser.add_argument("--prerequisite-value", type=float, required=True)
    parser.add_argument("--graph-navigation-value", type=float, required=True)
    parser.add_argument("--weights", type=str, default="0.50,0.30,0.20")
    args = parser.parse_args()

    weights = [float(part.strip()) for part in args.weights.split(",")]
    values = [args.semantic_similarity, args.prerequisite_value, args.graph_navigation_value]
    if len(weights) != len(values):
        raise SystemExit("weights must contain exactly three comma-separated values")
    total = sum(weights)
    if total <= 0:
        raise SystemExit("weights must sum to a positive value")
    score = sum((w / total) * v for w, v in zip(weights, values))
    print(f"link_recommendation_score={score:.6f}")


if __name__ == "__main__":
    main()
