from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from boundary_reliability.workflow import BoundaryReliabilityCase, reliability_quality, reliability_risk
from calculators.reliability_quality_calculator import compute


def test_reliability_scores_in_range():
    case = BoundaryReliabilityCase("Test", "Context", "Claim", 0.8, 0.8, 0.8, 0.75, 0.75, 0.75, 0.7, 0.75, 0.7, 0.7)
    assert 0 <= reliability_quality(case) <= 100
    assert 0 <= reliability_risk(case) <= 100


def test_calculator_returns_interpretation():
    assert "interpretation" in compute([0.75] * 10)
