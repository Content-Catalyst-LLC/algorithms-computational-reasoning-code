from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a simple feedback update.")
    parser.add_argument("--state", type=float, required=True)
    parser.add_argument("--intervention", type=float, required=True)
    parser.add_argument("--feedback-rate", type=float, required=True)
    parser.add_argument("--decay-rate", type=float, default=0.0)
    args = parser.parse_args()

    next_state = args.state + args.feedback_rate * args.state + args.intervention - args.decay_rate * args.state
    print(f"next_state={next_state:.6f}")


if __name__ == "__main__":
    main()
