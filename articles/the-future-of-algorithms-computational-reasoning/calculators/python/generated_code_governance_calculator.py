from __future__ import annotations
import argparse

parser = argparse.ArgumentParser(description="Flag AI-generated code governance gaps.")
parser.add_argument("--claim", type=str, required=True)
args = parser.parse_args()
claim = args.claim.lower()
risky_terms = [
    "no tests needed",
    "no review needed",
    "no dependency audit",
    "no owner",
    "ship generated code directly",
    "no documentation needed",
    "no security review",
]
hits = [term for term in risky_terms if term in claim]
print(f"generated_code_governance_risk={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
