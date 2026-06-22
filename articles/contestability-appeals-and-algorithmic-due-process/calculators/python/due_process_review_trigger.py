from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Flag due-process review trigger.")
    parser.add_argument("--stakes", type=float, required=True)
    parser.add_argument("--contestability", type=float, required=True)
    parser.add_argument("--stakes-threshold", type=float, default=0.75)
    parser.add_argument("--contestability-threshold", type=float, default=0.70)
    args = parser.parse_args()

    trigger = int(args.stakes >= args.stakes_threshold and args.contestability < args.contestability_threshold)
    print(f"stakes={args.stakes:.6f}")
    print(f"contestability={args.contestability:.6f}")
    print(f"review_trigger={trigger}")


if __name__ == "__main__":
    main()
