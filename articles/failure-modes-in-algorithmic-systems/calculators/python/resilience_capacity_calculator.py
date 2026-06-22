from __future__ import annotations
import argparse

def main() -> None:
    parser = argparse.ArgumentParser(description="Compute resilience capacity.")
    parser.add_argument("--monitoring", type=float, required=True)
    parser.add_argument("--fallback", type=float, required=True)
    parser.add_argument("--rollback", type=float, required=True)
    parser.add_argument("--escalation", type=float, required=True)
    parser.add_argument("--repair", type=float, required=True)
    args = parser.parse_args()
    score = (args.monitoring + args.fallback + args.rollback + args.escalation + args.repair) / 5.0
    print(f"resilience_capacity={score:.6f}")

if __name__ == "__main__":
    main()
