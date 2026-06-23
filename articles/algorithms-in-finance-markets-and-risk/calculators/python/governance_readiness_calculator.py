from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute financial algorithm governance readiness.")
parser.add_argument("--transparency", type=float, required=True)
parser.add_argument("--human-review", type=float, required=True)
parser.add_argument("--validation", type=float, required=True)
parser.add_argument("--monitoring", type=float, required=True)
parser.add_argument("--governance", type=float, required=True)
args = parser.parse_args()

score = (args.transparency + args.human_review + args.validation + args.monitoring + args.governance) / 5.0
print(f"governance_readiness_score={score:.6f}")
