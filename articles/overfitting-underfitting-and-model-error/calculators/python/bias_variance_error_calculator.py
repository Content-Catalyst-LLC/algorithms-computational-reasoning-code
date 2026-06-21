from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Combine bias, variance, and irreducible error terms.")
    parser.add_argument("--bias", type=float, required=True)
    parser.add_argument("--variance", type=float, required=True)
    parser.add_argument("--irreducible", type=float, default=0.0)
    args = parser.parse_args()
    total = args.bias ** 2 + args.variance + args.irreducible
    print(f"bias_squared={args.bias ** 2:.6f}")
    print(f"variance={args.variance:.6f}")
    print(f"irreducible_error={args.irreducible:.6f}")
    print(f"total_expected_error={total:.6f}")


if __name__ == "__main__":
    main()
