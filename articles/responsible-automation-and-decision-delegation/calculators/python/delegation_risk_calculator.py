from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute delegation risk score.")
    parser.add_argument("--stakes", type=float, required=True)
    parser.add_argument("--delegation-readiness", type=float, required=True)
    args = parser.parse_args()

    risk = args.stakes * (1.0 - args.delegation_readiness)
    print(f"delegation_risk_score={risk:.6f}")


if __name__ == "__main__":
    main()
