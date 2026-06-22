from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Flag algorithmic harm escalation.")
    parser.add_argument("--harm-risk", type=float, required=True)
    parser.add_argument("--responsibility-capacity", type=float, required=True)
    parser.add_argument("--harm-threshold", type=float, default=0.30)
    parser.add_argument("--responsibility-threshold", type=float, default=0.65)
    args = parser.parse_args()

    escalate = int(args.harm_risk >= args.harm_threshold and args.responsibility_capacity < args.responsibility_threshold)
    print(f"harm_risk={args.harm_risk:.6f}")
    print(f"responsibility_capacity={args.responsibility_capacity:.6f}")
    print(f"escalate={escalate}")


if __name__ == "__main__":
    main()
