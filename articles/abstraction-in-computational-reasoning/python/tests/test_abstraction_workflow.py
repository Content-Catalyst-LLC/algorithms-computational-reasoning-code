from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from abstraction_audit.workflow import (
    AbstractionCase,
    abstraction_risk,
    abstraction_score,
    evaluate_cases,
)
from calculators.abstraction_score_calculator import compute


def test_abstraction_score_in_range():
    case = AbstractionCase("Test", "System", "Representation", 0.8, 0.7, 0.6, 0.7, 0.7, 0.7, 0.6, 0.6, 0.7, 0.7)
    assert 0 <= abstraction_score(case) <= 100
    assert 0 <= abstraction_risk(case) <= 100


def test_evaluate_cases_adds_diagnostic():
    case = AbstractionCase("Test", "System", "Representation", 0.8, 0.7, 0.6, 0.7, 0.7, 0.7, 0.6, 0.6, 0.7, 0.7)
    rows = evaluate_cases([case])
    assert "diagnostic" in rows[0]


def test_calculator_returns_interpretation():
    result = compute(0.8, 0.7, 0.6, 0.7, 0.7, 0.7, 0.6, 0.6, 0.7, 0.7)
    assert "interpretation" in result
