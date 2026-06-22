from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Classify feedback effect.")
    parser.add_argument("--factor", type=float, required=True)
    args = parser.parse_args()

    if args.factor > 1.0:
        label = "amplifying"
    elif args.factor > 0.0:
        label = "dampening"
    else:
        label = "inverting_or_unstable"

    print(f"feedback_factor={args.factor:.6f}")
    print(f"classification={label}")


if __name__ == "__main__":
    main()
