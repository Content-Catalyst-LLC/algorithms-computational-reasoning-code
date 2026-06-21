from __future__ import annotations
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare unregularized and regularized held-out error.")
    parser.add_argument("--unregularized-test-error", type=float, required=True)
    parser.add_argument("--regularized-test-error", type=float, required=True)
    args = parser.parse_args()
    improvement = args.unregularized_test_error - args.regularized_test_error
    percent = 100.0 * improvement / args.unregularized_test_error if args.unregularized_test_error else 0.0
    print(f"unregularized_test_error={args.unregularized_test_error:.6f}")
    print(f"regularized_test_error={args.regularized_test_error:.6f}")
    print(f"absolute_improvement={improvement:.6f}")
    print(f"percent_improvement={percent:.2f}")


if __name__ == "__main__":
    main()
