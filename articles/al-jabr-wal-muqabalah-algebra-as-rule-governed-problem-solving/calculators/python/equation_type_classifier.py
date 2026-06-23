from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Classify a toy equation by highest polynomial degree.")
parser.add_argument("--degree", type=int, required=True)
args = parser.parse_args()

if args.degree < 0:
    raise SystemExit("degree must be nonnegative")
if args.degree == 0:
    label = "constant_or_degenerate"
elif args.degree == 1:
    label = "linear_problem_type"
elif args.degree == 2:
    label = "quadratic_problem_type"
else:
    label = "higher_order_problem_type"
print(f"equation_type={label}")
