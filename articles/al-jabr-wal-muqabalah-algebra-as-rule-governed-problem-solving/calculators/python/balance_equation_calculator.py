from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Apply the same addition to both sides of an equation.")
parser.add_argument("--left", type=float, required=True)
parser.add_argument("--right", type=float, required=True)
parser.add_argument("--add", type=float, required=True)
args = parser.parse_args()

before = args.left - args.right
left_after = args.left + args.add
right_after = args.right + args.add
after = left_after - right_after
print(f"left_after={left_after:.6f}")
print(f"right_after={right_after:.6f}")
print(f"difference_before={before:.6f}")
print(f"difference_after={after:.6f}")
