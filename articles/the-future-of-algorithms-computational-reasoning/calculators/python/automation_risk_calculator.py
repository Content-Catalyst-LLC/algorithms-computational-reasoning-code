from __future__ import annotations
import argparse

parser = argparse.ArgumentParser(description="Estimate automation risk from stakes, opacity, delegation, and irreversibility.")
parser.add_argument("--stakes", type=float, required=True)
parser.add_argument("--opacity", type=float, required=True)
parser.add_argument("--delegation", type=float, required=True)
parser.add_argument("--irreversibility", type=float, required=True)
args = parser.parse_args()
risk = args.stakes * args.opacity * args.delegation * args.irreversibility
print(f"automation_risk={max(0.0, min(1.0, risk)):.6f}")
