from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from api_interfaces.examples import compatibility_check, validate_record
from calculators.interface_quality_calculator import compute as interface_compute
from calculators.compatibility_risk_calculator import compute as compatibility_compute

def test_validator_and_compatibility():
    assert validate_record({"case_id":"x","status":"review","score":1.0})["valid"] is True
    assert validate_record({"case_id":"x","score":"bad"})["valid"] is False
    assert compatibility_check({"a","b"},{"a","b","c"})["compatible"] is True
    assert compatibility_check({"a","b"},{"a"})["compatible"] is False

def test_calculators():
    assert interface_compute([0.75]*10)["interface_quality"] > 0
    assert compatibility_compute(0,0,0,1,1,1)["compatibility_risk_score"] >= 0
