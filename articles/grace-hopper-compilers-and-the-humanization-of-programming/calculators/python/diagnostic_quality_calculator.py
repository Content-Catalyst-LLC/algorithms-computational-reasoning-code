from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Estimate diagnostic helpfulness from clarity, location, explanation, and fix hint.")
parser.add_argument("--clarity", type=float, required=True)
parser.add_argument("--location", type=float, required=True)
parser.add_argument("--explanation", type=float, required=True)
parser.add_argument("--fix-hint", type=float, required=True)
args = parser.parse_args()

score = (args.clarity + args.location + args.explanation + args.fix_hint) / 4.0
print(f"diagnostic_quality_score={score:.6f}")
