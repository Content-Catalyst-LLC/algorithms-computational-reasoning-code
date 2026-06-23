from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute learning-system risk.")
parser.add_argument("--impact-score", type=float, required=True)
parser.add_argument("--equity-readiness", type=float, required=True)
parser.add_argument("--pedagogical-validity", type=float, required=True)
parser.add_argument("--governance-readiness", type=float, required=True)
args = parser.parse_args()

risk = (
    args.impact_score +
    (1.0 - args.equity_readiness) +
    (1.0 - args.pedagogical_validity) +
    (1.0 - args.governance_readiness)
) / 4.0
print(f"learning_system_risk_score={risk:.6f}")
