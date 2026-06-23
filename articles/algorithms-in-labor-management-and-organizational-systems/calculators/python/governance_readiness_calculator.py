from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute workplace algorithm governance readiness.")
parser.add_argument("--fairness-readiness", type=float, required=True)
parser.add_argument("--privacy-readiness", type=float, required=True)
parser.add_argument("--contestability", type=float, required=True)
parser.add_argument("--safety-readiness", type=float, required=True)
parser.add_argument("--human-review", type=float, required=True)
parser.add_argument("--monitoring", type=float, required=True)
parser.add_argument("--governance", type=float, required=True)
args = parser.parse_args()

score = (
    args.fairness_readiness +
    args.privacy_readiness +
    args.contestability +
    args.safety_readiness +
    args.human_review +
    args.monitoring +
    args.governance
) / 7.0
print(f"governance_readiness_score={score:.6f}")
