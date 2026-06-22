from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute simplified computational justice capacity.")
    parser.add_argument("--fairness-evidence", type=float, required=True)
    parser.add_argument("--measurement-validity", type=float, required=True)
    parser.add_argument("--contestability", type=float, required=True)
    parser.add_argument("--remediation", type=float, required=True)
    args = parser.parse_args()

    score = (args.fairness_evidence + args.measurement_validity + args.contestability + args.remediation) / 4.0
    print(f"justice_capacity_score={score:.6f}")


if __name__ == "__main__":
    main()
