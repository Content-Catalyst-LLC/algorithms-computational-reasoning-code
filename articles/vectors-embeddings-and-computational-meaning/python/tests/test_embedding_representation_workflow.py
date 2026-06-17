from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from embedding_representation.workflow import EmbeddingSystemCase, embedding_quality, meaning_overclaim_risk
from embedding_representation.examples import cosine_similarity, euclidean_distance, nearest_neighbors, demo_embedding_space
from calculators.embedding_quality_calculator import compute


def test_embedding_scores_in_range():
    case = EmbeddingSystemCase("Test", "Context", "Choice", 0.8, 0.8, 0.8, 0.75, 0.75, 0.75, 0.8, 0.75, 0.8, 0.8)
    assert 0 <= embedding_quality(case) <= 100
    assert 0 <= meaning_overclaim_risk(case) <= 100


def test_similarity_metrics():
    assert round(cosine_similarity([1, 0], [1, 0]), 4) == 1.0
    assert round(cosine_similarity([1, 0], [0, 1]), 4) == 0.0
    assert round(euclidean_distance([0, 0], [3, 4]), 4) == 5.0


def test_nearest_neighbors_and_demo():
    rows = nearest_neighbors([1, 0], {"a": [1, 0], "b": [0, 1]})
    assert rows[0]["item_id"] == "a"
    assert "nearest_neighbors" in demo_embedding_space()


def test_calculator_returns_interpretation():
    assert "interpretation" in compute([0.75] * 10)
