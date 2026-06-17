from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from type_systems.workflow import TypeRepresentationCase, type_quality, type_risk
from type_systems.examples import ArticleRecord, validate_article_record, demo_type_validation
from calculators.type_quality_calculator import compute as type_compute
from calculators.boundary_validation_calculator import compute as boundary_compute


def test_type_scores_in_range():
    case = TypeRepresentationCase("Test", "Context", "Choice", 0.8, 0.8, 0.75, 0.85, 0.8, 0.75, 0.8, 0.8, 0.75, 0.8)
    assert 0 <= type_quality(case) <= 100
    assert 0 <= type_risk(case) <= 100


def test_article_record_validation():
    good = ArticleRecord("Title", "good-slug", "Series", "published", "https://github.com/example/repo")
    bad = ArticleRecord("", "Bad Slug", "", "done", "ftp://example.org")
    assert validate_article_record(good) == []
    assert len(validate_article_record(bad)) >= 4


def test_demo_and_calculators():
    assert demo_type_validation()["valid"] is True
    assert "interpretation" in type_compute([0.75] * 10)
    assert boundary_compute(8, 7, 6, 7)["boundary_validation_score"] > 0
