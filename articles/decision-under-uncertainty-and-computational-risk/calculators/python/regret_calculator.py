from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute regret relative to best option value.")
    parser.add_argument("--chosen-value", type=float, required=True)
    parser.add_argument("--best-value", type=float, required=True)
    args = parser.parse_args()
    regret = max(0.0, args.best_value - args.chosen_value)
    print(f"regret={regret:.6f}")


if __name__ == "__main__":
    main()
