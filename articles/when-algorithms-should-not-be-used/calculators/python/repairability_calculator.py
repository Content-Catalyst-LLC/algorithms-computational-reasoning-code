from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute repairability.")
    parser.add_argument("--detection", type=float, required=True)
    parser.add_argument("--correction", type=float, required=True)
    parser.add_argument("--remedy", type=float, required=True)
    parser.add_argument("--recurrence-prevention", type=float, required=True)
    args = parser.parse_args()

    score = (args.detection + args.correction + args.remedy + args.recurrence_prevention) / 4.0
    print(f"repairability_score={score:.6f}")


if __name__ == "__main__":
    main()
