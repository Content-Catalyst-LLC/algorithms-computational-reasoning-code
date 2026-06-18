from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from performance_systems.workflow import response_time, throughput, utilization, little_law, amdahl_speedup

def test_response_time():
    assert response_time(45,20,85,35,15) == 200

def test_throughput():
    assert throughput(12000,60) == 200

def test_utilization():
    assert utilization(180,200) == 0.9

def test_little_law():
    assert little_law(180,0.45) == 81

def test_amdahl_speedup():
    assert amdahl_speedup(1,0.12) == 1
