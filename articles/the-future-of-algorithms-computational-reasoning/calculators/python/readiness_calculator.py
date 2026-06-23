from __future__ import annotations
import argparse

parser = argparse.ArgumentParser(description="Estimate deployment readiness.")
parser.add_argument("--technical-capability", type=float, required=True)
parser.add_argument("--governance-maturity", type=float, required=True)
parser.add_argument("--deployment-readiness", type=float, required=True)
args = parser.parse_args()
readiness = (args.technical_capability + args.governance_maturity + args.deployment_readiness) / 3.0
print(f"readiness_score={readiness:.6f}")
