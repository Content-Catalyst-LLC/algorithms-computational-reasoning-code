from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Evaluate y = ax^2 + bx + c as a formula-translation teaching example.")
parser.add_argument("--x", type=float, required=True)
parser.add_argument("--a", type=float, default=2.0)
parser.add_argument("--b", type=float, default=-3.0)
parser.add_argument("--c", type=float, default=1.0)
args = parser.parse_args()

y = args.a * args.x * args.x + args.b * args.x + args.c
print(f"formula=y = {args.a}x^2 + {args.b}x + {args.c}")
print(f"x={args.x:.6f}")
print(f"y={y:.6f}")
