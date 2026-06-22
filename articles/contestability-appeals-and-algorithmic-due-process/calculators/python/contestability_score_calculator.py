from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute contestability score.")
    parser.add_argument("--notice", type=float, required=True)
    parser.add_argument("--reasons", type=float, required=True)
    parser.add_argument("--evidence-access", type=float, required=True)
    parser.add_argument("--human-review", type=float, required=True)
    parser.add_argument("--correction", type=float, required=True)
    parser.add_argument("--remedy", type=float, required=True)
    args = parser.parse_args()

    score = (args.notice + args.reasons + args.evidence_access + args.human_review + args.correction + args.remedy) / 6.0
    print(f"contestability_score={score:.6f}")


if __name__ == "__main__":
    main()
