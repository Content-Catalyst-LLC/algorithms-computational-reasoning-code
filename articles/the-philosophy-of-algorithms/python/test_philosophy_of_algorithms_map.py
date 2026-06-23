from __future__ import annotations
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import philosophy_of_algorithms_map as philo

def test_high_priority_domains_include_automated_decision_and_agents() -> None:
    config = philo.AlgorithmicPhilosophyConfig()
    scored = [philo.score_domain(row, config) for row in philo.philosophical_domains()]
    high = {row["domain_id"] for row in scored if row["review_status"] == "high_priority_philosophical_review"}
    assert "automated_decision_systems" in high
    assert "agentic_tool_use" in high

def test_cautions_include_formalization_and_ai() -> None:
    cautions = {row["caution"] for row in philo.philosophical_cautions()}
    assert "do_not_confuse_formalization_with_reality" in cautions
    assert "do_not_confuse_ai_output_with_accountable_reasoning" in cautions

def test_delegation_risk_bounds() -> None:
    assert philo.delegation_risk(0.0, 1.0, 1.0) == 0.0
    assert philo.delegation_risk(1.0, 1.0, 1.0) == 1.0
    assert 0.0 < philo.delegation_risk(0.7, 0.6, 0.5) < 1.0

def main() -> None:
    test_high_priority_domains_include_automated_decision_and_agents()
    test_cautions_include_formalization_and_ai()
    test_delegation_risk_bounds()
    print("All philosophy of algorithms tests passed.")

if __name__ == "__main__":
    main()
