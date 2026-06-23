from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag governance risks in feedback-loop claims.")
parser.add_argument("--claim", type=str, required=True)
args = parser.parse_args()

claim = args.claim.lower()
risky_terms = [
    "feedback is always good",
    "no appeal needed",
    "model governance is enough",
    "outputs do not affect future data",
    "humans are just system components",
    "automation has no responsibility problem",
]
hits = [term for term in risky_terms if term in claim]
print(f"feedback_governance_risk={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
