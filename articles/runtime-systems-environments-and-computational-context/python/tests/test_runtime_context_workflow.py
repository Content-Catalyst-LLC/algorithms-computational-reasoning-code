from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from runtime_context.examples import minimal_environment_manifest, validate_required_config
from calculators.runtime_quality_calculator import compute as runtime_compute
from calculators.reproducibility_context_calculator import compute as repro_compute

def test_manifest_and_config():
    assert "python_version" in minimal_environment_manifest()
    assert validate_required_config(["PATH"])["valid"] is True

def test_calculators():
    assert runtime_compute([0.75]*10)["runtime_quality"] > 0
    assert repro_compute(1,1,1,1,1,1)["reproducibility_context_score"] == 100
