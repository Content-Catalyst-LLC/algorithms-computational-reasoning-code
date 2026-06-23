from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute infrastructure risk = hazard * exposure * vulnerability.")
parser.add_argument("--hazard", type=float, required=True)
parser.add_argument("--exposure", type=float, required=True)
parser.add_argument("--vulnerability", type=float, required=True)
args = parser.parse_args()

risk = args.hazard * args.exposure * args.vulnerability
print(f"infrastructure_risk={risk:.6f}")
