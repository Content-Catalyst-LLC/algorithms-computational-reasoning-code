from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from algorithmic_literacy.workflow import LiteracyCase, evaluate_cases, literacy_gap_score, literacy_support_score
from calculators.literacy_support_calculator import compute


def test_literacy_scores_in_range():
    case = LiteracyCase("Test", "System", "Users", 0.7, 0.6, 0.7, 0.5, 0.6, 0.7, 0.8, 0.7)
    assert 0 <= literacy_support_score(case) <= 100
    assert 0 <= literacy_gap_score(case) <= 100


def test_evaluate_cases_adds_diagnostic():
    case = LiteracyCase("Test", "System", "Users", 0.7, 0.6, 0.7, 0.5, 0.6, 0.7, 0.8, 0.7)
    rows = evaluate_cases([case])
    assert "diagnostic" in rows[0]


def test_calculator_returns_interpretation():
    result = compute(0.7, 0.6, 0.7, 0.5, 0.6, 0.7, 0.8, 0.7)
    assert "interpretation" in result
