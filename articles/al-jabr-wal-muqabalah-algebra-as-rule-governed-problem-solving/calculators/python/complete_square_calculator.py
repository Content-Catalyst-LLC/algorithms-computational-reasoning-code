from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute completing-square term for x^2 + b*x.")
parser.add_argument("--b", type=float, required=True)
args = parser.parse_args()

term = (args.b / 2.0) ** 2
print(f"completing_term={term:.6f}")
print(f"square_form=(x + {args.b / 2.0:.6f})^2")
