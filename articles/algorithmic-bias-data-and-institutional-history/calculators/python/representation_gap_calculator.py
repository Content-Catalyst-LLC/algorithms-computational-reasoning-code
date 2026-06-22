from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute representation gap.")
    parser.add_argument("--data-share", type=float, required=True)
    parser.add_argument("--deployment-share", type=float, required=True)
    args = parser.parse_args()

    print(f"representation_gap={abs(args.data_share - args.deployment_share):.6f}")


if __name__ == "__main__":
    main()
