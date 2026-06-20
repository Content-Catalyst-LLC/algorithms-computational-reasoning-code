#!/usr/bin/env python3
"""Small secure-communication governance calculator.

This calculator scores governance readiness. It does not implement production
cryptography.
"""

from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ARTICLE_ROOT / "calculators" / "outputs" / "secure_communication_calculator.csv"


def score_case(values: dict[str, float]) -> float:
    weights = {
        "threat_model": 0.12,
        "protocols": 0.10,
        "keys": 0.14,
        "validation": 0.10,
        "integrity": 0.10,
        "authentication": 0.10,
        "randomness": 0.08,
        "secret_storage": 0.10,
        "rotation": 0.08,
        "implementation_review": 0.08,
    }
    return round(100 * sum(weights[key] * values[key] for key in weights), 3)


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    rows = [
        {
            "case": "standard secure channel",
            "score": score_case({
                "threat_model": 0.86,
                "protocols": 0.88,
                "keys": 0.82,
                "validation": 0.90,
                "integrity": 0.86,
                "authentication": 0.84,
                "randomness": 0.84,
                "secret_storage": 0.82,
                "rotation": 0.78,
                "implementation_review": 0.80,
            }),
        },
        {
            "case": "legacy manual transfer",
            "score": score_case({
                "threat_model": 0.36,
                "protocols": 0.28,
                "keys": 0.24,
                "validation": 0.18,
                "integrity": 0.34,
                "authentication": 0.28,
                "randomness": 0.30,
                "secret_storage": 0.22,
                "rotation": 0.16,
                "implementation_review": 0.20,
            }),
        },
    ]

    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["case", "score"])
        writer.writeheader()
        writer.writerows(rows)

    for row in rows:
        print(f"{row['case']}: {row['score']}")
    print(OUTPUT)


if __name__ == "__main__":
    main()
