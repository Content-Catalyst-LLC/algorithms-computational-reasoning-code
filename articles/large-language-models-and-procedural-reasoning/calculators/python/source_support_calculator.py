from __future__ import annotations
import argparse


def parse_sources(value: str) -> set[str]:
    if not value:
        return set()
    return {part.strip().replace("source:", "") for part in value.split(";") if part.strip()}


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute source support coverage.")
    parser.add_argument("--expected", default="")
    parser.add_argument("--found", default="")
    parser.add_argument("--requires-sources", action="store_true")
    args = parser.parse_args()
    expected = parse_sources(args.expected)
    found = parse_sources(args.found)
    missing = sorted(expected - found)
    if not args.requires_sources:
        score = 1.0
    else:
        score = 1.0 if expected and not missing else 0.0
    print(f"expected={';'.join(sorted(expected))}")
    print(f"found={';'.join(sorted(found))}")
    print(f"missing={';'.join(missing)}")
    print(f"source_score={score:.6f}")


if __name__ == "__main__":
    main()
