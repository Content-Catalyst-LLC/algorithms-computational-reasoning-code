# Data Dictionary

## system_scenarios.csv

- `scenario_id`: synthetic systems-modeling scenario.
- `feedback_strength`: degree to which system outputs influence future inputs.
- `network_dependency`: degree of dependence on connected components or networks.
- `scenario_uncertainty`: uncertainty across modeled futures.
- `resilience`: ability to absorb stress and recover.
- `calibration`: empirical fit or credibility of model behavior.
- `documentation`: quality of boundaries, assumptions, scenarios, and outputs.
- `governance`: readiness of review, decision logging, monitoring, and stop authority.
- `stakes`: consequence level of model use.

## systems_modeling_audit.csv

- `system_vulnerability_score`: average feedback strength, network dependency, scenario uncertainty, and weak resilience.
- `model_readiness_score`: average calibration, documentation, governance, and resilience.
- `system_modeling_risk_score`: stakes multiplied by vulnerability and weak readiness.
- `recommendation`: suggested governance stance.

## systems_modeling_summary.csv

- `scenarios_reviewed`: number of scenarios evaluated.
- `scenarios_for_escalation`: scenarios requiring stress testing and escalation.
- `scenarios_requiring_governance_review`: scenarios requiring governance review.
- `scenarios_not_ready_for_decision_use`: scenarios that should not guide decisions without redesign.
- `mean_system_vulnerability_score`: average vulnerability.
- `mean_model_readiness_score`: average readiness.
- `mean_system_modeling_risk_score`: average systems-modeling risk.
