from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Build a Church numeral expression as repeated function application.")
parser.add_argument("--n", type=int, required=True)
args = parser.parse_args()

if args.n < 0:
    raise SystemExit("n must be nonnegative")

body = "x"
for _ in range(args.n):
    body = f"f ({body})"
print(f"church_numeral=λf. λx. {body}")
print(f"applies_f_times={args.n}")
