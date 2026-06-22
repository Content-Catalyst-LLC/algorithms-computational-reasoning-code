from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute procedural risk from stakes and contestability.")
    parser.add_argument("--stakes", type=float, required=True)
    parser.add_argument("--contestability", type=float, required=True)
    args = parser.parse_args()

    risk = args.stakes * (1.0 - args.contestability)
    print(f"stakes={args.stakes:.6f}")
    print(f"contestability={args.contestability:.6f}")
    print(f"procedural_risk={risk:.6f}")


if __name__ == "__main__":
    main()
