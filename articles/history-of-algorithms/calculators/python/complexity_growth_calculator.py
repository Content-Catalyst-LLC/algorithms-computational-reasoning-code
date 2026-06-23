from __future__ import annotations

import argparse
import math

parser = argparse.ArgumentParser(description="Compare basic growth rates for a given n.")
parser.add_argument("--n", type=int, required=True)
args = parser.parse_args()

if args.n <= 0:
    raise SystemExit("n must be positive")

n = args.n
values = {
    "n": float(n),
    "n_log2_n": n * math.log2(n),
    "n_squared": float(n * n),
    "two_to_n": float(2 ** min(n, 60)),
}
for key, value in values.items():
    print(f"{key}={value:.6f}")
