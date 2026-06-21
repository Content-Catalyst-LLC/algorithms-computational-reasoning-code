from __future__ import annotations

import argparse


def safe_div(n: float, d: float) -> float:
    return 0.0 if d == 0 else n / d


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute basic classification metrics.")
    parser.add_argument("--tp", type=float, required=True)
    parser.add_argument("--tn", type=float, required=True)
    parser.add_argument("--fp", type=float, required=True)
    parser.add_argument("--fn", type=float, required=True)
    args = parser.parse_args()

    accuracy = safe_div(args.tp + args.tn, args.tp + args.tn + args.fp + args.fn)
    precision = safe_div(args.tp, args.tp + args.fp)
    recall = safe_div(args.tp, args.tp + args.fn)
    f1 = safe_div(2 * precision * recall, precision + recall)

    print(f"accuracy={accuracy:.6f}")
    print(f"precision={precision:.6f}")
    print(f"recall={recall:.6f}")
    print(f"f1={f1:.6f}")


if __name__ == "__main__":
    main()
