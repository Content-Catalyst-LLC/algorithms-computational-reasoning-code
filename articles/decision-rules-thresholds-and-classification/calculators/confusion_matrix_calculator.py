from __future__ import annotations

import argparse
import csv
from pathlib import Path


def safe_divide(a: float, b: float) -> float:
    return 0.0 if b == 0 else a / b


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute binary classification metrics from score/actual CSV.")
    parser.add_argument("--csv", type=Path, default=Path("data/classification_cases.csv"))
    parser.add_argument("--threshold", type=float, default=0.5)
    args = parser.parse_args()

    counts = {"TP": 0, "FP": 0, "TN": 0, "FN": 0}

    with args.csv.open("r", newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            pred = 1 if float(row["score"]) >= args.threshold else 0
            actual = int(row["actual"])

            if pred == 1 and actual == 1:
                counts["TP"] += 1
            elif pred == 1 and actual == 0:
                counts["FP"] += 1
            elif pred == 0 and actual == 0:
                counts["TN"] += 1
            else:
                counts["FN"] += 1

    tp, fp, tn, fn = counts["TP"], counts["FP"], counts["TN"], counts["FN"]
    print(f"threshold={args.threshold}")
    print(f"TP={tp} FP={fp} TN={tn} FN={fn}")
    print(f"precision={safe_divide(tp, tp + fp):.6f}")
    print(f"recall={safe_divide(tp, tp + fn):.6f}")
    print(f"specificity={safe_divide(tn, tn + fp):.6f}")


if __name__ == "__main__":
    main()
