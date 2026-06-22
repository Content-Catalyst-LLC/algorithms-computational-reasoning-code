from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute decision reconstruction risk.")
    parser.add_argument("--stakes", type=float, required=True)
    parser.add_argument("--audit-completeness", type=float, required=True)
    args = parser.parse_args()

    risk = args.stakes * (1.0 - args.audit_completeness)
    print(f"reconstruction_risk_score={risk:.6f}")


if __name__ == "__main__":
    main()
