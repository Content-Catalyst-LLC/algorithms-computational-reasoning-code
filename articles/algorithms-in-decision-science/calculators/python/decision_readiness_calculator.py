from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute decision-support readiness.")
    parser.add_argument("--calibration", type=float, required=True)
    parser.add_argument("--uncertainty-communication", type=float, required=True)
    parser.add_argument("--human-review", type=float, required=True)
    parser.add_argument("--contestability", type=float, required=True)
    parser.add_argument("--governance", type=float, required=True)
    args = parser.parse_args()

    score = (
        args.calibration
        + args.uncertainty_communication
        + args.human_review
        + args.contestability
        + args.governance
    ) / 5.0
    print(f"decision_support_readiness_score={score:.6f}")


if __name__ == "__main__":
    main()
