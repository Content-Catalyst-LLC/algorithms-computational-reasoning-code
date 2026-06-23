from __future__ import annotations
import argparse
parser = argparse.ArgumentParser(description="Estimate contestability need.")
parser.add_argument("--decision-severity", type=float, required=True)
parser.add_argument("--error-impact", type=float, required=True)
parser.add_argument("--opacity", type=float, required=True)
parser.add_argument("--affected-person-access", type=float, required=True)
args = parser.parse_args()
need = (args.decision_severity + args.error_impact + args.opacity + (1.0 - args.affected_person_access)) / 4.0
print(f"contestability_need={need:.6f}")
