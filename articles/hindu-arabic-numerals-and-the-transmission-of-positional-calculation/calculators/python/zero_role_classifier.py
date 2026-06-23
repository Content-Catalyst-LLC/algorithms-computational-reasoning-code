from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Classify zero's procedural role.")
parser.add_argument("--context", type=str, choices=["placeholder", "arithmetic", "boundary"], required=True)
args = parser.parse_args()

roles = {
    "placeholder": "zero marks an empty position and preserves place-value structure",
    "arithmetic": "zero acts as a number in operations such as addition and multiplication",
    "boundary": "zero creates special constraints, especially division by zero",
}
print(f"zero_role={roles[args.context]}")
