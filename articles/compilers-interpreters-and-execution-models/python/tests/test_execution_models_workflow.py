from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from execution_models.workflow import ExecutionModelCase, execution_quality, execution_risk
from execution_models.examples import Add, Multiply, Number, evaluate_expression, tokenize_expression, demo_interpreter
from calculators.execution_quality_calculator import compute as execution_compute
from calculators.build_reproducibility_calculator import compute as build_compute

def test_execution_scores_in_range():
    case = ExecutionModelCase("Test", "Context", "Choice", 0.8, 0.8, 0.75, 0.75, 0.8, 0.7, 0.8, 0.85, 0.8, 0.75)
    assert 0 <= execution_quality(case) <= 100
    assert 0 <= execution_risk(case) <= 100

def test_tiny_interpreter():
    tree = Add(Number(2), Multiply(Number(3), Number(4)))
    assert evaluate_expression(tree) == 14
    assert tokenize_expression("2 + 3 * 4") == ["2", "+", "3", "*", "4"]
    assert demo_interpreter()["result"] == 14

def test_calculators():
    assert "interpretation" in execution_compute([0.75] * 10)
    assert build_compute(1, 1, 1, 1, 1)["build_reproducibility_score"] == 100.0
