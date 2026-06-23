from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Show carrying for adding two single place values.")
parser.add_argument("--a", type=int, required=True)
parser.add_argument("--b", type=int, required=True)
parser.add_argument("--base", type=int, default=10)
args = parser.parse_args()

total = args.a + args.b
carry = total // args.base
digit = total % args.base
print(f"total={total}")
print(f"result_digit={digit}")
print(f"carry={carry}")
