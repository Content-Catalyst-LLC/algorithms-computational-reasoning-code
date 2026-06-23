from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Evaluate a simple synthetic eligibility rule.")
parser.add_argument("--income", type=float, required=True)
parser.add_argument("--income-threshold", type=float, required=True)
parser.add_argument("--documents-complete", type=str, required=True)
parser.add_argument("--residency-confirmed", type=str, required=True)
args = parser.parse_args()

docs = args.documents_complete.strip().lower() in {"1", "true", "yes", "y"}
residency = args.residency_confirmed.strip().lower() in {"1", "true", "yes", "y"}
eligible = args.income <= args.income_threshold and docs and residency
print(f"synthetic_eligible={str(eligible).lower()}")
