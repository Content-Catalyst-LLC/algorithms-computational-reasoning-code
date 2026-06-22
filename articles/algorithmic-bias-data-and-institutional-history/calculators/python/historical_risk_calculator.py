from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute simplified historical-risk score.")
    parser.add_argument("--provenance-risk", type=float, required=True)
    parser.add_argument("--measurement-weakness", type=float, required=True)
    parser.add_argument("--proxy-risk", type=float, required=True)
    parser.add_argument("--remediation", type=float, required=True)
    args = parser.parse_args()

    score = (args.provenance_risk + args.measurement_weakness + args.proxy_risk + (1.0 - args.remediation)) / 4.0
    print(f"historical_risk_score={score:.6f}")


if __name__ == "__main__":
    main()
