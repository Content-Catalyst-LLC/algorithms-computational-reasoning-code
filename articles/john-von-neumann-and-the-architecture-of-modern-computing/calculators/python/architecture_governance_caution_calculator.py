from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag architecture governance risks.")
parser.add_argument("--claim", type=str, required=True)
args = parser.parse_args()

claim = args.claim.lower()
risky_terms = [
    "no logs needed",
    "anyone can change code",
    "programs are always safe",
    "memory does not matter",
    "architecture is irrelevant",
    "ai has no infrastructure risk",
]
hits = [term for term in risky_terms if term in claim]
print(f"architecture_governance_risk={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
