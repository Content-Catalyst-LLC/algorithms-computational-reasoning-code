from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute symbolic constraint satisfaction.")
    parser.add_argument("--known", required=True, help="Comma-separated known facts")
    parser.add_argument("--required", required=True, help="Comma-separated required constraints")
    args = parser.parse_args()

    known = {item.strip() for item in args.known.split(",") if item.strip()}
    required = {item.strip() for item in args.required.split(",") if item.strip()}
    satisfied = sorted(required & known)
    missing = sorted(required - known)
    score = 1.0 if not required else len(satisfied) / len(required)

    print(f"required={sorted(required)}")
    print(f"satisfied={satisfied}")
    print(f"missing={missing}")
    print(f"satisfaction_score={score:.6f}")


if __name__ == "__main__":
    main()
