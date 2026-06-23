from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag common overclaims about al-Khwārizmī.")
parser.add_argument("--claim", type=str, required=True)
args = parser.parse_args()

claim = args.claim.lower()
risky_terms = [
    "invented all algorithms",
    "invented algorithms",
    "first computer scientist",
    "created ai",
    "wrote code",
    "invented place value",
    "invented all algebra",
    "only preserved",
]
hits = [term for term in risky_terms if term in claim]
print(f"myth_risk={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
