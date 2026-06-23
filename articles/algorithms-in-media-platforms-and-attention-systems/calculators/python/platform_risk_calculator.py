from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute platform risk.")
parser.add_argument("--attention-risk", type=float, required=True)
parser.add_argument("--governance-readiness", type=float, required=True)
args = parser.parse_args()

score = args.attention_risk * (1.0 - args.governance_readiness)
print(f"platform_risk_score={score:.6f}")
