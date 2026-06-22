from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute incident recurrence ratio.")
    parser.add_argument("--repeat-incidents", type=float, required=True)
    parser.add_argument("--total-incidents", type=float, required=True)
    args = parser.parse_args()

    score = 0.0 if args.total_incidents == 0 else args.repeat_incidents / args.total_incidents
    print(f"incident_recurrence_score={score:.6f}")


if __name__ == "__main__":
    main()
