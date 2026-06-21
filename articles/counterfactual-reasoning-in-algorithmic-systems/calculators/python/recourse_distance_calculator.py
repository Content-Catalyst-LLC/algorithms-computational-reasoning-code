from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute simple recourse distance and cost.")
    parser.add_argument("--current", type=float, required=True)
    parser.add_argument("--target", type=float, required=True)
    parser.add_argument("--unit-cost", type=float, required=True)
    args = parser.parse_args()
    delta = args.target - args.current
    cost = abs(delta) * args.unit_cost
    print(f"current={args.current:.6f}")
    print(f"target={args.target:.6f}")
    print(f"delta={delta:.6f}")
    print(f"cost={cost:.6f}")


if __name__ == "__main__":
    main()
