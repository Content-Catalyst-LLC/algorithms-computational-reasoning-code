from __future__ import annotations

import argparse


def safe_div(n: float, d: float) -> float:
    return 0.0 if d == 0 else n / d


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute sensitivity and specificity.")
    parser.add_argument("--tp", type=float, required=True)
    parser.add_argument("--tn", type=float, required=True)
    parser.add_argument("--fp", type=float, required=True)
    parser.add_argument("--fn", type=float, required=True)
    args = parser.parse_args()

    sensitivity = safe_div(args.tp, args.tp + args.fn)
    specificity = safe_div(args.tn, args.tn + args.fp)
    print(f"sensitivity={sensitivity:.6f}")
    print(f"specificity={specificity:.6f}")


if __name__ == "__main__":
    main()
