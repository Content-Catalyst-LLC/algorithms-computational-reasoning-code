from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from database_knowledge.workflow import schema_quality, governance_risk

def test_schema_quality():
    result = schema_quality(1,1,1,1,1)
    assert result["schema_quality_score"] == 100.0

def test_governance_risk():
    result = governance_risk(1,1,1,1,1)
    assert result["database_governance_risk"] == 0.0
