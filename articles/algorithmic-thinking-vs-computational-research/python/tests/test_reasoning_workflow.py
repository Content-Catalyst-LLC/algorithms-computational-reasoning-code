from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from algorithmic_vs_computational_reasoning.workflow import (
    ReasoningProfile,
    evaluate_profiles,
    score_algorithmic_thinking,
    score_computational_reasoning,
)
from calculators.reasoning_gap_calculator import compute


def test_scores_are_in_range():
    profile = ReasoningProfile("Test", 0.8, 0.7, 0.7, 0.8, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6)
    assert 0 <= score_algorithmic_thinking(profile) <= 100
    assert 0 <= score_computational_reasoning(profile) <= 100


def test_evaluate_profiles_adds_gap():
    profile = ReasoningProfile("Test", 0.8, 0.7, 0.7, 0.8, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6)
    rows = evaluate_profiles([profile])
    assert "reasoning_gap" in rows[0]
    assert "diagnostic" in rows[0]


def test_calculator_returns_interpretation():
    result = compute(0.8, 0.7, 0.7, 0.8, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6)
    assert "interpretation" in result
