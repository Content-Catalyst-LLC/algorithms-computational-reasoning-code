from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from state_mutation.examples import aliasing_demo, demo_state_machine, transition
from calculators.state_quality_calculator import compute as state_compute
from calculators.mutation_risk_calculator import compute as mutation_compute

def test_state_machine():
    assert transition("draft","review")[0]=="review"
    assert transition("published","draft")[0]=="published"
    assert demo_state_machine()["final_state"]=="archived"

def test_aliasing_and_calculators():
    d=aliasing_demo()
    assert d["original"]==d["alias"]
    assert d["copied"]!=d["original"]
    assert state_compute([0.75]*10)["state_quality"] > 0
    assert mutation_compute(10,8,6,5,7,6)["mutation_risk_score"] >= 0
