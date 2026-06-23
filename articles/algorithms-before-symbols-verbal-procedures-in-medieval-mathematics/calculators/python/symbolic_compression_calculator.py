from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Estimate compression from verbal instruction to symbolic shorthand.")
parser.add_argument("--verbal", type=str, required=True)
parser.add_argument("--symbolic", type=str, required=True)
args = parser.parse_args()

verbal_len = len(args.verbal.replace(" ", ""))
symbolic_len = len(args.symbolic.replace(" ", ""))
if symbolic_len == 0:
    raise SystemExit("symbolic expression cannot be empty")
ratio = verbal_len / symbolic_len
print(f"verbal_chars_no_spaces={verbal_len}")
print(f"symbolic_chars_no_spaces={symbolic_len}")
print(f"compression_ratio={ratio:.6f}")
