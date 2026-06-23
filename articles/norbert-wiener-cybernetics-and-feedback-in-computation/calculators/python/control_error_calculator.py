from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute control error and proportional corrective action.")
parser.add_argument("--target", type=float, required=True)
parser.add_argument("--observed", type=float, required=True)
parser.add_argument("--gain", type=float, default=1.0)
args = parser.parse_args()

error = args.target - args.observed
action = args.gain * error
print(f"error={error:.6f}")
print(f"corrective_action={action:.6f}")
