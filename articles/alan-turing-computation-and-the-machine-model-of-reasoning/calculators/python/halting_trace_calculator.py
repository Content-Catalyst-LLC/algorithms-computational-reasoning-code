from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Bounded trace for a toy program: countdown halts; loop does not halt within bound.")
parser.add_argument("--program", choices=["countdown", "loop"], required=True)
parser.add_argument("--n", type=int, default=5)
parser.add_argument("--max-steps", type=int, default=20)
args = parser.parse_args()

steps = 0
value = args.n
halted = False

while steps < args.max_steps:
    if args.program == "countdown":
        if value <= 0:
            halted = True
            break
        value -= 1
    elif args.program == "loop":
        value += 1
    steps += 1

print(f"halted_within_bound={str(halted).lower()}")
print(f"steps={steps}")
print(f"final_value={value}")
print("note=bounded traces illustrate behavior but do not solve the general halting problem")
