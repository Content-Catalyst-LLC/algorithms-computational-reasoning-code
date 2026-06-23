from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute financial algorithm risk.")
parser.add_argument("--model-risk", type=float, required=True)
parser.add_argument("--impact-score", type=float, required=True)
parser.add_argument("--governance-readiness", type=float, required=True)
args = parser.parse_args()

score = (args.model_risk + args.impact_score + (1.0 - args.governance_readiness)) / 3.0
print(f"financial_algorithm_risk_score={score:.6f}")
