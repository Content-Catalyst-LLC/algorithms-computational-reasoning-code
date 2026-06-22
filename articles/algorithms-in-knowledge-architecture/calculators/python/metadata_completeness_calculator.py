from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute metadata completeness.")
    parser.add_argument("--present-fields", type=float, required=True)
    parser.add_argument("--required-fields", type=float, required=True)
    args = parser.parse_args()

    if args.required_fields <= 0:
        raise SystemExit("required-fields must be positive")
    score = args.present_fields / args.required_fields
    score = max(0.0, min(1.0, score))
    print(f"metadata_completeness_score={score:.6f}")


if __name__ == "__main__":
    main()
