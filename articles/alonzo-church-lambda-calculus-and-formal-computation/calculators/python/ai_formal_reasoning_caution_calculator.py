from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag overclaims about AI and formal reasoning.")
parser.add_argument("--claim", type=str, required=True)
args = parser.parse_args()

claim = args.claim.lower()
risky_terms = [
    "ai proves everything",
    "formal systems decide all truth",
    "lambda calculus solves all reasoning",
    "no need for human judgment",
    "all outputs are formal proofs",
    "automation has no limits",
]
hits = [term for term in risky_terms if term in claim]
print(f"formal_reasoning_overclaim={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
