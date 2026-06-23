from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Classify a medieval-style mathematical problem from a controlled vocabulary.")
parser.add_argument("--domain", choices=["arithmetic", "algebra", "commercial", "inheritance", "table", "geometric"], required=True)
args = parser.parse_args()

procedures = {
    "arithmetic": "select written reckoning operation",
    "algebra": "identify unknowns and equation type",
    "commercial": "identify rate, unit, price, share, or debt rule",
    "inheritance": "identify heirs, shares, remainder, and adjustment",
    "table": "select lookup, correction, or interpolation procedure",
    "geometric": "select area, length, proportion, or demonstration procedure",
}
print(f"procedure_family={procedures[args.domain]}")
