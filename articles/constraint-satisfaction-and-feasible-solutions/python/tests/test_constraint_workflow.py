from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'python'))
from constraint_satisfaction.workflow import feasible_assignments, assignment_feasible, violation_count

def test_feasible_assignment_count():
    constraints=[{'kind':'not_equal','left':'A','right':'B'},{'kind':'not_equal','left':'B','right':'C'}]
    assert len(feasible_assignments(['A','B','C'],['red','blue'],constraints)) == 2

def test_candidate_feasible():
    constraints=[{'kind':'not_equal','left':'A','right':'B'}]
    assert assignment_feasible({'A':'red','B':'blue'},constraints)

def test_candidate_violation_count():
    constraints=[{'kind':'not_equal','left':'A','right':'B'}]
    assert violation_count({'A':'red','B':'red'},constraints) == 1
