from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute documentation completeness.")
    parser.add_argument("--completed-fields", type=float, required=True)
    parser.add_argument("--required-fields", type=float, required=True)
    args = parser.parse_args()

    score = 0.0 if args.required_fields == 0 else args.completed_fields / args.required_fields
    print(f"documentation_completeness_score={score:.6f}")


if __name__ == "__main__":
    main()
