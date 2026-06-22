from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Classify whether a score crosses threshold.")
    parser.add_argument("--score", type=float, required=True)
    parser.add_argument("--threshold", type=float, required=True)
    args = parser.parse_args()

    action = args.score >= args.threshold
    print(f"threshold_action={str(action).lower()}")


if __name__ == "__main__":
    main()
