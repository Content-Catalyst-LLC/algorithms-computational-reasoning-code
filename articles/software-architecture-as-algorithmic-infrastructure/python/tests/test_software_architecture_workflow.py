from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from software_architecture.examples import dependency_density, failure_reachability
from calculators.architecture_quality_calculator import compute as architecture_compute
from calculators.dependency_risk_calculator import compute as dependency_compute

def test_graph_helpers():
    edges=[("api","domain"),("domain","interfaces"),("worker","domain")]
    assert dependency_density(edges) > 0
    assert "interfaces" in failure_reachability(edges, "api")

def test_calculators():
    assert architecture_compute([0.75]*10)["architecture_quality"] > 0
    assert dependency_compute(10,14,2,3,1)["dependency_risk_score"] >= 0
