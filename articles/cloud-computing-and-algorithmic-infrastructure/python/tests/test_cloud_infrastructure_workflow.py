from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from cloud_infrastructure.workflow import total_latency, nominal_capacity, unit_cost, redundant_availability

def test_total_latency():
    assert total_latency(80,45,60,25,15) == 225

def test_nominal_capacity():
    assert nominal_capacity(12,250) == 3000

def test_unit_cost():
    assert unit_cost(120,35,25,90,18,144000) == 0.002

def test_redundant_availability():
    assert redundant_availability([0.99,0.985]) == 0.99985
