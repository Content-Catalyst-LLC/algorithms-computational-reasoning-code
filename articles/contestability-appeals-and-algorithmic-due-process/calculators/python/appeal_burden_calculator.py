from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute simplified appeal burden.")
    parser.add_argument("--time-burden", type=float, required=True)
    parser.add_argument("--form-complexity", type=float, required=True)
    parser.add_argument("--language-difficulty", type=float, required=True)
    parser.add_argument("--accessibility-support", type=float, required=True)
    args = parser.parse_args()

    burden = (args.time_burden + args.form_complexity + args.language_difficulty + (1.0 - args.accessibility_support)) / 4.0
    print(f"appeal_burden={burden:.6f}")


if __name__ == "__main__":
    main()
