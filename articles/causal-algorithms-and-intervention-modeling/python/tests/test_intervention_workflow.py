from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "python" / "intervention_modeling_workflow.py"
spec = importlib.util.spec_from_file_location("intervention_modeling_workflow", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
assert spec.loader is not None
spec.loader.exec_module(module)


def test_case_generation_and_effects() -> None:
    config = module.InterventionConfig(seed=123, n=30)
    cases = module.generate_cases(config)
    scenarios = module.default_scenarios()
    scenario_rows = module.build_scenario_rows(cases, scenarios, config)
    estimates = module.estimate_effects(scenario_rows)
    assert len(cases) == 30
    assert len(scenario_rows) == 30 * len(scenarios)
    assert len(estimates) == len(scenarios)
    assert all("mean_estimated_effect" in row for row in estimates)
    assert any(float(row["mean_estimated_effect"]) > 0 for row in estimates)


def test_feasibility_review_contains_status() -> None:
    config = module.InterventionConfig(seed=456, n=40)
    cases = module.generate_cases(config)
    scenario_rows = module.build_scenario_rows(cases, module.default_scenarios(), config)
    estimates = module.estimate_effects(scenario_rows)
    review = module.feasibility_review(estimates)
    assert len(review) == len(estimates)
    assert all(row["feasibility_status"] for row in review)


if __name__ == "__main__":
    test_case_generation_and_effects()
    test_feasibility_review_contains_status()
    print("intervention workflow tests passed")
