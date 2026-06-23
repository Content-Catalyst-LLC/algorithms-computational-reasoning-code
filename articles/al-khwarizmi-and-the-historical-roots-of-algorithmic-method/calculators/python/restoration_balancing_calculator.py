from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Normalize simple like-term counts on left and right sides.")
parser.add_argument("--left-roots", type=float, required=True)
parser.add_argument("--right-roots", type=float, required=True)
parser.add_argument("--left-numbers", type=float, required=True)
parser.add_argument("--right-numbers", type=float, required=True)
args = parser.parse_args()

net_roots_left = args.left_roots - args.right_roots
net_numbers_right = args.right_numbers - args.left_numbers

print(f"normalized_left_roots={net_roots_left:.6f}")
print(f"normalized_right_numbers={net_numbers_right:.6f}")
print("interpretation=like terms balanced into simplified root/number relation")
