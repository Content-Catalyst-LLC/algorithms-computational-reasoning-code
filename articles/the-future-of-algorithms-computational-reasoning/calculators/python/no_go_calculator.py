from __future__ import annotations
import argparse

parser = argparse.ArgumentParser(description="Evaluate no-go/refusal criteria.")
for name in ["poor-fit", "invalid-data", "high-opacity", "no-appeal", "no-governance"]:
    parser.add_argument(f"--{name}", action="store_true")
args = parser.parse_args()
no_go = args.poor_fit or args.invalid_data or args.high_opacity or args.no_appeal or args.no_governance
print(f"no_go={str(no_go).lower()}")
