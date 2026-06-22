from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute governance readiness score.")
    parser.add_argument("--ownership", type=float, required=True)
    parser.add_argument("--documentation", type=float, required=True)
    parser.add_argument("--monitoring", type=float, required=True)
    parser.add_argument("--contestability", type=float, required=True)
    parser.add_argument("--remediation", type=float, required=True)
    parser.add_argument("--stop-authority", type=float, required=True)
    args = parser.parse_args()

    score = (
        args.ownership
        + args.documentation
        + args.monitoring
        + args.contestability
        + args.remediation
        + args.stop_authority
    ) / 6.0
    print(f"governance_readiness_score={score:.6f}")


if __name__ == "__main__":
    main()
