from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Estimate dependency governance risk.")
parser.add_argument("--unmaintained-packages", type=int, required=True)
parser.add_argument("--total-packages", type=int, required=True)
parser.add_argument("--unpinned-packages", type=int, required=True)
args = parser.parse_args()

if args.total_packages <= 0:
    raise SystemExit("total packages must be positive")
risk = (args.unmaintained_packages + args.unpinned_packages) / (2.0 * args.total_packages)
risk = max(0.0, min(1.0, risk))
print(f"dependency_governance_risk={risk:.6f}")
