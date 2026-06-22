# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `stock_flow_calculator.py` — next stock equals current stock plus inflow minus outflow.
- `feedback_update_calculator.py` — simple feedback update.
- `system_vulnerability_calculator.py` — average feedback strength, network dependency, scenario uncertainty, and weak resilience.
- `model_readiness_calculator.py` — average calibration, documentation, governance, and resilience.
- `sensitivity_calculator.py` — proportional output response to proportional parameter change.
- `resilience_calculator.py` — simple recovery-based resilience score.

## R calculators

- `systems_model_score.R` — compute vulnerability, readiness, and risk indicators.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
