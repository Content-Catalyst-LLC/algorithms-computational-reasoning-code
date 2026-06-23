# Data Dictionary

## infrastructure_systems.csv

- `system_id`: synthetic climate, energy, or infrastructure algorithmic system.
- `public_impact`: consequence level for public services, communities, or public investment.
- `climate_exposure`: degree to which hazards, climate change, or environmental stress affect the system.
- `reliability_impact`: consequence level for service reliability, safety, operations, or essential infrastructure.
- `equity_readiness`: readiness of environmental justice, service equity, community impact, and distributional review.
- `validation_readiness`: readiness of validation, stress testing, sensitivity analysis, and physical plausibility review.
- `monitoring_readiness`: readiness of sensor coverage, data quality, drift monitoring, and incident learning.
- `governance_readiness`: readiness of ownership, documentation, review authority, audit trails, and stop rules.
- `maintenance_readiness`: readiness of lifecycle maintenance, asset review, recalibration, and model aging controls.

## infrastructure_algorithm_risk_audit.csv

- `impact_score`: average public impact, climate exposure, and reliability impact.
- `governance_score`: average equity readiness, validation readiness, monitoring readiness, governance readiness, and maintenance readiness.
- `resilience_risk_score`: average impact score, weak equity readiness, weak validation readiness, and weak governance score.
- `recommendation`: suggested governance stance.

## infrastructure_algorithm_summary.csv

- `systems_reviewed`: number of synthetic systems reviewed.
- `systems_requiring_governance_redesign`: systems requiring governance redesign before public use.
- `systems_requiring_public_value_review`: systems requiring public-value and equity review.
- `systems_requiring_reliability_review`: systems requiring reliability and safety review.
- `systems_requiring_climate_equity_review`: systems requiring climate-equity review.
