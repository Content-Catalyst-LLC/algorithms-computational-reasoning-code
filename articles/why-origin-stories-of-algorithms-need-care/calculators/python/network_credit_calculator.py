from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Score inclusion of transmission actors.")
for name in ["translators", "scribes", "teachers", "users", "institutions", "tools"]:
    parser.add_argument(f"--has-{name}", choices=["true", "false"], required=True)
args = parser.parse_args()

values = [
    args.has_translators == "true",
    args.has_scribes == "true",
    args.has_teachers == "true",
    args.has_users == "true",
    args.has_institutions == "true",
    args.has_tools == "true",
]
score = sum(values) / len(values)
print(f"network_credit_score={score:.6f}")
