from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute expected value of action.")
    parser.add_argument("--probability", type=float, required=True)
    parser.add_argument("--benefit-if-act", type=float, required=True)
    parser.add_argument("--cost-if-act", type=float, required=True)
    args = parser.parse_args()

    score = args.probability * args.benefit_if_act - args.cost_if_act
    print(f"expected_value_of_action={score:.6f}")


if __name__ == "__main__":
    main()
