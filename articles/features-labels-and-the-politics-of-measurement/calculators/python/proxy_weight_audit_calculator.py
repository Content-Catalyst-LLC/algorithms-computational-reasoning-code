from __future__ import annotations
import argparse

def main() -> None:
    parser = argparse.ArgumentParser(description="Flag proxy dominance and missingness risk.")
    parser.add_argument("--proxy-weight", type=float, required=True)
    parser.add_argument("--construct-weight", type=float, required=True)
    parser.add_argument("--missingness-rate", type=float, required=True)
    args = parser.parse_args()
    dominance_ratio = args.proxy_weight / args.construct_weight if args.construct_weight != 0 else float("inf")
    risk = "high" if dominance_ratio > 1.5 or args.missingness_rate > 0.20 else "review" if dominance_ratio > 1.0 or args.missingness_rate > 0.10 else "lower"
    print(f"proxy_to_construct_weight_ratio={dominance_ratio:.6f}")
    print(f"missingness_rate={args.missingness_rate:.6f}")
    print(f"measurement_review_risk={risk}")

if __name__ == "__main__":
    main()
