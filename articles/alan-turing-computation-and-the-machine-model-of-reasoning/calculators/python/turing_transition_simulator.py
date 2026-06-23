from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Run a tiny Turing-style transition system that changes 1s to 1s until blank.")
parser.add_argument("--tape", type=str, default="111_")
parser.add_argument("--max-steps", type=int, default=20)
args = parser.parse_args()

tape = list(args.tape)
head = 0
state = "scan"
blank = "_"
steps = 0

while steps < args.max_steps and state != "halt":
    if head >= len(tape):
        tape.append(blank)
    symbol = tape[head]
    if state == "scan" and symbol == "1":
        tape[head] = "1"
        head += 1
    elif state == "scan" and symbol == blank:
        tape[head] = blank
        state = "halt"
    else:
        state = "halt"
    steps += 1

print(f"state={state}")
print(f"steps={steps}")
print(f"head={head}")
print("tape=" + "".join(tape))
