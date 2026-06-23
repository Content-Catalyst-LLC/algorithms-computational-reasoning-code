from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag overclaims about reward and value in adaptive systems.")
parser.add_argument("--claim", type=str, required=True)
args = parser.parse_args()

claim = args.claim.lower()
risky_terms = [
    "reward is value",
    "maximize reward means ethical",
    "feedback guarantees good behavior",
    "no human oversight needed",
    "control equals wisdom",
]
hits = [term for term in risky_terms if term in claim]
print(f"reward_value_overclaim={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
