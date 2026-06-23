from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Classify simple lambda terms as obviously reducible or already normal.")
parser.add_argument("--term", type=str, required=True)
args = parser.parse_args()

term = args.term.strip()
reducible_markers = ["(λ", "lambda", "\\lambda"]
is_reducible = any(marker in term for marker in reducible_markers) and ")" in term and " " in term
print(f"obviously_reducible={str(is_reducible).lower()}")
print("note=this helper is a teaching heuristic, not a full lambda-calculus parser")
