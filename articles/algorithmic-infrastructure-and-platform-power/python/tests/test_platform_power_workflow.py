from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from platform_power.workflow import dependency_score, switching_cost, api_dependency_ratio, visibility_share

def test_dependency_score():
    assert dependency_score(.80,.90,.70,.85,.65) == 78.9

def test_switching_cost():
    assert switching_cost(45000,120000,18000,24000,75000) == 282000

def test_api_dependency_ratio():
    assert api_dependency_ratio(850000,1000000) == 0.85

def test_visibility_share():
    assert visibility_share(250000,5000000) == 0.05
