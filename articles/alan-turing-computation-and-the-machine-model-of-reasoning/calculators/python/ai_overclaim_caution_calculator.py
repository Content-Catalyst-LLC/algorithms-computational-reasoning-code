from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag overclaims about computation, reasoning, and AI.")
parser.add_argument("--claim", type=str, required=True)
args = parser.parse_args()

claim = args.claim.lower()
risky_terms = [
    "all reasoning is computation",
    "ai decides everything",
    "no limits to automation",
    "turing proved machines think",
    "computable means easy",
    "halting problem is solved",
]
hits = [term for term in risky_terms if term in claim]
print(f"ai_overclaim_risk={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
