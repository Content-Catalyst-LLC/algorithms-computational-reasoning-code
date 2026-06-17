from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from automated_reasoning.workflow import AutomatedReasoningCase, automated_reasoning_quality, inference_overclaim_risk
from calculators.automated_reasoning_quality_calculator import compute


def test_automated_reasoning_scores_in_range():
    case = AutomatedReasoningCase("Test", "Context", "Claim", 0.8, 0.8, 0.8, 0.75, 0.75, 0.75, 0.7, 0.75, 0.7, 0.7)
    assert 0 <= automated_reasoning_quality(case) <= 100
    assert 0 <= inference_overclaim_risk(case) <= 100


def test_calculator_returns_interpretation():
    assert "interpretation" in compute([0.75] * 10)
