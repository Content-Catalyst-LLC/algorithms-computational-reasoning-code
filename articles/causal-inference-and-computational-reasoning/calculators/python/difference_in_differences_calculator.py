from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a difference-in-differences estimate.")
    parser.add_argument("--treated-pre", type=float, required=True)
    parser.add_argument("--treated-post", type=float, required=True)
    parser.add_argument("--control-pre", type=float, required=True)
    parser.add_argument("--control-post", type=float, required=True)
    args = parser.parse_args()
    treated_change = args.treated_post - args.treated_pre
    control_change = args.control_post - args.control_pre
    did = treated_change - control_change
    print(f"treated_change={treated_change:.6f}")
    print(f"control_change={control_change:.6f}")
    print(f"did_estimate={did:.6f}")


if __name__ == "__main__":
    main()
