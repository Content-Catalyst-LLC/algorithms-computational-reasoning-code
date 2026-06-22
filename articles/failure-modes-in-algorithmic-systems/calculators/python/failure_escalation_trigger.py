from __future__ import annotations
import argparse

def main() -> None:
    parser = argparse.ArgumentParser(description="Flag failure-mode escalation.")
    parser.add_argument("--failure-risk", type=float, required=True)
    parser.add_argument("--resilience", type=float, required=True)
    parser.add_argument("--failure-threshold", type=float, default=0.20)
    parser.add_argument("--resilience-threshold", type=float, default=0.60)
    args = parser.parse_args()
    escalate = int(args.failure_risk >= args.failure_threshold and args.resilience < args.resilience_threshold)
    print(f"failure_risk={args.failure_risk:.6f}")
    print(f"resilience_capacity={args.resilience:.6f}")
    print(f"escalate={escalate}")

if __name__ == "__main__":
    main()
