from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Apply a simple decision threshold.")
    parser.add_argument("--risk", type=float, required=True)
    parser.add_argument("--expected-value", type=float, required=True)
    parser.add_argument("--risk-threshold", type=float, default=0.35)
    parser.add_argument("--value-threshold", type=float, default=0.08)
    args = parser.parse_args()
    if args.risk >= args.risk_threshold and args.expected_value >= args.value_threshold:
        action = "act_with_review"
    elif args.risk >= args.risk_threshold:
        action = "review_or_monitor"
    else:
        action = "defer_or_monitor"
    print(f"action={action}")


if __name__ == "__main__":
    main()
