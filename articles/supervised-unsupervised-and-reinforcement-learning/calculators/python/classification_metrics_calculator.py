from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute classification metrics from a confusion matrix.")
    parser.add_argument("--tp", type=int, required=True)
    parser.add_argument("--fp", type=int, required=True)
    parser.add_argument("--tn", type=int, required=True)
    parser.add_argument("--fn", type=int, required=True)
    args = parser.parse_args()
    total = max(1, args.tp + args.fp + args.tn + args.fn)
    accuracy = (args.tp + args.tn) / total
    precision = args.tp / max(1, args.tp + args.fp)
    recall = args.tp / max(1, args.tp + args.fn)
    f1 = 0.0 if precision + recall == 0 else 2 * precision * recall / (precision + recall)
    print(f"accuracy={accuracy:.6f}")
    print(f"precision={precision:.6f}")
    print(f"recall={recall:.6f}")
    print(f"f1={f1:.6f}")


if __name__ == "__main__":
    main()
