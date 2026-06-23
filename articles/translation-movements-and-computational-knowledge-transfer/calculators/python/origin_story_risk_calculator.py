from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag oversimplified origin-story phrases.")
parser.add_argument("--phrase", type=str, required=True)
args = parser.parse_args()

phrase = args.phrase.lower()
risk_terms = [
    "only preserved",
    "single origin",
    "everything happened",
    "invented all",
    "just translated",
    "one source",
]
hits = [term for term in risk_terms if term in phrase]
print(f"origin_story_risk={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
