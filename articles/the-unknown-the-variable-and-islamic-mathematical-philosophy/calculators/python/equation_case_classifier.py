from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Classify a simple algebraic case with square, root, and number terms.")
parser.add_argument("--square", type=float, default=0.0)
parser.add_argument("--root", type=float, default=0.0)
parser.add_argument("--number", type=float, default=0.0)
args = parser.parse_args()

has_square = abs(args.square) > 1e-12
has_root = abs(args.root) > 1e-12
has_number = abs(args.number) > 1e-12

if has_square and has_root and has_number:
    case = "squares_and_roots_equal_number"
elif has_square and has_number:
    case = "squares_equal_number"
elif has_root and has_number:
    case = "roots_equal_number"
elif has_square and has_root:
    case = "squares_equal_roots"
else:
    case = "insufficient_case_structure"
print(f"equation_case={case}")
