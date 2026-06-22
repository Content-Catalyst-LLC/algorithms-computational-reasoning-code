from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute proxy validity gap.")
    parser.add_argument("--validity", type=float, required=True)
    args = parser.parse_args()
    gap = 1.0 - args.validity
    print(f"proxy_validity={args.validity:.6f}")
    print(f"validity_gap={gap:.6f}")


if __name__ == "__main__":
    main()
