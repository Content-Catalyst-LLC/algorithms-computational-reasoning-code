from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Rename a simple bound variable in λx. body.")
parser.add_argument("--body", type=str, default="x")
parser.add_argument("--old", type=str, default="x")
parser.add_argument("--new", type=str, default="y")
args = parser.parse_args()

if args.new in args.body.replace(args.old, ""):
    print("warning=possible_capture_or_name_collision")
renamed = args.body.replace(args.old, args.new)
print(f"before=λ{args.old}. {args.body}")
print(f"after=λ{args.new}. {renamed}")
print("rule=alpha_conversion_when_binding_structure_is_preserved")
