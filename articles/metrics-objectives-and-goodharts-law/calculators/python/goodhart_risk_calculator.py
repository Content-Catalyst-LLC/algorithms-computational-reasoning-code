from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a simple Goodhart risk score.")
    parser.add_argument("--proxy-gap", type=float, required=True)
    parser.add_argument("--pressure", type=float, required=True)
    parser.add_argument("--gaming-risk", type=float, required=True)
    parser.add_argument("--guardrails", type=int, required=True)
    parser.add_argument("--minimum-guardrails", type=int, default=2)
    args = parser.parse_args()

    guardrail_penalty = 1.0 if args.guardrails < args.minimum_guardrails else 0.0
    score = (args.proxy_gap + args.pressure + args.gaming_risk + guardrail_penalty) / 4.0
    status = "pass"
    if args.pressure >= 0.70 and args.proxy_gap >= 0.20:
        status = "review"
    if args.pressure >= 0.70 and args.proxy_gap >= 0.20 and (args.gaming_risk >= 0.60 or guardrail_penalty == 1.0):
        status = "escalate"

    print(f"goodhart_risk_score={score:.6f}")
    print(f"status={status}")


if __name__ == "__main__":
    main()
