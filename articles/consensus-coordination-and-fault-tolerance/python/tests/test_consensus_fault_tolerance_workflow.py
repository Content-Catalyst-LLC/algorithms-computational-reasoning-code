from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from consensus_fault_tolerance.workflow import majority_quorum, crash_fault_tolerance, byzantine_replica_requirement, quorum_intersection_holds
def test_majority_quorum(): assert majority_quorum(5) == 3
def test_crash_fault_tolerance(): assert crash_fault_tolerance(5) == 2
def test_byzantine_replica_requirement(): assert byzantine_replica_requirement(2) == 7
def test_quorum_intersection(): assert quorum_intersection_holds(5,3) is True
