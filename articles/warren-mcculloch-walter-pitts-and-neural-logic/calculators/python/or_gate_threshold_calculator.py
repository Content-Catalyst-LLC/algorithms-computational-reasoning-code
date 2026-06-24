from __future__ import annotations
import argparse

parser = argparse.ArgumentParser(description="Demonstrate OR as threshold logic.")
parser.add_argument("--x1", type=int, required=True)
parser.add_argument("--x2", type=int, required=True)
args = parser.parse_args()
output = 1 if args.x1 + args.x2 >= 1 else 0
print(f"or_output={output}")
