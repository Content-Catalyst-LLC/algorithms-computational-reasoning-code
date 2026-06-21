from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute intervention net benefit after costs and governance risk penalty.")
    parser.add_argument("--effect", type=float, required=True)
    parser.add_argument("--implementation-cost", type=float, required=True)
    parser.add_argument("--governance-risk", type=float, required=True)
    parser.add_argument("--cost-weight", type=float, default=0.35)
    parser.add_argument("--risk-weight", type=float, default=0.15)
    args = parser.parse_args()
    net = args.effect - args.cost_weight * args.implementation_cost - args.risk_weight * args.governance_risk
    print(f"effect={args.effect:.6f}")
    print(f"net_benefit={net:.6f}")


if __name__ == "__main__":
    main()
