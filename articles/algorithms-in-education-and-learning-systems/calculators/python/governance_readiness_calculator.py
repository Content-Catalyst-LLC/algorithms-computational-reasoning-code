from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute learning-system governance readiness.")
parser.add_argument("--equity-readiness", type=float, required=True)
parser.add_argument("--privacy-readiness", type=float, required=True)
parser.add_argument("--pedagogical-validity", type=float, required=True)
parser.add_argument("--human-review", type=float, required=True)
parser.add_argument("--accessibility-readiness", type=float, required=True)
parser.add_argument("--monitoring", type=float, required=True)
parser.add_argument("--governance", type=float, required=True)
args = parser.parse_args()

score = (
    args.equity_readiness +
    args.privacy_readiness +
    args.pedagogical_validity +
    args.human_review +
    args.accessibility_readiness +
    args.monitoring +
    args.governance
) / 7.0
print(f"governance_readiness_score={score:.6f}")
