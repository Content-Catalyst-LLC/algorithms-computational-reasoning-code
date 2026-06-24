from __future__ import annotations
import argparse

parser = argparse.ArgumentParser(description="Update a tiny two-unit threshold network.")
parser.add_argument("--x1", type=int, required=True)
parser.add_argument("--x2", type=int, required=True)
parser.add_argument("--threshold", type=int, default=1)
args = parser.parse_args()
y1 = 1 if args.x1 + args.x2 >= args.threshold else 0
y2 = 1 if args.x1 - args.x2 >= args.threshold else 0
print(f"next_state={y1},{y2}")
