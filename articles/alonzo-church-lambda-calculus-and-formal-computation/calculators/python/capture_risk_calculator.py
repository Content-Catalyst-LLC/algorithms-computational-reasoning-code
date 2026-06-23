from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag simple variable-capture risks during substitution.")
parser.add_argument("--substitute-variable", type=str, required=True)
parser.add_argument("--argument-free-vars", type=str, required=True, help="Comma-separated free variables in argument")
parser.add_argument("--body-binders", type=str, required=True, help="Comma-separated binders in target body")
args = parser.parse_args()

free_vars = {x.strip() for x in args.argument_free_vars.split(",") if x.strip()}
binders = {x.strip() for x in args.body_binders.split(",") if x.strip()}
risk = bool(free_vars & binders)
print(f"capture_risk={str(risk).lower()}")
print("conflicting_names=" + ",".join(sorted(free_vars & binders)))
