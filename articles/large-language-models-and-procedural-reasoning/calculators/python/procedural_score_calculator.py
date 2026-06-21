from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a procedural step sufficiency score.")
    parser.add_argument("--steps-found", type=int, required=True)
    parser.add_argument("--minimum-steps", type=int, default=3)
    args = parser.parse_args()
    if args.minimum_steps <= 0:
        raise SystemExit("minimum-steps must be positive")
    score = min(1.0, args.steps_found / args.minimum_steps)
    print(f"steps_found={args.steps_found}")
    print(f"minimum_steps={args.minimum_steps}")
    print(f"procedural_score={score:.6f}")


if __name__ == "__main__":
    main()
