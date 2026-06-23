# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `expected_loss_calculator.py` — expected loss from probability of default, loss given default, and exposure at default.
- `portfolio_return_calculator.py` — weighted portfolio return.
- `portfolio_variance_calculator.py` — simple two-asset portfolio variance.
- `value_at_risk_calculator.py` — normal approximation VaR.
- `stress_loss_calculator.py` — scenario loss from exposure and shock.
- `governance_readiness_calculator.py` — average transparency, human review, validation, monitoring, and governance.
- `financial_algorithm_risk_calculator.py` — average model risk, impact, and weak governance readiness.

## R calculators

- `financial_algorithm_score.R` — compute impact, governance readiness, and financial algorithm risk.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
