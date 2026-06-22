from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute proportional sensitivity.")
    parser.add_argument("--baseline-output", type=float, required=True)
    parser.add_argument("--changed-output", type=float, required=True)
    parser.add_argument("--baseline-parameter", type=float, required=True)
    parser.add_argument("--changed-parameter", type=float, required=True)
    args = parser.parse_args()

    if args.baseline_output == 0 or args.baseline_parameter == 0:
        raise SystemExit("baseline output and baseline parameter must be nonzero")
    output_change = (args.changed_output - args.baseline_output) / args.baseline_output
    parameter_change = (args.changed_parameter - args.baseline_parameter) / args.baseline_parameter
    if parameter_change == 0:
        raise SystemExit("parameter change must be nonzero")
    sensitivity = output_change / parameter_change
    print(f"sensitivity_score={sensitivity:.6f}")


if __name__ == "__main__":
    main()
