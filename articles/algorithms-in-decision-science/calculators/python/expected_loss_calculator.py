from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute expected loss if no action.")
    parser.add_argument("--probability", type=float, required=True)
    parser.add_argument("--loss-if-miss", type=float, required=True)
    args = parser.parse_args()

    score = args.probability * args.loss_if_miss
    print(f"expected_loss_if_no_action={score:.6f}")


if __name__ == "__main__":
    main()
