#!/usr/bin/env python3
"""Self-contained cosine similarity calculator for recommendation examples."""
from __future__ import annotations

import argparse
import math


def parse_vector(raw: str) -> list[float]:
    return [float(part.strip()) for part in raw.split(",") if part.strip()]


def cosine(left: list[float], right: list[float]) -> float:
    if len(left) != len(right):
        raise ValueError("Vectors must have the same length")
    dot = sum(a * b for a, b in zip(left, right))
    left_norm = math.sqrt(sum(a * a for a in left))
    right_norm = math.sqrt(sum(b * b for b in right))
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return round(dot / (left_norm * right_norm), 6)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--left", required=True, help="Comma-separated numeric vector")
    parser.add_argument("--right", required=True, help="Comma-separated numeric vector")
    args = parser.parse_args()
    print(cosine(parse_vector(args.left), parse_vector(args.right)))


if __name__ == "__main__":
    main()
