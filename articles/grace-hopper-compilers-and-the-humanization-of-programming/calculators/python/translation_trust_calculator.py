from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Estimate translation trust from specification, tests, diagnostics, and review.")
parser.add_argument("--specification", type=float, required=True)
parser.add_argument("--tests", type=float, required=True)
parser.add_argument("--diagnostics", type=float, required=True)
parser.add_argument("--human-review", type=float, required=True)
args = parser.parse_args()

score = (args.specification + args.tests + args.diagnostics + args.human_review) / 4.0
print(f"translation_trust_score={score:.6f}")
