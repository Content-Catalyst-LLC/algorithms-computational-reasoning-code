from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from sequence_structures.workflow import SequenceStructureCase, sequence_structure_quality, sequence_structure_risk
from sequence_structures.examples import demo_sequence_structures, CircularBuffer
from calculators.sequence_structure_quality_calculator import compute


def test_sequence_scores_in_range():
    case = SequenceStructureCase("Test", "Context", "Choice", 0.8, 0.8, 0.8, 0.75, 0.75, 0.75, 0.7, 0.75, 0.7, 0.7)
    assert 0 <= sequence_structure_quality(case) <= 100
    assert 0 <= sequence_structure_risk(case) <= 100


def test_stack_queue_and_buffer_behavior():
    demo = demo_sequence_structures()
    assert demo["stack_order"] != demo["queue_order"]
    assert demo["circular_buffer_values_after_overwrite"] == ["b", "c", "d"]


def test_circular_buffer_capacity():
    buffer = CircularBuffer(2)
    buffer.append("x")
    buffer.append("y")
    buffer.append("z")
    assert buffer.values() == ["y", "z"]


def test_calculator_returns_interpretation():
    assert "interpretation" in compute([0.75] * 10)
