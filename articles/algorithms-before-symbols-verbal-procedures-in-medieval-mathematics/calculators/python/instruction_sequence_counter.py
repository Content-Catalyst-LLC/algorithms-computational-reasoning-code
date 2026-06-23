from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Count ordered verbal instruction steps separated by semicolons.")
parser.add_argument("--procedure", type=str, required=True)
args = parser.parse_args()

steps = [part.strip() for part in args.procedure.split(";") if part.strip()]
print(f"steps={len(steps)}")
for idx, step in enumerate(steps, start=1):
    print(f"{idx}: {step}")
