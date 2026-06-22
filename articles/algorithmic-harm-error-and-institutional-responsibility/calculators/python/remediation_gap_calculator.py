from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute remediation gap.")
    parser.add_argument("--severity", type=float, required=True)
    parser.add_argument("--repair", type=float, required=True)
    args = parser.parse_args()

    gap = max(0.0, args.severity - args.repair)
    print(f"severity={args.severity:.6f}")
    print(f"repair_capacity={args.repair:.6f}")
    print(f"remediation_gap={gap:.6f}")


if __name__ == "__main__":
    main()
