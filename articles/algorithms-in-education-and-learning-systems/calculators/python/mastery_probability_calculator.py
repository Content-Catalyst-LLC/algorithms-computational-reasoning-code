from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Toy mastery probability update from prior and evidence strength.")
parser.add_argument("--prior", type=float, required=True)
parser.add_argument("--evidence", type=float, required=True)
parser.add_argument("--weight", type=float, default=0.50)
args = parser.parse_args()

if not (0 <= args.prior <= 1 and 0 <= args.evidence <= 1 and 0 <= args.weight <= 1):
    raise SystemExit("prior, evidence, and weight must be in [0, 1]")
mastery = (1 - args.weight) * args.prior + args.weight * args.evidence
print(f"mastery_probability={mastery:.6f}")
