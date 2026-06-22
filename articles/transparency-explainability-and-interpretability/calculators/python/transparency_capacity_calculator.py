from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute transparency capacity score.")
    parser.add_argument("--documentation", type=float, required=True)
    parser.add_argument("--governance", type=float, required=True)
    parser.add_argument("--uncertainty", type=float, required=True)
    args = parser.parse_args()

    score = (args.documentation + args.governance + args.uncertainty) / 3.0
    print(f"transparency_capacity_score={score:.6f}")


if __name__ == "__main__":
    main()
