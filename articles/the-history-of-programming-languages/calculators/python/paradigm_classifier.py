from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Roughly classify a language description into historical paradigm tags.")
parser.add_argument("--description", type=str, required=True)
args = parser.parse_args()

text = args.description.lower()
tags = []
rules = {
    "functional": ["function", "lambda", "immutable", "pure", "haskell", "ml", "lisp"],
    "logic": ["logic", "facts", "rules", "prolog", "inference"],
    "object_oriented": ["object", "class", "method", "message", "smalltalk", "java"],
    "systems": ["memory", "pointer", "kernel", "systems", "c", "rust"],
    "database": ["sql", "query", "table", "relation", "database"],
    "scientific": ["fortran", "array", "numerical", "scientific", "simulation"],
    "scripting_web": ["script", "web", "javascript", "python", "php", "ruby"],
}
for tag, keywords in rules.items():
    if any(keyword in text for keyword in keywords):
        tags.append(tag)
print("paradigm_tags=" + ",".join(tags if tags else ["unclassified"]))
