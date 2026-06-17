from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from halting_boundary.workflow import HaltingBoundaryCase, halting_boundary_quality, automation_overclaim_risk
from calculators.halting_boundary_calculator import compute


def test_halting_scores_in_range():
    case = HaltingBoundaryCase("Test", "Context", "Claim", 0.8, 0.8, 0.8, 0.75, 0.75, 0.75, 0.7, 0.75, 0.7, 0.7)
    assert 0 <= halting_boundary_quality(case) <= 100
    assert 0 <= automation_overclaim_risk(case) <= 100


def test_calculator_returns_interpretation():
    assert "interpretation" in compute([0.75] * 10)
