from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from reliability.examples import nondecreasing, round_trip, score_in_range
from calculators.reliability_quality_calculator import compute as reliability_compute
from calculators.test_coverage_risk_calculator import compute as coverage_compute

def test_basic_properties():
    assert score_in_range(50) is True
    assert score_in_range(150) is False
    assert nondecreasing([1,2,2,3]) is True
    assert nondecreasing([1,3,2]) is False
    assert round_trip("test") is True

def test_calculators():
    assert reliability_compute([0.75]*10)["reliability_quality"] > 0
    assert coverage_compute(40,30,4,5,3,5)["test_coverage_risk_score"] >= 0
