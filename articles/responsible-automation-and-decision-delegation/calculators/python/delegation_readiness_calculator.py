from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute delegation readiness score.")
    parser.add_argument("--evidence-quality", type=float, required=True)
    parser.add_argument("--validation", type=float, required=True)
    parser.add_argument("--reversibility", type=float, required=True)
    parser.add_argument("--contestability", type=float, required=True)
    parser.add_argument("--governance", type=float, required=True)
    parser.add_argument("--human-review", type=float, required=True)
    args = parser.parse_args()

    score = (
        args.evidence_quality
        + args.validation
        + args.reversibility
        + args.contestability
        + args.governance
        + args.human_review
    ) / 6.0
    print(f"delegation_readiness_score={score:.6f}")


if __name__ == "__main__":
    main()
