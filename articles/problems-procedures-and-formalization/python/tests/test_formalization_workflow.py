from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from formalization_audit.workflow import (
    FormalizationCase,
    evaluate_cases,
    formalization_risk,
    formalization_score,
)
from calculators.formalization_score_calculator import compute


def test_formalization_score_in_range():
    case = FormalizationCase("Test", "Concern", "Task", 0.8, 0.8, 0.7, 0.7, 0.7, 0.6, 0.6, 0.7, 0.7, 0.6)
    assert 0 <= formalization_score(case) <= 100
    assert 0 <= formalization_risk(case) <= 100


def test_evaluate_cases_adds_diagnostic():
    case = FormalizationCase("Test", "Concern", "Task", 0.8, 0.8, 0.7, 0.7, 0.7, 0.6, 0.6, 0.7, 0.7, 0.6)
    rows = evaluate_cases([case])
    assert "diagnostic" in rows[0]


def test_calculator_returns_interpretation():
    result = compute(0.8, 0.8, 0.7, 0.7, 0.7, 0.6, 0.6, 0.7, 0.7, 0.6)
    assert "interpretation" in result
