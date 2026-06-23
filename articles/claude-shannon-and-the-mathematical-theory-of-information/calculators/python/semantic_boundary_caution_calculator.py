from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag overclaims that confuse Shannon information with meaning/truth.")
parser.add_argument("--claim", type=str, required=True)
args = parser.parse_args()

claim = args.claim.lower()
risky_terms = [
    "entropy proves meaning",
    "high information means wisdom",
    "bits determine truth",
    "information theory solves ethics",
    "compression proves understanding",
    "ai meaning is just entropy",
]
hits = [term for term in risky_terms if term in claim]
print(f"semantic_boundary_risk={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
