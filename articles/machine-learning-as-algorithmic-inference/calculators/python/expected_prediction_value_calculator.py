from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute expected value of acting on a model score.")
    parser.add_argument("--score", type=float, required=True, help="Estimated probability of beneficial/target event")
    parser.add_argument("--benefit", type=float, required=True, help="Benefit if action is appropriate")
    parser.add_argument("--harm", type=float, required=True, help="Harm/cost if action is inappropriate")
    args = parser.parse_args()
    ev = args.score * args.benefit - (1.0 - args.score) * args.harm
    print(f"score={args.score:.6f}")
    print(f"expected_value={ev:.6f}")
    print(f"recommended_action={'act' if ev >= 0 else 'do_not_act'}")


if __name__ == "__main__":
    main()
