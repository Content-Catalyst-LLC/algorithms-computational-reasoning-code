from __future__ import annotations
import argparse

def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a simple causal effect contrast.")
    parser.add_argument("--treated-mean", type=float, required=True)
    parser.add_argument("--control-mean", type=float, required=True)
    args = parser.parse_args()
    effect = args.treated_mean - args.control_mean
    print(f"treated_mean={args.treated_mean:.6f}")
    print(f"control_mean={args.control_mean:.6f}")
    print(f"difference={effect:.6f}")

if __name__ == "__main__":
    main()
