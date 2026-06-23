from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag overclaims about AI-generated code and correctness.")
parser.add_argument("--claim", type=str, required=True)
args = parser.parse_args()

claim = args.claim.lower()
risky_terms = [
    "it runs so it is correct",
    "no proof needed",
    "no tests needed",
    "ai generated code is automatically safe",
    "plausible code is enough",
    "generated code needs no review",
]
hits = [term for term in risky_terms if term in claim]
print(f"generated_code_reasoning_risk={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
