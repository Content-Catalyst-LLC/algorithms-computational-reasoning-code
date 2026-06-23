from __future__ import annotations

import argparse
from fractions import Fraction

parser = argparse.ArgumentParser(description="Compute Bernoulli number B_n using a simple Akiyama-Tanigawa method.")
parser.add_argument("--n", type=int, required=True)
args = parser.parse_args()

if args.n < 0:
    raise SystemExit("n must be nonnegative")

a = [Fraction(0) for _ in range(args.n + 1)]
for m in range(args.n + 1):
    a[m] = Fraction(1, m + 1)
    for j in range(m, 0, -1):
        a[j - 1] = j * (a[j - 1] - a[j])

result = a[0]
print(f"B_{args.n}={result.numerator}/{result.denominator}")
print(f"B_{args.n}_decimal={float(result):.12f}")
