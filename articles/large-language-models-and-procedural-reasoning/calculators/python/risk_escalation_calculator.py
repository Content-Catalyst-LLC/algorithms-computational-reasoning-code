from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Classify LLM output review status from component scores.")
    parser.add_argument("--procedural-score", type=float, required=True)
    parser.add_argument("--source-score", type=float, required=True)
    parser.add_argument("--risk-score", type=float, required=True)
    parser.add_argument("--stakes", choices=["low", "medium", "high"], default="medium")
    args = parser.parse_args()
    overall = (args.procedural_score + args.source_score + args.risk_score) / 3.0
    if args.stakes == "high" and (args.risk_score < 1.0 or args.source_score < 1.0 or args.procedural_score < 1.0):
        status = "escalate"
    elif overall >= 0.80:
        status = "pass"
    else:
        status = "review"
    print(f"overall_score={overall:.6f}")
    print(f"status={status}")


if __name__ == "__main__":
    main()
