from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute workload burden score.")
parser.add_argument("--pace", type=float, required=True)
parser.add_argument("--hours", type=float, required=True)
parser.add_argument("--fatigue", type=float, required=True)
parser.add_argument("--schedule-volatility", type=float, required=True)
args = parser.parse_args()

score = (args.pace + args.hours + args.fatigue + args.schedule_volatility) / 4.0
print(f"workload_burden_score={score:.6f}")
