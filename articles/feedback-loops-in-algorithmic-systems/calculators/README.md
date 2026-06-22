# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `feedback_risk_calculator.py` — combine amplification, concentration, intervention influence, drift, and recursive data.
- `drift_trigger_calculator.py` — flag whether distribution shift exceeds a threshold.
- `amplification_factor_calculator.py` — classify feedback as dampening, stable, or amplifying.

## R calculators

- `feedback_pressure_score.R` — combine amplification and exposure concentration.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
