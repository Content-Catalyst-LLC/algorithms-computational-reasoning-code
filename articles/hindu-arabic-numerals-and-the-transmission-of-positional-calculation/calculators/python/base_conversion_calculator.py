from __future__ import annotations

import argparse

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

parser = argparse.ArgumentParser(description="Convert a nonnegative integer to a target base.")
parser.add_argument("--number", type=int, required=True)
parser.add_argument("--base", type=int, required=True)
args = parser.parse_args()

if args.number < 0:
    raise SystemExit("number must be nonnegative")
if not (2 <= args.base <= len(DIGITS)):
    raise SystemExit("base must be between 2 and 36")
n = args.number
if n == 0:
    print("0")
else:
    out = []
    while n:
        n, rem = divmod(n, args.base)
        out.append(DIGITS[rem])
    print("".join(reversed(out)))
