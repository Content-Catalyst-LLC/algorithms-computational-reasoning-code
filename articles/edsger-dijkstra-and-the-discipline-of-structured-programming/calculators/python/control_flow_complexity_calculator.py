from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Estimate simplified cyclomatic complexity as decisions + 1.")
parser.add_argument("--decisions", type=int, required=True, help="Number of if/while/for/case decision points.")
args = parser.parse_args()

if args.decisions < 0:
    raise SystemExit("decisions must be nonnegative")
complexity = args.decisions + 1
print(f"simplified_cyclomatic_complexity={complexity}")
