from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute sum of absolute differences between observed and expected frequencies.")
parser.add_argument("--observed", type=str, required=True, help="Comma-separated observed frequencies.")
parser.add_argument("--expected", type=str, required=True, help="Comma-separated expected frequencies.")
args = parser.parse_args()

observed = [float(part.strip()) for part in args.observed.split(",")]
expected = [float(part.strip()) for part in args.expected.split(",")]
if len(observed) != len(expected):
    raise SystemExit("observed and expected must have the same length")
distance = sum(abs(o - e) for o, e in zip(observed, expected))
print(f"frequency_distance={distance:.6f}")
