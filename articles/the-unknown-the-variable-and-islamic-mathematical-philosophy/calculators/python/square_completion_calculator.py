from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute completion term for x^2 + b x = c.")
parser.add_argument("--b", type=float, required=True)
parser.add_argument("--c", type=float, required=True)
args = parser.parse_args()

completion = (args.b / 2.0) ** 2
new_rhs = args.c + completion
print(f"completion_term={completion:.6f}")
print(f"completed_rhs={new_rhs:.6f}")
