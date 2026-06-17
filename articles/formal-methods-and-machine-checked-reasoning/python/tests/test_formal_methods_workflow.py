from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from formal_methods.workflow import FormalMethodsCase, formal_methods_quality, verification_overclaim_risk
from formal_methods.proof_obligation_examples import verified_sort_demo
from calculators.formal_methods_quality_calculator import compute


def test_formal_methods_scores_in_range():
    case = FormalMethodsCase("Test", "Context", "Claim", 0.8, 0.8, 0.8, 0.75, 0.75, 0.75, 0.7, 0.75, 0.7, 0.7)
    assert 0 <= formal_methods_quality(case) <= 100
    assert 0 <= verification_overclaim_risk(case) <= 100


def test_verified_sort_demo_obligations_hold():
    demo = verified_sort_demo([3, 1, 2])
    assert demo["sortedness_obligation"] is True
    assert demo["permutation_obligation"] is True


def test_calculator_returns_interpretation():
    assert "interpretation" in compute([0.75] * 10)
