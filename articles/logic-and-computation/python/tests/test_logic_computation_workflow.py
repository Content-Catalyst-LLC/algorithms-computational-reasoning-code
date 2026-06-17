from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from logic_computation.workflow import LogicCase, evaluate_cases, logic_quality, logic_risk
from calculators.logic_quality_calculator import compute


def test_logic_scores_in_range():
    case = LogicCase("Test", "System", "Rules", 0.8, 0.8, 0.75, 0.7, 0.75, 0.75, 0.75, 0.65, 0.7, 0.7)
    assert 0 <= logic_quality(case) <= 100
    assert 0 <= logic_risk(case) <= 100


def test_evaluate_cases_adds_diagnostic():
    case = LogicCase("Test", "System", "Rules", 0.8, 0.8, 0.75, 0.7, 0.75, 0.75, 0.75, 0.65, 0.7, 0.7)
    rows = evaluate_cases([case])
    assert "diagnostic" in rows[0]


def test_calculator_returns_interpretation():
    result = compute(0.8, 0.8, 0.75, 0.7, 0.75, 0.75, 0.75, 0.65, 0.7, 0.7)
    assert "interpretation" in result
