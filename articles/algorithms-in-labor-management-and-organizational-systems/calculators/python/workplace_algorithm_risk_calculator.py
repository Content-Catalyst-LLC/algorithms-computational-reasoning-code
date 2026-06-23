from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute workplace algorithm risk.")
parser.add_argument("--impact-score", type=float, required=True)
parser.add_argument("--fairness-readiness", type=float, required=True)
parser.add_argument("--privacy-readiness", type=float, required=True)
parser.add_argument("--contestability", type=float, required=True)
parser.add_argument("--governance-readiness", type=float, required=True)
args = parser.parse_args()

risk = (
    args.impact_score +
    (1.0 - args.fairness_readiness) +
    (1.0 - args.privacy_readiness) +
    (1.0 - args.contestability) +
    (1.0 - args.governance_readiness)
) / 5.0
print(f"workplace_algorithm_risk_score={risk:.6f}")
