from __future__ import annotations
import argparse

def rate(num: float, den: float) -> float:
    return 0.0 if den == 0 else num / den

def main() -> None:
    parser = argparse.ArgumentParser(description="Compute basic label/construct confusion metrics.")
    parser.add_argument("--tp", type=float, required=True)
    parser.add_argument("--fp", type=float, required=True)
    parser.add_argument("--tn", type=float, required=True)
    parser.add_argument("--fn", type=float, required=True)
    args = parser.parse_args()
    print(f"sensitivity={rate(args.tp, args.tp + args.fn):.6f}")
    print(f"specificity={rate(args.tn, args.tn + args.fp):.6f}")
    print(f"false_positive_rate={rate(args.fp, args.fp + args.tn):.6f}")
    print(f"false_negative_rate={rate(args.fn, args.fn + args.tp):.6f}")

if __name__ == "__main__":
    main()
