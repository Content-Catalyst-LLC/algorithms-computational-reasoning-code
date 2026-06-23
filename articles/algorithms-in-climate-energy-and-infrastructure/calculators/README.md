# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `infrastructure_risk_calculator.py` — hazard × exposure × vulnerability.
- `grid_balance_calculator.py` — supply/storage/imports minus demand/exports/losses.
- `maintenance_priority_calculator.py` — weighted condition, criticality, consequence, and equity priority.
- `avoided_loss_calculator.py` — expected loss without intervention minus expected loss with intervention.
- `governance_readiness_calculator.py` — average equity, validation, monitoring, governance, and maintenance readiness.
- `resilience_risk_calculator.py` — average impact, weak equity, weak validation, and weak governance.

## R calculators

- `infrastructure_algorithm_score.R` — compute impact, governance, and resilience risk indicators.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
