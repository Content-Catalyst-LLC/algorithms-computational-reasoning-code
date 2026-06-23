from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Score authorship dimensions in Lovelace history.")
for name in ["translation", "notes", "interpretation", "collaboration", "procedure"]:
    parser.add_argument(f"--has-{name}", choices=["true", "false"], required=True)
args = parser.parse_args()

values = [
    args.has_translation == "true",
    args.has_notes == "true",
    args.has_interpretation == "true",
    args.has_collaboration == "true",
    args.has_procedure == "true",
]
score = sum(values) / len(values)
print(f"authorship_credit_score={score:.6f}")
