from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute overreliance gap.")
    parser.add_argument("--acceptance", type=float, required=True)
    parser.add_argument("--quality", type=float, required=True)
    args = parser.parse_args()

    gap = max(0.0, args.acceptance - args.quality)
    print(f"acceptance_rate={args.acceptance:.6f}")
    print(f"model_quality={args.quality:.6f}")
    print(f"overreliance_gap={gap:.6f}")


if __name__ == "__main__":
    main()
