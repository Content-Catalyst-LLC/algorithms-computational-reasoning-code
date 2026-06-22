from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute documentation risk.")
    parser.add_argument("--stakes", type=float, required=True)
    parser.add_argument("--documentation-quality", type=float, required=True)
    args = parser.parse_args()

    risk = args.stakes * (1.0 - args.documentation_quality)
    print(f"documentation_risk_score={risk:.6f}")


if __name__ == "__main__":
    main()
