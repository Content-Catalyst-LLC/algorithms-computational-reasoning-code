from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from algorithmic_verification.workflow import VerificationCase, verification_quality, verification_risk
from calculators.verification_quality_calculator import compute


def test_verification_scores_in_range():
    case = VerificationCase("Test", "Context", "Claim", 0.8, 0.8, 0.8, 0.75, 0.75, 0.75, 0.7, 0.75, 0.7, 0.7)
    assert 0 <= verification_quality(case) <= 100
    assert 0 <= verification_risk(case) <= 100


def test_calculator_returns_interpretation():
    assert "interpretation" in compute([0.75] * 10)
