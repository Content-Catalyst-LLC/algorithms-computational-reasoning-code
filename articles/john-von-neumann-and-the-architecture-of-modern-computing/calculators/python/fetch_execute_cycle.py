from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Simulate a tiny fetch-execute cycle.")
parser.add_argument("--program", type=str, default="LOAD 2,ADD 3,STORE 0,HALT")
args = parser.parse_args()

instructions = [x.strip() for x in args.program.split(",") if x.strip()]
acc = 0
pc = 0
trace = []

while pc < len(instructions):
    inst = instructions[pc]
    trace.append(f"fetch pc={pc} instruction={inst}")
    op, *rest = inst.split()
    if op == "LOAD":
        acc = int(rest[0])
    elif op == "ADD":
        acc += int(rest[0])
    elif op == "STORE":
        trace.append(f"store address={rest[0]} value={acc}")
    elif op == "HALT":
        trace.append("halt")
        break
    pc += 1

print("accumulator=" + str(acc))
print("trace=" + " | ".join(trace))
