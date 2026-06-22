from __future__ import annotations

import argparse
import math


def parse_vector(text: str) -> list[float]:
    return [float(part.strip()) for part in text.split(",") if part.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute cosine similarity.")
    parser.add_argument("--x", type=str, required=True, help="Comma-separated vector")
    parser.add_argument("--y", type=str, required=True, help="Comma-separated vector")
    args = parser.parse_args()

    x = parse_vector(args.x)
    y = parse_vector(args.y)
    if len(x) != len(y):
        raise SystemExit("vectors must have same length")
    dot = sum(a * b for a, b in zip(x, y))
    norm_x = math.sqrt(sum(a * a for a in x))
    norm_y = math.sqrt(sum(b * b for b in y))
    if norm_x == 0 or norm_y == 0:
        raise SystemExit("vectors must be nonzero")
    score = dot / (norm_x * norm_y)
    print(f"cosine_similarity={score:.6f}")


if __name__ == "__main__":
    main()
