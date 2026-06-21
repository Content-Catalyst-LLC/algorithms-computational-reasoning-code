from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute expected reward for an action probability and reward value.")
    parser.add_argument("--reward-probability", type=float, required=True)
    parser.add_argument("--reward-value", type=float, default=1.0)
    parser.add_argument("--cost", type=float, default=0.0)
    args = parser.parse_args()
    expected_reward = args.reward_probability * args.reward_value - args.cost
    print(f"reward_probability={args.reward_probability:.6f}")
    print(f"reward_value={args.reward_value:.6f}")
    print(f"cost={args.cost:.6f}")
    print(f"expected_reward={expected_reward:.6f}")


if __name__ == "__main__":
    main()
