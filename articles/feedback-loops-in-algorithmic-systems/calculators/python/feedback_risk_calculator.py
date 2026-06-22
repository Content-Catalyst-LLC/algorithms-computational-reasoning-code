from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a simple algorithmic feedback risk score.")
    parser.add_argument("--amplification", type=float, required=True)
    parser.add_argument("--concentration", type=float, required=True)
    parser.add_argument("--intervention", type=float, required=True)
    parser.add_argument("--drift", type=float, required=True)
    parser.add_argument("--recursive-data", type=float, required=True)
    args = parser.parse_args()

    score = (args.amplification + args.concentration + args.intervention + args.drift + args.recursive_data) / 5.0
    status = "pass"
    if args.amplification >= 0.70 or args.concentration >= 0.65 or args.drift >= 0.25 or args.recursive_data >= 0.30:
        status = "review"
    if (args.amplification >= 0.70 and args.concentration >= 0.65) or (args.drift >= 0.25 and args.recursive_data >= 0.30):
        status = "escalate"

    print(f"feedback_risk_score={score:.6f}")
    print(f"status={status}")


if __name__ == "__main__":
    main()
