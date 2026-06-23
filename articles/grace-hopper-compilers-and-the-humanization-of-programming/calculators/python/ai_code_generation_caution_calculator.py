from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag overclaims that confuse AI code generation with compiler guarantees.")
parser.add_argument("--claim", type=str, required=True)
args = parser.parse_args()

claim = args.claim.lower()
risky_terms = [
    "ai generated code is automatically correct",
    "no tests needed",
    "ai is just a compiler",
    "probabilistic code generation guarantees semantics",
    "no human review needed",
    "generated code is always secure",
]
hits = [term for term in risky_terms if term in claim]
print(f"ai_code_generation_overclaim={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
