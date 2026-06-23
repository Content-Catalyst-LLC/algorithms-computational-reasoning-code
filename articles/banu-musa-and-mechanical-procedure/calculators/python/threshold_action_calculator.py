from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Toy threshold action calculator for conceptual mechanical procedure.")
parser.add_argument("--level", type=float, required=True)
parser.add_argument("--threshold", type=float, required=True)
args = parser.parse_args()

action = args.level >= args.threshold
print(f"action_triggered={str(action).lower()}")
