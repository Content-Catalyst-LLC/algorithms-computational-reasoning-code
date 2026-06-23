from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Classify standards/conformance coverage.")
parser.add_argument("--has-spec", action="store_true")
parser.add_argument("--has-tests", action="store_true")
parser.add_argument("--has-validation", action="store_true")
parser.add_argument("--has-documentation", action="store_true")
args = parser.parse_args()

score = sum([args.has_spec, args.has_tests, args.has_validation, args.has_documentation]) / 4.0
if score >= 0.75:
    status = "strong_conformance_scaffold"
elif score >= 0.5:
    status = "partial_conformance_scaffold"
else:
    status = "weak_conformance_scaffold"

print(f"conformance_score={score:.6f}")
print(f"status={status}")
