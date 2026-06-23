from __future__ import annotations

import argparse

Z_BY_CONFIDENCE = {
    "0.90": 1.281552,
    "0.95": 1.644854,
    "0.99": 2.326348,
}

parser = argparse.ArgumentParser(description="Compute normal approximation VaR for a loss distribution.")
parser.add_argument("--portfolio-value", type=float, required=True)
parser.add_argument("--volatility", type=float, required=True)
parser.add_argument("--confidence", type=str, default="0.95", choices=sorted(Z_BY_CONFIDENCE.keys()))
args = parser.parse_args()

var = args.portfolio_value * args.volatility * Z_BY_CONFIDENCE[args.confidence]
print(f"value_at_risk={var:.6f}")
