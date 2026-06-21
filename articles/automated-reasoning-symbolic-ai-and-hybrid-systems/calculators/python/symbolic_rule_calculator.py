from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Check whether a symbolic rule fires.")
    parser.add_argument("--facts", required=True, help="Comma-separated known facts")
    parser.add_argument("--premises", required=True, help="Comma-separated required premises")
    parser.add_argument("--conclusion", required=True, help="Conclusion if rule fires")
    args = parser.parse_args()

    facts = {item.strip() for item in args.facts.split(",") if item.strip()}
    premises = {item.strip() for item in args.premises.split(",") if item.strip()}
    fires = premises.issubset(facts)

    print(f"facts={sorted(facts)}")
    print(f"premises={sorted(premises)}")
    print(f"fires={int(fires)}")
    print(f"conclusion={args.conclusion if fires else 'not_derived'}")


if __name__ == "__main__":
    main()
