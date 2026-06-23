from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Walk through a simplified compiler pipeline.")
parser.add_argument("--source", type=str, default="ADD PAYROLL-TOTAL TO TAX-BASE")
args = parser.parse_args()

tokens = args.source.replace(".", " ").split()
pipeline = [
    ("source", args.source),
    ("tokens", tokens),
    ("syntax_tree", "statement(operation=ADD, operands=...)"),
    ("checked_program", "types-and-names-checked"),
    ("target_code", "machine-specific instruction sequence"),
]
for stage, value in pipeline:
    print(f"{stage}={value}")
