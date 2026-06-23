from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Estimate portability as supported targets divided by desired targets.")
parser.add_argument("--supported-targets", type=float, required=True)
parser.add_argument("--desired-targets", type=float, required=True)
args = parser.parse_args()

if args.desired_targets <= 0:
    raise SystemExit("desired targets must be positive")
score = max(0.0, min(1.0, args.supported_targets / args.desired_targets))
print(f"portability_score={score:.6f}")
