from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="List loop proof obligations.")
parser.add_argument("--loop-name", type=str, default="loop")
args = parser.parse_args()

obligations = [
    "initialization: invariant holds before loop",
    "preservation: body preserves invariant when guard is true",
    "progress: variant decreases or moves toward termination",
    "exit: invariant and false guard imply postcondition",
]
for item in obligations:
    print(f"{args.loop_name}:{item}")
