from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Count language-transfer stages in a path such as Greek>Syriac>Arabic>Latin.")
parser.add_argument("--path", type=str, required=True)
args = parser.parse_args()

languages = [item.strip() for item in args.path.replace("→", ">").split(">") if item.strip()]
stages = max(0, len(languages) - 1)
print(f"languages={len(languages)}")
print(f"transfer_stages={stages}")
