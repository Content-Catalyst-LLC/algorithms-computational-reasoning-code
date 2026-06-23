from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Check whether a numeric variant strictly decreases.")
parser.add_argument("--variant-values", type=str, required=True)
args = parser.parse_args()

values = [float(x.strip()) for x in args.variant_values.split(",") if x.strip()]
decreases = all(values[i + 1] < values[i] for i in range(len(values) - 1))
nonnegative = all(v >= 0 for v in values)
print(f"strictly_decreasing={str(decreases).lower()}")
print(f"nonnegative={str(nonnegative).lower()}")
print(f"termination_argument_plausible={str(decreases and nonnegative).lower()}")
