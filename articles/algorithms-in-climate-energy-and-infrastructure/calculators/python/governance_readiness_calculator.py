from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute infrastructure governance readiness.")
parser.add_argument("--equity-readiness", type=float, required=True)
parser.add_argument("--validation-readiness", type=float, required=True)
parser.add_argument("--monitoring-readiness", type=float, required=True)
parser.add_argument("--governance-readiness", type=float, required=True)
parser.add_argument("--maintenance-readiness", type=float, required=True)
args = parser.parse_args()

score = (
    args.equity_readiness +
    args.validation_readiness +
    args.monitoring_readiness +
    args.governance_readiness +
    args.maintenance_readiness
) / 5.0
print(f"governance_score={score:.6f}")
