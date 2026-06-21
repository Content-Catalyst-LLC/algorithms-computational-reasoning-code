from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a simple intervention effect contrast.")
    parser.add_argument("--baseline-outcome", type=float, required=True)
    parser.add_argument("--intervention-outcome", type=float, required=True)
    args = parser.parse_args()
    effect = args.intervention_outcome - args.baseline_outcome
    print(f"baseline_outcome={args.baseline_outcome:.6f}")
    print(f"intervention_outcome={args.intervention_outcome:.6f}")
    print(f"estimated_effect={effect:.6f}")


if __name__ == "__main__":
    main()
