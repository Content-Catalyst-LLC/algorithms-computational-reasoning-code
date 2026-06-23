from __future__ import annotations
import argparse
parser = argparse.ArgumentParser(description="Average philosophical review dimensions.")
for name in ["formalization-intensity","abstraction-risk","representation-risk","delegation-level","opacity","optimization-pressure","contestability-need","institutional-consequence","human-judgment-requirement","governance-urgency"]:
    parser.add_argument(f"--{name}", type=float, required=True)
args = parser.parse_args()
score = (args.formalization_intensity + args.abstraction_risk + args.representation_risk + args.delegation_level + args.opacity + args.optimization_pressure + args.contestability_need + args.institutional_consequence + args.human_judgment_requirement + args.governance_urgency) / 10.0
print(f"philosophical_review_score={score:.6f}")
