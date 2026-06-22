from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute algorithmic harm risk.")
    parser.add_argument("--error-likelihood", type=float, required=True)
    parser.add_argument("--severity", type=float, required=True)
    parser.add_argument("--exposure", type=float, required=True)
    parser.add_argument("--contestability", type=float, required=True)
    args = parser.parse_args()

    risk = args.error_likelihood * args.severity * args.exposure * (1.0 - args.contestability)
    print(f"harm_risk_score={risk:.6f}")


if __name__ == "__main__":
    main()
