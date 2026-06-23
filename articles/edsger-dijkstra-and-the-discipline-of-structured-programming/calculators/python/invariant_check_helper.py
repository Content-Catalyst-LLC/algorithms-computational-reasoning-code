from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Check whether all trace values satisfy lower <= x <= upper.")
parser.add_argument("--trace", type=str, required=True, help="Comma-separated numeric trace.")
parser.add_argument("--lower", type=float, required=True)
parser.add_argument("--upper", type=float, required=True)
args = parser.parse_args()

values = [float(x.strip()) for x in args.trace.split(",") if x.strip()]
violations = [x for x in values if not (args.lower <= x <= args.upper)]
print(f"invariant_holds={str(len(violations) == 0).lower()}")
print("violations=" + ",".join(str(v) for v in violations))
