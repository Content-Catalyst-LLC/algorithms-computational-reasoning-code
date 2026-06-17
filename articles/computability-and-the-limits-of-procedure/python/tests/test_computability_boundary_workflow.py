from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from computability_boundary.workflow import ComputabilityBoundaryCase, computability_boundary_quality, procedural_overclaim_risk
from calculators.computability_boundary_calculator import compute


def test_computability_scores_in_range():
    case = ComputabilityBoundaryCase("Test", "Context", "Claim", 0.8, 0.8, 0.8, 0.75, 0.75, 0.75, 0.7, 0.75, 0.7, 0.7)
    assert 0 <= computability_boundary_quality(case) <= 100
    assert 0 <= procedural_overclaim_risk(case) <= 100


def test_calculator_returns_interpretation():
    assert "interpretation" in compute([0.75] * 10)
