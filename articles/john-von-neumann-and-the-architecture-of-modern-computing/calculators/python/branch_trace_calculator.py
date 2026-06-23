from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Trace simple branch/loop behavior.")
parser.add_argument("--n", type=int, default=3)
args = parser.parse_args()

n = args.n
steps = []
while n > 0:
    steps.append(f"n={n}: branch loop")
    n -= 1
steps.append("n=0: exit")
print("steps=" + " | ".join(steps))
print(f"loop_iterations={args.n if args.n > 0 else 0}")
