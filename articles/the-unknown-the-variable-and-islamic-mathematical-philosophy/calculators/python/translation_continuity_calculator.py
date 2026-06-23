from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Score continuity across Arabic, Latin, vernacular, and symbolic forms.")
for name in ["arabic", "latin", "vernacular", "symbolic"]:
    parser.add_argument(f"--has-{name}", choices=["true", "false"], required=True)
args = parser.parse_args()

values = [
    args.has_arabic == "true",
    args.has_latin == "true",
    args.has_vernacular == "true",
    args.has_symbolic == "true",
]
score = sum(values) / len(values)
print(f"translation_continuity={score:.6f}")
