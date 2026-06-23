from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute public algorithmic risk.")
parser.add_argument("--rights-impact", type=float, required=True)
parser.add_argument("--governance-readiness", type=float, required=True)
args = parser.parse_args()

score = args.rights_impact * (1.0 - args.governance_readiness)
print(f"public_algorithmic_risk_score={score:.6f}")
