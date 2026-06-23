from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Verify whether candidate x satisfies x^2 + b x = c.")
parser.add_argument("--x", type=float, required=True)
parser.add_argument("--b", type=float, required=True)
parser.add_argument("--c", type=float, required=True)
parser.add_argument("--tolerance", type=float, default=1e-6)
args = parser.parse_args()

lhs = args.x * args.x + args.b * args.x
error = abs(lhs - args.c)
print(f"lhs={lhs:.6f}")
print(f"rhs={args.c:.6f}")
print(f"error={error:.6f}")
print(f"verified={str(error <= args.tolerance).lower()}")
