from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a simple resilience score.")
    parser.add_argument("--post-shock-performance", type=float, required=True)
    parser.add_argument("--recovery-performance", type=float, required=True)
    parser.add_argument("--baseline-performance", type=float, required=True)
    args = parser.parse_args()

    if args.baseline_performance <= 0:
        raise SystemExit("baseline performance must be positive")
    shock_absorption = args.post_shock_performance / args.baseline_performance
    recovery = args.recovery_performance / args.baseline_performance
    score = max(0.0, min(1.0, (shock_absorption + recovery) / 2.0))
    print(f"resilience_score={score:.6f}")


if __name__ == "__main__":
    main()
