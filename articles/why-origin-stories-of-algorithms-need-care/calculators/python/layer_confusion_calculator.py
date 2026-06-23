from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag confusion among word, concept, practice, institution, and modern formalization layers.")
parser.add_argument("--claim", type=str, required=True)
args = parser.parse_args()

claim = args.claim.lower()
risky_patterns = [
    "word proves",
    "name proves",
    "therefore invented",
    "same as modern",
    "began with the word",
    "all algorithms began",
]
hits = [pattern for pattern in risky_patterns if pattern in claim]
print(f"layer_confusion_risk={str(bool(hits)).lower()}")
print("matched_patterns=" + ",".join(hits))
