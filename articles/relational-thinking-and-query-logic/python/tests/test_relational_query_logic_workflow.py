from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from relational_query_logic.workflow import query_logic_calculator, join_risk_calculator, relational_set_examples

def test_query_logic_calculator():
    result = query_logic_calculator(1,1,1,1,1,1)
    assert result["query_logic_core_score"] == 100.0

def test_join_risk_calculator():
    result = join_risk_calculator(1,1,1,1,1)
    assert result["join_risk"] == 0.0

def test_set_examples():
    rows = relational_set_examples()
    assert any(row["operation"] == "anti_join_missing_references" for row in rows)
