from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from data_structures.workflow import DataStructureCase, structure_reasoning_quality, structure_mismatch_risk
from data_structures.examples import demo_structures
from calculators.data_structure_quality_calculator import compute


def test_structure_scores_in_range():
    case = DataStructureCase("Test", "Context", "Choice", 0.8, 0.8, 0.8, 0.75, 0.75, 0.75, 0.7, 0.75, 0.7, 0.7)
    assert 0 <= structure_reasoning_quality(case) <= 100
    assert 0 <= structure_mismatch_risk(case) <= 100


def test_stack_queue_priority_differ():
    demo = demo_structures()
    assert demo["stack_order"] != demo["queue_order"]
    assert demo["priority_order"][0] == "urgent"


def test_calculator_returns_interpretation():
    assert "interpretation" in compute([0.75] * 10)
