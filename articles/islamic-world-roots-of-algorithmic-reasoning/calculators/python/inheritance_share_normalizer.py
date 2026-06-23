from __future__ import annotations

import argparse
from fractions import Fraction

parser = argparse.ArgumentParser(description="Normalize raw inheritance-style shares so they sum to one.")
parser.add_argument("--shares", type=str, required=True, help="Comma-separated shares, such as 1/2,1/3,1/6.")
args = parser.parse_args()

shares = [Fraction(part.strip()) for part in args.shares.split(",")]
total = sum(shares, Fraction(0, 1))
if total <= 0:
    raise SystemExit("shares must sum to a positive value")
normalized = [share / total for share in shares]
print("normalized_shares=" + ",".join(str(item) for item in normalized))
print(f"sum={sum(normalized, Fraction(0, 1))}")
