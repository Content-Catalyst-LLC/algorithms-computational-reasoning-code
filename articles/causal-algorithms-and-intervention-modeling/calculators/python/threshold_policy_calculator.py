from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate a score under baseline and changed action thresholds.")
    parser.add_argument("--score", type=float, required=True)
    parser.add_argument("--baseline-threshold", type=float, default=0.55)
    parser.add_argument("--new-threshold", type=float, required=True)
    args = parser.parse_args()
    baseline = "act" if args.score >= args.baseline_threshold else "monitor"
    changed = "act" if args.score >= args.new_threshold else "monitor"
    print(f"score={args.score:.6f}")
    print(f"baseline_decision={baseline}")
    print(f"new_threshold_decision={changed}")
    print(f"decision_changed={baseline != changed}")


if __name__ == "__main__":
    main()
