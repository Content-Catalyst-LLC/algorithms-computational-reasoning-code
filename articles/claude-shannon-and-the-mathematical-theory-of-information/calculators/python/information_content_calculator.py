from __future__ import annotations

import argparse
import math

parser = argparse.ArgumentParser(description="Compute self-information I(x) = -log2 p(x).")
parser.add_argument("--probability", type=float, required=True)
args = parser.parse_args()

if not (0 < args.probability <= 1):
    raise SystemExit("probability must be in (0, 1]")
info = -math.log2(args.probability)
print(f"information_bits={info:.9f}")
