from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from p_np_hardness.workflow import verify_sat_assignment, verify_graph_coloring

def test_certificate_verifiers():
    assert verify_sat_assignment([[1,-2],[2,3]], {1: True, 2: False, 3: True}) is True
    assert verify_graph_coloring([(1,2),(2,3)], {1: 1, 2: 2, 3: 1}) is True
