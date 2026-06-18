from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from pipelines_workflows.workflow import freshness_score, validation_pass_rate, pipeline_quality_calculator, topological_order

def test_freshness_score():
    assert freshness_score(0) == 1.0

def test_validation_pass_rate():
    assert validation_pass_rate(18,20) == 0.9

def test_pipeline_quality_calculator():
    assert pipeline_quality_calculator(1,1,1,1,1)["pipeline_quality_score"] == 100.0

def test_topological_order():
    tasks=[{"task_id":"a","depends_on":""},{"task_id":"b","depends_on":"a"}]
    assert topological_order(tasks) == ["a","b"]
