from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute two-asset portfolio variance.")
parser.add_argument("--w1", type=float, required=True)
parser.add_argument("--w2", type=float, required=True)
parser.add_argument("--sigma1", type=float, required=True)
parser.add_argument("--sigma2", type=float, required=True)
parser.add_argument("--rho", type=float, required=True)
args = parser.parse_args()

variance = (
    args.w1 ** 2 * args.sigma1 ** 2 +
    args.w2 ** 2 * args.sigma2 ** 2 +
    2 * args.w1 * args.w2 * args.rho * args.sigma1 * args.sigma2
)
print(f"portfolio_variance={variance:.6f}")
