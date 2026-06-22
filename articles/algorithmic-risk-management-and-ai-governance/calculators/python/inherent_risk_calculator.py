from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute inherent risk score.")
    parser.add_argument("--severity", type=float, required=True)
    parser.add_argument("--likelihood", type=float, required=True)
    parser.add_argument("--detectability", type=float, required=True)
    args = parser.parse_args()

    score = args.severity * args.likelihood * (1.0 - args.detectability)
    print(f"inherent_risk_score={score:.6f}")


if __name__ == "__main__":
    main()
