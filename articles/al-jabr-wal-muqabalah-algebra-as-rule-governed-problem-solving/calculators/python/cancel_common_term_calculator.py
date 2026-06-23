from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Cancel the same common term from both sides.")
parser.add_argument("--left", type=float, required=True)
parser.add_argument("--right", type=float, required=True)
parser.add_argument("--common", type=float, required=True)
args = parser.parse_args()

left_after = args.left - args.common
right_after = args.right - args.common
print(f"left_after={left_after:.6f}")
print(f"right_after={right_after:.6f}")
print(f"difference_preserved={(left_after - right_after):.6f}")
