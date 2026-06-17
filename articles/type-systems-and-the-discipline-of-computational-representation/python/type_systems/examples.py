from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import re


SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


@dataclass(frozen=True)
class ArticleRecord:
    title: str
    slug: str
    series: str
    status: str
    repository_url: str


@dataclass(frozen=True)
class TypeConcept:
    type_concept: str
    category: str
    definition: str
    example: str


def validate_article_record(record: ArticleRecord) -> list[str]:
    errors: list[str] = []
    if not record.title.strip():
        errors.append("title must be non-empty")
    if not SLUG_RE.match(record.slug):
        errors.append("slug must use lowercase letters, numbers, and hyphens")
    if record.status not in {"draft", "review", "published", "archived"}:
        errors.append("status must be one of draft, review, published, archived")
    if not record.repository_url.startswith("https://github.com/"):
        errors.append("repository_url must point to GitHub")
    if not record.series.strip():
        errors.append("series must be non-empty")
    return errors


def load_type_taxonomy(article_root: Path) -> list[TypeConcept]:
    path = article_root / "data" / "synthetic_type_taxonomy.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        return [
            TypeConcept(
                row["type_concept"],
                row["category"],
                row["definition"],
                row["example"],
            )
            for row in csv.DictReader(handle)
        ]


def demo_type_validation(article_root: Path | None = None) -> dict[str, object]:
    record = ArticleRecord(
        title="Type Systems and the Discipline of Computational Representation",
        slug="type-systems-and-the-discipline-of-computational-representation",
        series="Algorithms & Computational Reasoning",
        status="published",
        repository_url="https://github.com/Content-Catalyst-LLC/algorithms-computational-reasoning-code/tree/main/articles/type-systems-and-the-discipline-of-computational-representation/",
    )
    errors = validate_article_record(record)
    payload: dict[str, object] = {
        "record": asdict(record),
        "valid": len(errors) == 0,
        "errors": errors,
        "interpretation": "Runtime validation complements static type discipline by checking domain-specific constraints at system boundaries.",
    }
    if article_root is not None and (article_root / "data" / "synthetic_type_taxonomy.csv").exists():
        payload["taxonomy_count"] = len(load_type_taxonomy(article_root))
    return payload
