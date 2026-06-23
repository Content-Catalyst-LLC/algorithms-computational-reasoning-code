from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Estimate high-level translation trust from readability, translation, performance, tests, and documentation.")
parser.add_argument("--readability", type=float, required=True)
parser.add_argument("--correct-translation", type=float, required=True)
parser.add_argument("--performance", type=float, required=True)
parser.add_argument("--tests", type=float, required=True)
parser.add_argument("--documentation", type=float, required=True)
args = parser.parse_args()

score = (args.readability + args.correct_translation + args.performance + args.tests + args.documentation) / 5.0
print(f"translation_trust_score={score:.6f}")
