from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute responsible-use readiness.")
    parser.add_argument("--target-legitimacy", type=float, required=True)
    parser.add_argument("--data-legitimacy", type=float, required=True)
    parser.add_argument("--contestability", type=float, required=True)
    parser.add_argument("--human-judgment", type=float, required=True)
    parser.add_argument("--governance-capacity", type=float, required=True)
    parser.add_argument("--repairability", type=float, required=True)
    args = parser.parse_args()

    score = (
        args.target_legitimacy
        + args.data_legitimacy
        + args.contestability
        + args.human_judgment
        + args.governance_capacity
        + args.repairability
    ) / 6.0
    print(f"responsible_use_readiness_score={score:.6f}")


if __name__ == "__main__":
    main()
