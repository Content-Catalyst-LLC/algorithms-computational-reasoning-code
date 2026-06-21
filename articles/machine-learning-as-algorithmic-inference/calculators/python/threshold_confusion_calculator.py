from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute classification rates from confusion-matrix counts.")
    parser.add_argument("--tp", type=int, required=True)
    parser.add_argument("--fp", type=int, required=True)
    parser.add_argument("--tn", type=int, required=True)
    parser.add_argument("--fn", type=int, required=True)
    args = parser.parse_args()
    total = max(1, args.tp + args.fp + args.tn + args.fn)
    accuracy = (args.tp + args.tn) / total
    precision = args.tp / max(1, args.tp + args.fp)
    recall = args.tp / max(1, args.tp + args.fn)
    fpr = args.fp / max(1, args.fp + args.tn)
    fnr = args.fn / max(1, args.fn + args.tp)
    print(f"accuracy={accuracy:.6f}")
    print(f"precision={precision:.6f}")
    print(f"recall={recall:.6f}")
    print(f"false_positive_rate={fpr:.6f}")
    print(f"false_negative_rate={fnr:.6f}")


if __name__ == "__main__":
    main()
