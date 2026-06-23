from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute health algorithm risk.")
parser.add_argument("--impact-score", type=float, required=True)
parser.add_argument("--clinical-validation", type=float, required=True)
parser.add_argument("--equity-readiness", type=float, required=True)
parser.add_argument("--governance-readiness", type=float, required=True)
args = parser.parse_args()

score = (
    args.impact_score +
    (1.0 - args.clinical_validation) +
    (1.0 - args.equity_readiness) +
    (1.0 - args.governance_readiness)
) / 4.0
print(f"health_algorithm_risk_score={score:.6f}")
