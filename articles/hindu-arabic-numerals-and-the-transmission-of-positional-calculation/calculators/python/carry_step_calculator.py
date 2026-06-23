from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute digit and carry from a local sum.")
parser.add_argument("--local-sum", type=int, required=True)
parser.add_argument("--base", type=int, default=10)
args = parser.parse_args()

if args.base <= 1:
    raise SystemExit("base must be greater than 1")
digit = args.local_sum % args.base
carry = args.local_sum // args.base
print(f"digit={digit}")
print(f"carry={carry}")
