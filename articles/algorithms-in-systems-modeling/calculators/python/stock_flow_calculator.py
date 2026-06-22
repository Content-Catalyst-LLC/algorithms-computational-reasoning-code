from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a stock-and-flow update.")
    parser.add_argument("--current-stock", type=float, required=True)
    parser.add_argument("--inflow", type=float, required=True)
    parser.add_argument("--outflow", type=float, required=True)
    args = parser.parse_args()

    next_stock = args.current_stock + args.inflow - args.outflow
    print(f"next_stock={next_stock:.6f}")


if __name__ == "__main__":
    main()
