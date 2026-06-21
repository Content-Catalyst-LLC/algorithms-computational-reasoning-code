from __future__ import annotations
import argparse

def main() -> None:
    parser = argparse.ArgumentParser(description="Estimate expected mislabeled records under label noise.")
    parser.add_argument("--sample-size", type=float, required=True)
    parser.add_argument("--noise-rate", type=float, required=True)
    args = parser.parse_args()
    mislabeled = args.sample_size * args.noise_rate
    correctly_labeled = args.sample_size - mislabeled
    print(f"sample_size={args.sample_size:.0f}")
    print(f"noise_rate={args.noise_rate:.6f}")
    print(f"expected_mislabeled_records={mislabeled:.2f}")
    print(f"expected_correctly_labeled_records={correctly_labeled:.2f}")

if __name__ == "__main__":
    main()
