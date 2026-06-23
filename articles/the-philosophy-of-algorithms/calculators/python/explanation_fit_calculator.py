from __future__ import annotations
import argparse
parser = argparse.ArgumentParser(description="Estimate explanation fit across audiences.")
parser.add_argument("--affected-person-fit", type=float, required=True)
parser.add_argument("--developer-fit", type=float, required=True)
parser.add_argument("--regulator-fit", type=float, required=True)
parser.add_argument("--institution-fit", type=float, required=True)
args = parser.parse_args()
fit = (args.affected_person_fit + args.developer_fit + args.regulator_fit + args.institution_fit) / 4.0
print(f"explanation_fit={fit:.6f}")
print(f"explanation_gap={1.0 - fit:.6f}")
