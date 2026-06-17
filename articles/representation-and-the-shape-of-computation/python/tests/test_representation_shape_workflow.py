from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from representation_shape.workflow import RepresentationCase, representation_quality, representation_risk
from representation_shape.examples import demo_shapes
from calculators.representation_quality_calculator import compute


def test_representation_scores_in_range():
    case = RepresentationCase("Test", "Context", "Choice", 0.8, 0.8, 0.8, 0.75, 0.75, 0.75, 0.7, 0.75, 0.7, 0.7)
    assert 0 <= representation_quality(case) <= 100
    assert 0 <= representation_risk(case) <= 100


def test_shape_demo_differs_between_stack_and_queue():
    demo = demo_shapes()
    assert demo["stack_order"] != demo["queue_order"]


def test_calculator_returns_interpretation():
    assert "interpretation" in compute([0.75] * 10)
