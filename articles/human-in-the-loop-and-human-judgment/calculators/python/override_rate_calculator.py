from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute human override rate.")
    parser.add_argument("--overrides", type=float, required=True)
    parser.add_argument("--reviewed-cases", type=float, required=True)
    args = parser.parse_args()

    score = 0.0 if args.reviewed_cases == 0 else args.overrides / args.reviewed_cases
    print(f"override_rate={score:.6f}")


if __name__ == "__main__":
    main()
