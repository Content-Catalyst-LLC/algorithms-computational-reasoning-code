from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute attention-system governance readiness.")
parser.add_argument("--transparency", type=float, required=True)
parser.add_argument("--contestability", type=float, required=True)
parser.add_argument("--moderation-readiness", type=float, required=True)
parser.add_argument("--user-control", type=float, required=True)
parser.add_argument("--governance", type=float, required=True)
parser.add_argument("--monitoring", type=float, required=True)
args = parser.parse_args()

score = (
    args.transparency +
    args.contestability +
    args.moderation_readiness +
    args.user_control +
    args.governance +
    args.monitoring
) / 6.0
print(f"governance_readiness_score={score:.6f}")
