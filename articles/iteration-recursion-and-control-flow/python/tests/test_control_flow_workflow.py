from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from control_flow.examples import bounded_retry_outcomes, iterative_sum, nondecreasing, recursive_factorial
from calculators.control_flow_quality_calculator import compute as quality_compute
from calculators.recursion_depth_risk_calculator import compute as recursion_compute

def test_control_flow_examples():
    assert iterative_sum([1,2,3]) == 6
    assert recursive_factorial(5) == 120
    assert nondecreasing([1,2,2,3]) is True
    assert nondecreasing([1,3,2]) is False
    assert bounded_retry_outcomes(5,3)[-1].endswith("success")
    assert bounded_retry_outcomes(2,None)[-1] == "exhausted"

def test_calculators():
    assert quality_compute([0.75]*10)["control_flow_quality"] > 0
    assert recursion_compute(250,1000,1,1,0,100)["recursion_depth_risk_score"] >= 0
