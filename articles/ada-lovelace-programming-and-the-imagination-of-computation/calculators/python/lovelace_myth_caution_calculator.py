from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag slogan, dismissal, and projection risks in Lovelace claims.")
parser.add_argument("--claim", type=str, required=True)
args = parser.parse_args()

claim = args.claim.lower()
risky_terms = [
    "only a translator",
    "single-handedly invented computing",
    "wrote modern code",
    "first programmer full stop",
    "babbage alone did everything",
    "proved ai impossible",
]
hits = [term for term in risky_terms if term in claim]
print(f"lovelace_claim_risk={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
