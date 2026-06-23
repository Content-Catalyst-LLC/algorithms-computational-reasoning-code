from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Demonstrate carry from ones to tens for two one-digit numbers.")
parser.add_argument("--a", type=int, required=True)
parser.add_argument("--b", type=int, required=True)
args = parser.parse_args()

total = args.a + args.b
carry = total // 10
ones = total % 10
print(f"sum={total}")
print(f"carry={carry}")
print(f"ones={ones}")
