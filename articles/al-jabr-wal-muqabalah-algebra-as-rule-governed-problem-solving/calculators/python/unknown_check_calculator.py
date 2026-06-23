from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Check whether candidate x satisfies a*x + b = c.")
parser.add_argument("--a", type=float, required=True)
parser.add_argument("--b", type=float, required=True)
parser.add_argument("--c", type=float, required=True)
parser.add_argument("--x", type=float, required=True)
parser.add_argument("--tolerance", type=float, default=1e-9)
args = parser.parse_args()

lhs = args.a * args.x + args.b
residual = lhs - args.c
satisfies = abs(residual) <= args.tolerance
print(f"lhs={lhs:.6f}")
print(f"rhs={args.c:.6f}")
print(f"residual={residual:.6f}")
print(f"satisfies={str(satisfies).lower()}")
