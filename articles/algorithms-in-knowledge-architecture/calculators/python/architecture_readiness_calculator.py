from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute knowledge architecture readiness.")
    parser.add_argument("--metadata", type=float, required=True)
    parser.add_argument("--taxonomy", type=float, required=True)
    parser.add_argument("--search", type=float, required=True)
    parser.add_argument("--link", type=float, required=True)
    parser.add_argument("--recommendation", type=float, required=True)
    parser.add_argument("--provenance", type=float, required=True)
    parser.add_argument("--editorial-review", type=float, required=True)
    args = parser.parse_args()

    score = (
        args.metadata + args.taxonomy + args.search + args.link +
        args.recommendation + args.provenance + args.editorial_review
    ) / 7.0
    print(f"architecture_readiness_score={score:.6f}")


if __name__ == "__main__":
    main()
