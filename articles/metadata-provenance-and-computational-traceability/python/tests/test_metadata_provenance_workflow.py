from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from metadata_provenance.workflow import TraceabilityCase, traceability_quality, traceability_risk
from metadata_provenance.examples import checksum, provenance_demo, find_upstream
from calculators.traceability_quality_calculator import compute as trace_compute
from calculators.metadata_completeness_calculator import compute as metadata_compute


def test_traceability_scores_in_range():
    case = TraceabilityCase("Test", "Context", "Choice", 0.8, 0.8, 0.75, 0.8, 0.8, 0.75, 0.75, 0.8, 0.7, 0.75)
    assert 0 <= traceability_quality(case) <= 100
    assert 0 <= traceability_risk(case) <= 100


def test_checksum_and_provenance_demo():
    assert len(checksum("metadata")) == 64
    demo = provenance_demo()
    assert "trace_checksum" in demo
    assert len(demo["edges"]) >= 1


def test_upstream_lookup_and_calculators():
    edges = [{"from_id": "output", "to_id": "input", "relation": "was_derived_from"}]
    assert find_upstream("output", edges) == ["input"]
    assert "interpretation" in trace_compute([0.75] * 10)
    assert metadata_compute(["title", "creator"])["present_field_count"] == 2
