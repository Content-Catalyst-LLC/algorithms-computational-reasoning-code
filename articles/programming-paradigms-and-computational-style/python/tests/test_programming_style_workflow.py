from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from programming_style.workflow import ParadigmStyleCase, style_quality, style_risk
from programming_style.examples import procedural_average, functional_average, demo_styles
from calculators.style_quality_calculator import compute as style_compute
from calculators.state_visibility_calculator import compute as state_compute


def test_style_scores_in_range():
    case = ParadigmStyleCase("Test", "Context", "Choice", 0.8, 0.75, 0.8, 0.8, 0.75, 0.8, 0.75, 0.7, 0.8, 0.8)
    assert 0 <= style_quality(case) <= 100
    assert 0 <= style_risk(case) <= 100


def test_style_examples():
    values = [1.0, 2.0, 3.0]
    assert procedural_average(values) == 2.0
    assert functional_average(values) == 2.0
    assert "functional_average" in demo_styles()


def test_calculators():
    assert "interpretation" in style_compute([0.75] * 10)
    assert state_compute(8, 6, 5, 4)["state_visibility_score"] > 0
