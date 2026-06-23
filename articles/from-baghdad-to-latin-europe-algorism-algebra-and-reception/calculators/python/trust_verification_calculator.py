from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Score method trust from checks, teaching, adoption, auditability, and practical use.")
for name in ["checks", "teaching", "adoption", "auditability", "practical_use"]:
    parser.add_argument(f"--{name.replace('_', '-')}", choices=["true", "false"], required=True)
args = parser.parse_args()

values = [
    args.checks == "true",
    args.teaching == "true",
    args.adoption == "true",
    args.auditability == "true",
    args.practical_use == "true",
]
score = sum(values) / len(values)
print(f"trust_verification_score={score:.6f}")
