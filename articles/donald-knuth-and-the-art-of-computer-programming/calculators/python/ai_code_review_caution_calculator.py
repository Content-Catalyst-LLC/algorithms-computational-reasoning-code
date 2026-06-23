from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag overclaims about generated code and algorithmic understanding.")
parser.add_argument("--claim", type=str, required=True)
args = parser.parse_args()

claim = args.claim.lower()
risky_terms = [
    "generated code is understood",
    "no analysis needed",
    "no tests needed",
    "ai code is automatically optimal",
    "no documentation needed",
    "plausible code is enough",
]
hits = [term for term in risky_terms if term in claim]
print(f"algorithmic_understanding_risk={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
