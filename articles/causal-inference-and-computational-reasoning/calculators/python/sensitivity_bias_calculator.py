from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Adjust a reported effect by hypothetical unmeasured bias.")
    parser.add_argument("--effect", type=float, required=True)
    parser.add_argument("--bias", type=float, required=True)
    args = parser.parse_args()
    adjusted = args.effect - args.bias
    print(f"reported_effect={args.effect:.6f}")
    print(f"hypothetical_bias={args.bias:.6f}")
    print(f"bias_adjusted_effect={adjusted:.6f}")


if __name__ == "__main__":
    main()
