from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Apply the same addition to both sides of an equation.")
parser.add_argument("--left", type=float, required=True)
parser.add_argument("--right", type=float, required=True)
parser.add_argument("--add", type=float, required=True)
args = parser.parse_args()

new_left = args.left + args.add
new_right = args.right + args.add
print(f"left_after={new_left:.6f}")
print(f"right_after={new_right:.6f}")
print(f"difference_preserved={(new_left - new_right):.6f}")
