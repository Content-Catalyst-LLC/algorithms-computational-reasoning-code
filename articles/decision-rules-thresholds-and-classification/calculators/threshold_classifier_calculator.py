from __future__ import annotations

import argparse


def classify(score: float, threshold: float) -> int:
    return 1 if score >= threshold else 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Classify a score using a threshold.")
    parser.add_argument("--score", type=float, required=True)
    parser.add_argument("--threshold", type=float, default=0.5)
    args = parser.parse_args()

    label = classify(args.score, args.threshold)
    print(label)


if __name__ == "__main__":
    main()
