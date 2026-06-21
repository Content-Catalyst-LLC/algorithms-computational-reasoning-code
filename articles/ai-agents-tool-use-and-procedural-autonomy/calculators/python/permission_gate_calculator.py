from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate an agent tool-use permission gate.")
    parser.add_argument("--risk", type=float, required=True)
    parser.add_argument("--approval-required", type=int, choices=[0, 1], required=True)
    parser.add_argument("--approved", type=int, choices=[0, 1], required=True)
    parser.add_argument("--threshold", type=float, default=0.65)
    args = parser.parse_args()

    approval_violation = args.approval_required == 1 and args.approved == 0
    escalation = args.risk >= args.threshold
    if approval_violation:
        status = "blocked"
    elif escalation:
        status = "escalate"
    else:
        status = "pass"

    print(f"risk={args.risk:.6f}")
    print(f"approval_required={args.approval_required}")
    print(f"approved={args.approved}")
    print(f"status={status}")


if __name__ == "__main__":
    main()
