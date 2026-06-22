from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute simple measurement risk score.")
    parser.add_argument("--validity-gap", type=float, required=True)
    parser.add_argument("--missingness", type=float, required=True)
    parser.add_argument("--differential-error", type=float, required=True)
    parser.add_argument("--label-error", type=float, required=True)
    args = parser.parse_args()

    score = (args.validity_gap + args.missingness + args.differential_error + args.label_error) / 4.0
    status = "pass"
    if args.validity_gap >= 0.30 or args.differential_error >= 0.15 or args.label_error >= 0.10:
        status = "review"
    if args.validity_gap >= 0.30 and (args.missingness >= 0.20 or args.differential_error >= 0.15 or args.label_error >= 0.10):
        status = "escalate"

    print(f"measurement_risk_score={score:.6f}")
    print(f"status={status}")


if __name__ == "__main__":
    main()
