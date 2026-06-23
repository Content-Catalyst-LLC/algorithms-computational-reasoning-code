from __future__ import annotations
import argparse
parser = argparse.ArgumentParser(description="Estimate delegation risk from severity, automation, and opacity.")
parser.add_argument("--decision-severity", type=float, required=True)
parser.add_argument("--automation-level", type=float, required=True)
parser.add_argument("--opacity", type=float, required=True)
args = parser.parse_args()
risk = max(0.0, min(1.0, args.decision_severity * args.automation_level * args.opacity))
print(f"delegation_risk={risk:.6f}")
