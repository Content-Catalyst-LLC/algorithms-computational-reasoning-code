from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute documentation freshness.")
    parser.add_argument("--days-since-update", type=float, required=True)
    parser.add_argument("--required-review-interval", type=float, required=True)
    args = parser.parse_args()

    if args.required_review_interval <= 0:
        freshness = 0.0
    else:
        freshness = max(0.0, 1.0 - args.days_since_update / args.required_review_interval)
    print(f"freshness_score={freshness:.6f}")


if __name__ == "__main__":
    main()
