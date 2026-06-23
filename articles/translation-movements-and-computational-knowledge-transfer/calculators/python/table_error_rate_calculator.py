from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Calculate simple table mismatch rate.")
parser.add_argument("--mismatches", type=float, required=True)
parser.add_argument("--checked-values", type=float, required=True)
args = parser.parse_args()

if args.checked_values <= 0:
    raise SystemExit("checked-values must be positive")
error_rate = args.mismatches / args.checked_values
print(f"table_error_rate={error_rate:.6f}")
print(f"table_accuracy={1.0 - error_rate:.6f}")
