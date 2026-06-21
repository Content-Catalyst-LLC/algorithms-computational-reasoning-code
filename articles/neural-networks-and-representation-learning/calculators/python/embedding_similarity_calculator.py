from __future__ import annotations
import argparse
import math


def parse_vector(raw: str) -> list[float]:
    return [float(part.strip()) for part in raw.split(",") if part.strip()]


def cosine(left: list[float], right: list[float]) -> float:
    if len(left) != len(right):
        raise ValueError("Vectors must have the same length.")
    dot = sum(a * b for a, b in zip(left, right))
    left_norm = math.sqrt(sum(a * a for a in left))
    right_norm = math.sqrt(sum(b * b for b in right))
    if left_norm == 0 or right_norm == 0:
        raise ValueError("Cosine similarity is undefined for zero vectors.")
    return dot / (left_norm * right_norm)


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute cosine similarity between two embedding vectors.")
    parser.add_argument("--left", required=True, help="Comma-separated vector, e.g. 0.6,0.2,0.1")
    parser.add_argument("--right", required=True, help="Comma-separated vector, e.g. 0.5,0.1,0.2")
    args = parser.parse_args()
    similarity = cosine(parse_vector(args.left), parse_vector(args.right))
    print(f"cosine_similarity={similarity:.6f}")


if __name__ == "__main__":
    main()
