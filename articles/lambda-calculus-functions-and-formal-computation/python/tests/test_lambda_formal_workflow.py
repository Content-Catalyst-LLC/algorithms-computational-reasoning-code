from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from lambda_formal.workflow import LambdaExpressionCase, lambda_reasoning_quality, formalization_risk
from lambda_formal.reducer import demo_identity_reduction
from calculators.lambda_reasoning_quality_calculator import compute


def test_lambda_scores_in_range():
    case = LambdaExpressionCase("Test", "Context", "Claim", 0.8, 0.8, 0.8, 0.75, 0.75, 0.75, 0.7, 0.75, 0.7, 0.7)
    assert 0 <= lambda_reasoning_quality(case) <= 100
    assert 0 <= formalization_risk(case) <= 100


def test_identity_reduction_demo():
    trace = demo_identity_reduction()
    assert trace[-1] == "a"


def test_calculator_returns_interpretation():
    assert "interpretation" in compute([0.75] * 10)
