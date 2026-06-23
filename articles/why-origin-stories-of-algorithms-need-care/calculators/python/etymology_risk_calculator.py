from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag etymology-as-invention risk.")
parser.add_argument("--claim", type=str, required=True)
args = parser.parse_args()

claim = args.claim.lower()
risky_terms = ["invented algorithms", "origin of all algorithms", "algorithm means he invented", "because the word comes from"]
hits = [term for term in risky_terms if term in claim]
print(f"etymology_risk={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
