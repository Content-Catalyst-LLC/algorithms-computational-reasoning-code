from __future__ import annotations
import argparse

def main() -> None:
    parser = argparse.ArgumentParser(description="Compute algorithmic failure risk.")
    parser.add_argument("--likelihood", type=float, required=True)
    parser.add_argument("--severity", type=float, required=True)
    parser.add_argument("--detectability", type=float, required=True)
    parser.add_argument("--controllability", type=float, required=True)
    args = parser.parse_args()
    risk = args.likelihood * args.severity * (1.0 - args.detectability) * (1.0 - args.controllability)
    print(f"failure_risk_score={risk:.6f}")

if __name__ == "__main__":
    main()
