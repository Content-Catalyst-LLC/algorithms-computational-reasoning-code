#!/usr/bin/env python3
"""Self-contained ranking score calculator for website reuse."""
from __future__ import annotations

import argparse


def score(text_match: float, quality: float, freshness: float, diversity_bonus: float, risk_penalty: float) -> float:
    return round(0.36 * text_match + 0.30 * quality + 0.16 * freshness + 0.14 * diversity_bonus - 0.20 * risk_penalty, 6)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--text-match", type=float, required=True)
    parser.add_argument("--quality", type=float, required=True)
    parser.add_argument("--freshness", type=float, required=True)
    parser.add_argument("--diversity-bonus", type=float, required=True)
    parser.add_argument("--risk-penalty", type=float, required=True)
    args = parser.parse_args()
    print(score(args.text_match, args.quality, args.freshness, args.diversity_bonus, args.risk_penalty))


if __name__ == "__main__":
    main()
