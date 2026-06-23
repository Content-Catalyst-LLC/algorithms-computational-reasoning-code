from __future__ import annotations
import argparse

parser = argparse.ArgumentParser(description="Estimate future algorithmic risk.")
for name in ["institutional-consequence", "uncertainty", "automation-level", "opacity", "contestability-need", "human-judgment-requirement", "failure-severity"]:
    parser.add_argument(f"--{name}", type=float, required=True)
args = parser.parse_args()
risk = (
    args.institutional_consequence + args.uncertainty + args.automation_level + args.opacity +
    args.contestability_need + args.human_judgment_requirement + args.failure_severity
) / 7.0
print(f"future_risk_score={risk:.6f}")
