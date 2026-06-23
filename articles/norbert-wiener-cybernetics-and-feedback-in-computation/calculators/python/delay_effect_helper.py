from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compare delayed observation with current state.")
parser.add_argument("--delayed-observed", type=float, required=True)
parser.add_argument("--current-state", type=float, required=True)
parser.add_argument("--target", type=float, required=True)
args = parser.parse_args()

delayed_error = args.target - args.delayed_observed
current_error = args.target - args.current_state
print(f"delayed_error={delayed_error:.6f}")
print(f"current_error={current_error:.6f}")
print(f"error_mismatch={abs(delayed_error - current_error):.6f}")
