from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute audit completeness score.")
    parser.add_argument("--required-records", type=float, required=True)
    parser.add_argument("--available-records", type=float, required=True)
    args = parser.parse_args()

    score = 0.0 if args.required_records == 0 else args.available_records / args.required_records
    print(f"audit_completeness_score={score:.6f}")


if __name__ == "__main__":
    main()
