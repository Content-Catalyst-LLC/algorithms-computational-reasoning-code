from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Reduce a tiny set of teaching lambda-calculus patterns.")
parser.add_argument("--pattern", choices=["identity", "constant_first", "apply_twice"], required=True)
parser.add_argument("--argument", type=str, default="y")
args = parser.parse_args()

if args.pattern == "identity":
    before = f"(λx. x) {args.argument}"
    after = args.argument
elif args.pattern == "constant_first":
    before = f"((λx. λy. x) {args.argument}) z"
    after = args.argument
else:
    before = f"(λf. λx. f (f x)) F {args.argument}"
    after = f"F (F {args.argument})"

print(f"before={before}")
print(f"after={after}")
print("rule=beta_reduction_by_substitution")
