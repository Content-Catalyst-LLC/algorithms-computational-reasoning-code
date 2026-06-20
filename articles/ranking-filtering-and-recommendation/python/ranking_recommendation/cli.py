from __future__ import annotations

import argparse
import json
from .audit import read_candidates, rank_candidates


def parse_weights(raw: str) -> dict[str, float]:
    weights: dict[str, float] = {}
    for part in raw.split(","):
        key, value = part.split("=", 1)
        weights[key.strip()] = float(value)
    required = {"text_match", "quality", "freshness", "diversity_bonus", "risk_penalty"}
    missing = required - set(weights)
    if missing:
        raise ValueError(f"Missing weights: {sorted(missing)}")
    return weights


def main() -> None:
    parser = argparse.ArgumentParser(description="Rank synthetic candidates with transparent weights.")
    parser.add_argument("--weights", default="text_match=0.36,quality=0.30,freshness=0.16,diversity_bonus=0.14,risk_penalty=0.20")
    args = parser.parse_args()
    ranked = rank_candidates(read_candidates(), parse_weights(args.weights))
    print(json.dumps(ranked, indent=2))


if __name__ == "__main__":
    main()
