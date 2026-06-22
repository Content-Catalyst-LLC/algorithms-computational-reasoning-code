from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute performance decay from baseline.")
    parser.add_argument("--baseline", type=float, required=True)
    parser.add_argument("--current", type=float, required=True)
    args = parser.parse_args()

    decay = args.baseline - args.current
    print(f"baseline={args.baseline:.6f}")
    print(f"current={args.current:.6f}")
    print(f"performance_decay={decay:.6f}")


if __name__ == "__main__":
    main()
