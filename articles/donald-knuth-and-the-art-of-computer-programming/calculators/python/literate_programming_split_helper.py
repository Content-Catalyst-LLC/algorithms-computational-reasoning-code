from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Sketch weave/tangle split for a literate source.")
parser.add_argument("--module", type=str, default="sorting_algorithm")
args = parser.parse_args()

print(f"literate_source={args.module}.w")
print(f"weave_output={args.module}.pdf_or_html")
print(f"tangle_output={args.module}.source_code")
print("principle=one source supports human explanation and machine execution")
