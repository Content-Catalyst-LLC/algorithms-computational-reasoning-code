from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag overclaims about AI-generated scientific code.")
parser.add_argument("--claim", type=str, required=True)
args = parser.parse_args()

claim = args.claim.lower()
risky_terms = [
    "generated scientific code is automatically correct",
    "no numerical review needed",
    "no performance testing needed",
    "no tests needed",
    "ai code is always optimized",
    "units do not need checking",
    "no documentation needed",
]
hits = [term for term in risky_terms if term in claim]
print(f"scientific_code_generation_risk={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
