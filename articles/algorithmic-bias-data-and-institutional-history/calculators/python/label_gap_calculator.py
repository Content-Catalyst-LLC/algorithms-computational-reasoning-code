from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute label gap.")
    parser.add_argument("--label-positive-rate", type=float, required=True)
    parser.add_argument("--verified-positive-rate", type=float, required=True)
    args = parser.parse_args()

    print(f"label_gap={abs(args.label_positive_rate - args.verified_positive_rate):.6f}")


if __name__ == "__main__":
    main()
