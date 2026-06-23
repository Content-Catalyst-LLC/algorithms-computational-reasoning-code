# Data Dictionary

## financial_systems.csv

- `system_id`: synthetic financial algorithmic system.
- `market_impact`: consequence level for markets, execution, liquidity, volatility, or market confidence.
- `consumer_impact`: consequence level for consumers, borrowers, account holders, or retail users.
- `model_risk`: exposure to incorrect assumptions, implementation errors, drift, misuse, or poor validation.
- `transparency`: clarity of purpose, variables, thresholds, explanations, and documentation.
- `human_review`: meaningful review, override, escalation, and challenge capacity.
- `validation`: conceptual soundness, implementation testing, backtesting, and sensitivity review.
- `monitoring`: post-deployment monitoring of errors, drift, losses, customer harm, market impact, and incidents.
- `governance`: model inventory, ownership, approval, change management, audit trails, and stop authority.
- `liquidity_risk`: risk that positions, payments, or funding cannot be exited or met under stress.

## financial_algorithm_risk_audit.csv

- `impact_score`: average market impact, consumer impact, and liquidity risk.
- `governance_readiness_score`: average transparency, human review, validation, monitoring, and governance.
- `financial_algorithm_risk_score`: average model risk, impact score, and weak governance readiness.
- `recommendation`: suggested governance stance.

## financial_algorithm_summary.csv

- `systems_reviewed`: number of synthetic financial algorithm systems.
- `systems_requiring_control_redesign`: systems requiring control redesign before scaling.
- `systems_requiring_consumer_protection_review`: systems requiring consumer protection review.
- `systems_requiring_market_stability_review`: systems requiring market stability review.
- `systems_requiring_model_governance_review`: systems requiring model governance review.
