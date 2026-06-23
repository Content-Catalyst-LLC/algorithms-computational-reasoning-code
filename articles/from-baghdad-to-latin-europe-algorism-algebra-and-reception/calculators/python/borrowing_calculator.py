from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Demonstrate borrowing in two-digit subtraction.")
parser.add_argument("--minuend", type=int, required=True)
parser.add_argument("--subtrahend", type=int, required=True)
args = parser.parse_args()

if args.minuend < 0 or args.minuend > 99 or args.subtrahend < 0 or args.subtrahend > 99:
    raise SystemExit("use two-digit nonnegative values")
borrow_needed = (args.minuend % 10) < (args.subtrahend % 10)
print(f"difference={args.minuend - args.subtrahend}")
print(f"borrow_needed={str(borrow_needed).lower()}")
