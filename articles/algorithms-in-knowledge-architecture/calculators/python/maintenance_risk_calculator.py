from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute knowledge architecture maintenance risk.")
    parser.add_argument("--metadata", type=float, required=True)
    parser.add_argument("--link-quality", type=float, required=True)
    parser.add_argument("--freshness", type=float, required=True)
    parser.add_argument("--provenance", type=float, required=True)
    args = parser.parse_args()

    score = ((1.0 - args.metadata) + (1.0 - args.link_quality) + (1.0 - args.freshness) + (1.0 - args.provenance)) / 4.0
    print(f"maintenance_risk_score={score:.6f}")


if __name__ == "__main__":
    main()
