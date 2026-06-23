from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Classify a simple quadratic-like algebraic case ax^2 + bx = c.")
parser.add_argument("--a", type=float, default=0.0)
parser.add_argument("--b", type=float, default=0.0)
parser.add_argument("--c", type=float, default=0.0)
args = parser.parse_args()

has_square = abs(args.a) > 1e-12
has_root = abs(args.b) > 1e-12
has_number = abs(args.c) > 1e-12

if has_square and has_root and has_number:
    case = "squares_and_roots_equal_number"
elif has_square and has_number:
    case = "squares_equal_number"
elif has_root and has_number:
    case = "roots_equal_number"
elif has_square and has_root:
    case = "squares_and_roots"
else:
    case = "insufficient_case_structure"
print(f"algebra_case={case}")
