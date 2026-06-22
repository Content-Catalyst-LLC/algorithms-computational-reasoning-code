from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute accountability capacity score.")
    parser.add_argument("--documentation", type=float, required=True)
    parser.add_argument("--provenance", type=float, required=True)
    parser.add_argument("--reviewability", type=float, required=True)
    parser.add_argument("--contestability", type=float, required=True)
    parser.add_argument("--remediation", type=float, required=True)
    parser.add_argument("--governance", type=float, required=True)
    args = parser.parse_args()

    score = (
        args.documentation
        + args.provenance
        + args.reviewability
        + args.contestability
        + args.remediation
        + args.governance
    ) / 6.0
    print(f"accountability_capacity_score={score:.6f}")


if __name__ == "__main__":
    main()
