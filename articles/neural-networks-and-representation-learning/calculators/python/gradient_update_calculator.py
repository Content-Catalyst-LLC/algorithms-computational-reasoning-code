from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a one-step gradient update for a parameter.")
    parser.add_argument("--theta", type=float, required=True)
    parser.add_argument("--gradient", type=float, required=True)
    parser.add_argument("--learning-rate", type=float, required=True)
    args = parser.parse_args()
    updated = args.theta - args.learning_rate * args.gradient
    print(f"theta={args.theta:.6f}")
    print(f"gradient={args.gradient:.6f}")
    print(f"learning_rate={args.learning_rate:.6f}")
    print(f"updated_theta={updated:.6f}")


if __name__ == "__main__":
    main()
