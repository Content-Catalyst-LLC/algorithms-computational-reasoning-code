from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute weighted search relevance.")
    parser.add_argument("--text-match", type=float, required=True)
    parser.add_argument("--semantic-similarity", type=float, required=True)
    parser.add_argument("--authority", type=float, required=True)
    parser.add_argument("--freshness", type=float, required=True)
    parser.add_argument("--weights", type=str, default="0.35,0.35,0.20,0.10")
    args = parser.parse_args()

    weights = [float(part.strip()) for part in args.weights.split(",")]
    values = [args.text_match, args.semantic_similarity, args.authority, args.freshness]
    if len(weights) != len(values):
        raise SystemExit("weights must contain exactly four comma-separated values")
    total = sum(weights)
    if total <= 0:
        raise SystemExit("weights must sum to a positive value")
    score = sum((w / total) * v for w, v in zip(weights, values))
    print(f"weighted_relevance_score={score:.6f}")


if __name__ == "__main__":
    main()
