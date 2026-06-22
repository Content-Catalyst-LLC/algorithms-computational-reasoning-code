from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute proxy gap from proxy-goal alignment.")
    parser.add_argument("--alignment", type=float, required=True)
    args = parser.parse_args()
    gap = 1.0 - args.alignment
    print(f"alignment={args.alignment:.6f}")
    print(f"proxy_gap={gap:.6f}")


if __name__ == "__main__":
    main()
