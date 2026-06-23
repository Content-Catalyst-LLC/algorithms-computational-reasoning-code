from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Produce a simple BNF-style production.")
parser.add_argument("--nonterminal", type=str, default="expression")
parser.add_argument("--alternatives", type=str, default="term | expression + term | expression - term")
args = parser.parse_args()

print(f"<{args.nonterminal}> ::= {args.alternatives}")
