from __future__ import annotations
import argparse
import csv


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a simple inverse-probability weighted effect from a CSV.")
    parser.add_argument("--csv", required=True, help="CSV with treatment, observed_outcome, and treatment_probability columns.")
    args = parser.parse_args()
    treated_num = treated_den = control_num = control_den = 0.0
    with open(args.csv, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            p = min(0.95, max(0.05, float(row["treatment_probability"])))
            y = float(row["observed_outcome"])
            if int(row["treatment"]) == 1:
                w = 1.0 / p
                treated_num += w * y
                treated_den += w
            else:
                w = 1.0 / (1.0 - p)
                control_num += w * y
                control_den += w
    effect = treated_num / treated_den - control_num / control_den
    print(f"ipw_effect={effect:.6f}")


if __name__ == "__main__":
    main()
