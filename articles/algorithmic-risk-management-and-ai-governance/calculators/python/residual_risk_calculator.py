from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute residual risk score.")
    parser.add_argument("--inherent-risk", type=float, required=True)
    parser.add_argument("--control-effectiveness", type=float, required=True)
    args = parser.parse_args()

    score = args.inherent_risk * (1.0 - args.control_effectiveness)
    print(f"residual_risk_score={score:.6f}")


if __name__ == "__main__":
    main()
