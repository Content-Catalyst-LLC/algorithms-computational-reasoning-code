from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from algorithms_reasoning.diagnostics import AlgorithmScenario, evaluate_scenario, summarize
from calculators.complexity_calculator import estimate


def test_evaluate_scenario_returns_records():
    scenario = AlgorithmScenario(
        "Test", 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.2, 0.8, 0.8
    )
    records = evaluate_scenario(scenario, max_power=5)
    assert len(records) == 2
    assert records[-1]["input_size"] == 32


def test_summarize_has_diagnostic():
    scenario = AlgorithmScenario(
        "Test", 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.2, 0.8, 0.8
    )
    summary = summarize(evaluate_scenario(scenario, max_power=5))
    assert "diagnostic" in summary[0]


def test_complexity_calculator():
    result = estimate(16)
    assert result["linear"] == 16
    assert result["quadratic"] == 256
