from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from optimization_audit.workflow import linear_objective, constraint_margin, penalty_objective, normalized_tradeoff_score

def test_linear_objective():
    assert linear_objective([4.0,2.0,1.5],[10.0,20.0,5.0]) == 87.5

def test_constraint_margin():
    assert constraint_margin(100.0,86.5) == 13.5

def test_penalty_objective():
    assert penalty_objective(42.0,8.0,2.5) == 62.0

def test_normalized_tradeoff_score():
    assert normalized_tradeoff_score(0.30,0.82,0.25) == 0.7605
