from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from distributed_networks.workflow import quorum_size, crash_fault_tolerance, availability_with_replication, distributed_latency

def test_quorum_size():
    assert quorum_size(5) == 3

def test_crash_fault_tolerance():
    assert crash_fault_tolerance(5) == 2

def test_availability_with_replication():
    assert availability_with_replication(3, .99) == 0.999999

def test_distributed_latency():
    assert distributed_latency(35,80,20) == 135
