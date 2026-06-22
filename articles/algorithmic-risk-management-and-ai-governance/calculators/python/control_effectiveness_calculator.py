from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute control effectiveness score.")
    parser.add_argument("--prevention", type=float, required=True)
    parser.add_argument("--detection", type=float, required=True)
    parser.add_argument("--mitigation", type=float, required=True)
    parser.add_argument("--response", type=float, required=True)
    args = parser.parse_args()

    score = (args.prevention + args.detection + args.mitigation + args.response) / 4.0
    print(f"control_effectiveness_score={score:.6f}")


if __name__ == "__main__":
    main()
