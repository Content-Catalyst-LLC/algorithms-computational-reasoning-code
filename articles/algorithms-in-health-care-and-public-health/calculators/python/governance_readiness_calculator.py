from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute health algorithm governance readiness.")
parser.add_argument("--clinical-validation", type=float, required=True)
parser.add_argument("--equity-readiness", type=float, required=True)
parser.add_argument("--privacy-readiness", type=float, required=True)
parser.add_argument("--human-review", type=float, required=True)
parser.add_argument("--workflow-integration", type=float, required=True)
parser.add_argument("--monitoring", type=float, required=True)
parser.add_argument("--governance", type=float, required=True)
args = parser.parse_args()

score = (
    args.clinical_validation +
    args.equity_readiness +
    args.privacy_readiness +
    args.human_review +
    args.workflow_integration +
    args.monitoring +
    args.governance
) / 7.0
print(f"governance_readiness_score={score:.6f}")
