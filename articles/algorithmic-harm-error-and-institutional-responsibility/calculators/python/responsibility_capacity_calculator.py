from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute institutional responsibility capacity.")
    parser.add_argument("--ownership", type=float, required=True)
    parser.add_argument("--monitoring", type=float, required=True)
    parser.add_argument("--appeals", type=float, required=True)
    parser.add_argument("--repair", type=float, required=True)
    parser.add_argument("--governance", type=float, required=True)
    args = parser.parse_args()

    score = (args.ownership + args.monitoring + args.appeals + args.repair + args.governance) / 5.0
    print(f"responsibility_capacity={score:.6f}")


if __name__ == "__main__":
    main()
