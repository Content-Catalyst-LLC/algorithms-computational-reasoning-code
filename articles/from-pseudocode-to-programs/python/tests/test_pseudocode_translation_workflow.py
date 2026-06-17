from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from pseudocode_translation.workflow import TranslationCase, evaluate_cases, translation_quality, translation_risk
from calculators.translation_quality_calculator import compute


def test_translation_scores_in_range():
    case = TranslationCase("Test", "Goal", "Context", 0.8, 0.7, 0.7, 0.7, 0.8, 0.6, 0.6, 0.7, 0.8, 0.7)
    assert 0 <= translation_quality(case) <= 100
    assert 0 <= translation_risk(case) <= 100


def test_evaluate_cases_adds_diagnostic():
    case = TranslationCase("Test", "Goal", "Context", 0.8, 0.7, 0.7, 0.7, 0.8, 0.6, 0.6, 0.7, 0.8, 0.7)
    rows = evaluate_cases([case])
    assert "diagnostic" in rows[0]


def test_calculator_returns_interpretation():
    result = compute(0.8, 0.7, 0.7, 0.7, 0.8, 0.6, 0.6, 0.7, 0.8, 0.7)
    assert "interpretation" in result
