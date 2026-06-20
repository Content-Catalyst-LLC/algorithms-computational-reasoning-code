from __future__ import annotations

import argparse
import json

try:
    from .audit import threshold_report
except ImportError:
    from audit import threshold_report


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute threshold classification metrics.")
    parser.add_argument("--threshold", type=float, default=0.50)
    parser.add_argument("--false-positive-cost", type=float, default=1.0)
    parser.add_argument("--false-negative-cost", type=float, default=3.0)
    args = parser.parse_args()

    report = threshold_report(
        threshold=args.threshold,
        fp_cost=args.false_positive_cost,
        fn_cost=args.false_negative_cost,
    )
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
