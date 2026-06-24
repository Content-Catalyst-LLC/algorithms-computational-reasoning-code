from __future__ import annotations
import argparse

parser = argparse.ArgumentParser(description="Estimate caution required when interpreting simplified neural models.")
parser.add_argument("--simplification", type=float, required=True)
parser.add_argument("--biological-complexity", type=float, required=True)
parser.add_argument("--anthropomorphic-language", type=float, required=True)
parser.add_argument("--scope-statement", type=float, required=True, help="Higher means stronger scope statement; reduces risk.")
args = parser.parse_args()
risk = (args.simplification + args.biological_complexity + args.anthropomorphic_language + (1.0 - args.scope_statement)) / 4.0
print(f"biological_caution_score={risk:.6f}")
