from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute public algorithmic governance readiness.")
parser.add_argument("--data-quality", type=float, required=True)
parser.add_argument("--vendor-accountability", type=float, required=True)
parser.add_argument("--monitoring", type=float, required=True)
parser.add_argument("--procedural-readiness", type=float, required=True)
args = parser.parse_args()

score = (args.data_quality + args.vendor_accountability + args.monitoring + args.procedural_readiness) / 4.0
print(f"governance_readiness_score={score:.6f}")
