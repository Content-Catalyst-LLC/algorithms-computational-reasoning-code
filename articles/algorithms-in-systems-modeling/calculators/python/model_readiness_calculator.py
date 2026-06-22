from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute systems model readiness.")
    parser.add_argument("--calibration", type=float, required=True)
    parser.add_argument("--documentation", type=float, required=True)
    parser.add_argument("--governance", type=float, required=True)
    parser.add_argument("--resilience", type=float, required=True)
    args = parser.parse_args()

    score = (args.calibration + args.documentation + args.governance + args.resilience) / 4.0
    print(f"model_readiness_score={score:.6f}")


if __name__ == "__main__":
    main()
