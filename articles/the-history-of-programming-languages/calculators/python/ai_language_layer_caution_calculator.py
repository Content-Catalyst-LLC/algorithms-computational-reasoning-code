from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag AI-code claims that ignore language ecosystems.")
parser.add_argument("--claim", type=str, required=True)
args = parser.parse_args()

claim = args.claim.lower()
risky_terms = [
    "ai replaces programming languages",
    "no language knowledge needed",
    "generated code needs no tests",
    "dependencies do not matter",
    "runtime does not matter",
    "syntax is all that matters",
    "no review needed",
]
hits = [term for term in risky_terms if term in claim]
print(f"language_history_caution={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
