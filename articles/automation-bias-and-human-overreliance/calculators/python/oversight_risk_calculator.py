from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute simple oversight risk score.")
    parser.add_argument("--acceptance", type=float, required=True)
    parser.add_argument("--quality", type=float, required=True)
    parser.add_argument("--uncertainty", type=float, required=True)
    parser.add_argument("--review-time", type=float, required=True)
    parser.add_argument("--minimum-review-time", type=float, default=2.0)
    parser.add_argument("--override-friction", type=float, required=True)
    parser.add_argument("--appeal-pathway", type=int, required=True)
    args = parser.parse_args()

    overreliance_gap = max(0.0, args.acceptance - args.quality)
    review_deficit = max(0.0, (args.minimum_review_time - args.review_time) / args.minimum_review_time)
    weak_contestability = 1.0 if args.appeal_pathway == 0 else 0.0
    score = (args.acceptance + overreliance_gap + args.uncertainty + review_deficit + args.override_friction + weak_contestability) / 6.0

    status = "pass"
    if args.acceptance >= 0.85 or abs(args.acceptance - args.quality) >= 0.15 or review_deficit > 0 or args.override_friction >= 0.60 or weak_contestability:
        status = "review"
    if (args.acceptance >= 0.85 and args.quality <= 0.75) or (abs(args.acceptance - args.quality) >= 0.15 and review_deficit > 0) or (args.override_friction >= 0.60 and weak_contestability):
        status = "escalate"

    print(f"oversight_risk_score={score:.6f}")
    print(f"status={status}")


if __name__ == "__main__":
    main()
