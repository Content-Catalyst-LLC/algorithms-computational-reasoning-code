from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Flag drift review.")
    parser.add_argument("--drift", type=float, required=True)
    parser.add_argument("--threshold", type=float, default=0.25)
    args = parser.parse_args()

    trigger = int(args.drift >= args.threshold)
    print(f"drift={args.drift:.6f}")
    print(f"threshold={args.threshold:.6f}")
    print(f"review_trigger={trigger}")


if __name__ == "__main__":
    main()
