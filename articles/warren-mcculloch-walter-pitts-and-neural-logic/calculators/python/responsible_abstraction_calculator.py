from __future__ import annotations
import argparse

parser = argparse.ArgumentParser(description="Score formal clarity, stated limits, and historical care.")
parser.add_argument("--formal-clarity", type=float, required=True)
parser.add_argument("--stated-limits", type=float, required=True)
parser.add_argument("--historical-care", type=float, required=True)
args = parser.parse_args()
score = (args.formal_clarity + args.stated_limits + args.historical_care) / 3.0
print(f"responsible_abstraction_score={score:.6f}")
