from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a transparent weighted risk score.")
    parser.add_argument("--probability", type=float, required=True)
    parser.add_argument("--severity", type=float, required=True)
    parser.add_argument("--uncertainty", type=float, default=0.0)
    args = parser.parse_args()
    score = args.probability * args.severity * (1.0 + args.uncertainty)
    print(f"risk_score={score:.6f}")


if __name__ == "__main__":
    main()
