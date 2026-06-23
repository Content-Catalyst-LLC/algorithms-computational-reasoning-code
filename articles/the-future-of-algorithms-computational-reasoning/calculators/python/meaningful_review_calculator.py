from __future__ import annotations
import argparse

parser = argparse.ArgumentParser(description="Estimate whether human review is meaningful.")
for name in ["authority", "time", "evidence", "training", "override-power"]:
    parser.add_argument(f"--{name}", type=float, required=True)
args = parser.parse_args()
score = (args.authority + args.time + args.evidence + args.training + args.override_power) / 5.0
print(f"meaningful_review_score={score:.6f}")
print(f"symbolic_review_risk={1.0 - score:.6f}")
