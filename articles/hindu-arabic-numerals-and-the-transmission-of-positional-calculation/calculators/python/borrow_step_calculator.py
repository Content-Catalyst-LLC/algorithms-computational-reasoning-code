from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute a simple borrow transformation.")
parser.add_argument("--upper-digit", type=int, required=True)
parser.add_argument("--lower-digit", type=int, required=True)
parser.add_argument("--base", type=int, default=10)
args = parser.parse_args()

if args.base <= 1:
    raise SystemExit("base must be greater than 1")
if args.upper_digit <= 0:
    raise SystemExit("upper digit must be positive to borrow")
new_upper = args.upper_digit - 1
new_lower = args.lower_digit + args.base
print(f"new_upper_digit={new_upper}")
print(f"new_lower_digit={new_lower}")
