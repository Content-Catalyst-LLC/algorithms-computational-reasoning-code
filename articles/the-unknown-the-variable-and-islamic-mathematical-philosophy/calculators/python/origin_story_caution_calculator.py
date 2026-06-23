from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag anachronistic or oversimplified origin-story phrases.")
parser.add_argument("--phrase", type=str, required=True)
args = parser.parse_args()

phrase = args.phrase.lower()
risk_terms = [
    "invented variables",
    "first modern variable",
    "just primitive",
    "no symbols so no abstraction",
    "single origin",
    "same as modern x",
]
hits = [term for term in risk_terms if term in phrase]
print(f"origin_story_risk={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
