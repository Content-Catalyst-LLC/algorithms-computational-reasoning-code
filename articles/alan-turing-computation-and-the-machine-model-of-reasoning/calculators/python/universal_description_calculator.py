from __future__ import annotations

import argparse
import json

parser = argparse.ArgumentParser(description="Represent a toy machine description as data.")
parser.add_argument("--name", type=str, default="unary_increment")
args = parser.parse_args()

description = {
    "machine": args.name,
    "alphabet": ["1", "_"],
    "states": ["scan", "write", "halt"],
    "start_state": "scan",
    "blank": "_",
    "description_note": "A machine description can be stored as symbolic data and interpreted by another machine."
}
print(json.dumps(description, indent=2, sort_keys=True))
