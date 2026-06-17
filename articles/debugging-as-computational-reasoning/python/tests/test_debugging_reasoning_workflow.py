from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from debugging_reasoning.workflow import DebugCase, debugging_quality, evaluate_cases, recurrence_risk
from calculators.debugging_quality_calculator import compute


def test_debugging_scores_in_range():
    case = DebugCase("Test", "System", "Failure", "Expected", "Observed", 0.8, 0.8, 0.7, 0.7, 0.7, 0.7, 0.8, 0.7, 0.6, 0.6)
    assert 0 <= debugging_quality(case) <= 100
    assert 0 <= recurrence_risk(case) <= 100


def test_evaluate_cases_adds_diagnostic():
    case = DebugCase("Test", "System", "Failure", "Expected", "Observed", 0.8, 0.8, 0.7, 0.7, 0.7, 0.7, 0.8, 0.7, 0.6, 0.6)
    rows = evaluate_cases([case])
    assert "diagnostic" in rows[0]


def test_calculator_returns_interpretation():
    result = compute(0.8, 0.8, 0.7, 0.7, 0.7, 0.7, 0.8, 0.7, 0.6, 0.6)
    assert "interpretation" in result
