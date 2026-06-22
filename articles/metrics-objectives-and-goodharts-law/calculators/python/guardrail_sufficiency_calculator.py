from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Check guardrail sufficiency.")
    parser.add_argument("--guardrails", type=int, required=True)
    parser.add_argument("--minimum", type=int, default=2)
    args = parser.parse_args()

    sufficient = int(args.guardrails >= args.minimum)
    print(f"guardrails={args.guardrails}")
    print(f"minimum={args.minimum}")
    print(f"sufficient={sufficient}")


if __name__ == "__main__":
    main()
