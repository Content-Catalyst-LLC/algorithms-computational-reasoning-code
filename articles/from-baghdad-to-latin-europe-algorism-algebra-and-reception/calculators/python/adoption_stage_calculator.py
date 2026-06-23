from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Classify adoption stage from use, teaching, institution, and trust scores.")
parser.add_argument("--use", type=float, required=True)
parser.add_argument("--teaching", type=float, required=True)
parser.add_argument("--institution", type=float, required=True)
parser.add_argument("--trust", type=float, required=True)
args = parser.parse_args()

score = (args.use + args.teaching + args.institution + args.trust) / 4.0
if score >= 0.85:
    stage = "normalized"
elif score >= 0.65:
    stage = "adopted"
elif score >= 0.40:
    stage = "contested_or_mixed"
else:
    stage = "novel_or_marginal"
print(f"adoption_score={score:.6f}")
print(f"adoption_stage={stage}")
