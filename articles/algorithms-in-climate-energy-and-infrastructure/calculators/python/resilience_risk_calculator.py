from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute resilience risk.")
parser.add_argument("--impact-score", type=float, required=True)
parser.add_argument("--equity-readiness", type=float, required=True)
parser.add_argument("--validation-readiness", type=float, required=True)
parser.add_argument("--governance-score", type=float, required=True)
args = parser.parse_args()

risk = (
    args.impact_score +
    (1.0 - args.equity_readiness) +
    (1.0 - args.validation_readiness) +
    (1.0 - args.governance_score)
) / 4.0
print(f"resilience_risk_score={risk:.6f}")
