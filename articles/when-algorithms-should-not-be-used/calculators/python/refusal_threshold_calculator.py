from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Classify algorithmic refusal threshold.")
    parser.add_argument("--non-use-pressure", type=float, required=True)
    parser.add_argument("--responsible-readiness", type=float, required=True)
    parser.add_argument("--pressure-threshold", type=float, default=0.70)
    parser.add_argument("--readiness-threshold", type=float, default=0.65)
    args = parser.parse_args()

    status = "allow_with_controls"
    if args.non_use_pressure >= args.pressure_threshold and args.responsible_readiness < args.readiness_threshold:
        status = "refuse"
    elif args.responsible_readiness < args.readiness_threshold:
        status = "review_or_human_led"
    print(f"non_use_decision={status}")


if __name__ == "__main__":
    main()
