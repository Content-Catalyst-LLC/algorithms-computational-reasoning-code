from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Increment unary input by appending one 1 at the first blank.")
parser.add_argument("--tape", type=str, default="111_")
args = parser.parse_args()

tape = list(args.tape)
head = 0
while head < len(tape) and tape[head] == "1":
    head += 1
if head == len(tape):
    tape.append("_")
tape[head] = "1"
if head + 1 == len(tape):
    tape.append("_")
print("incremented_tape=" + "".join(tape))
