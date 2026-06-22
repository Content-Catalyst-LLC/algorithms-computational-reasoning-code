from __future__ import annotations
import argparse

def main() -> None:
    parser = argparse.ArgumentParser(description="Compute failure priority score.")
    parser.add_argument("--likelihood", type=float, required=True)
    parser.add_argument("--severity", type=float, required=True)
    parser.add_argument("--detectability", type=float, required=True)
    args = parser.parse_args()
    priority = args.likelihood * args.severity * (1.0 - args.detectability)
    print(f"failure_priority_score={priority:.6f}")

if __name__ == "__main__":
    main()
