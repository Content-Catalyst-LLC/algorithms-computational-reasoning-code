from __future__ import annotations

import csv
from pathlib import Path

manifest = Path("shared/metadata/articles.csv")
articles_dir = Path("articles")

if not manifest.exists():
    raise SystemExit("Missing shared/metadata/articles.csv")

rows = list(csv.DictReader(manifest.open(encoding="utf-8")))
missing = []
for row in rows:
    slug = row["slug"]
    path = articles_dir / slug / "README.md"
    if not path.exists():
        missing.append(slug)

if missing:
    raise SystemExit("Missing article README files: " + ", ".join(missing[:20]))

print(f"Validated {len(rows)} planned articles.")
