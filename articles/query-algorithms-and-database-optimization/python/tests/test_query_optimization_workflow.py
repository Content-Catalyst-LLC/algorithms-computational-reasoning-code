from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'python'))
from query_optimization.workflow import estimate_selection_rows, estimate_join_rows, index_tradeoff, plan_governance_score

def test_selection_estimate(): assert estimate_selection_rows(1000,.10)['estimated_rows']==100.0
def test_join_estimate(): assert estimate_join_rows(100,100,10,10)['estimated_join_rows']==1000.0
def test_index_tradeoff(): assert index_tradeoff(82,14,9,6)['net_index_value']==53
def test_plan_governance(): assert plan_governance_score(1,1,1,1,1)['plan_governance_score']==100.0
