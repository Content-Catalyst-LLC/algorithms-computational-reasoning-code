from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute algorithmic non-use pressure.")
    parser.add_argument("--stakes", type=float, required=True)
    parser.add_argument("--irreversibility", type=float, required=True)
    parser.add_argument("--governance-weakness", type=float, required=True)
    parser.add_argument("--proxy-illegitimacy", type=float, required=True)
    args = parser.parse_args()

    score = (args.stakes + args.irreversibility + args.governance_weakness + args.proxy_illegitimacy) / 4.0
    print(f"non_use_pressure_score={score:.6f}")


if __name__ == "__main__":
    main()
