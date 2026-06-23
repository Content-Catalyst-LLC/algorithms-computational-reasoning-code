from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Classify health action from risk threshold.")
parser.add_argument("--risk-score", type=float, required=True)
parser.add_argument("--threshold", type=float, default=0.70)
args = parser.parse_args()

action = "escalate_for_review" if args.risk_score >= args.threshold else "routine_monitoring"
print(f"health_action={action}")
