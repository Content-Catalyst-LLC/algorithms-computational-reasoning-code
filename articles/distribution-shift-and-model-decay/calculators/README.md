# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `performance_decay_calculator.py` — compute baseline minus current performance.
- `drift_trigger_calculator.py` — flag drift review triggers.
- `calibration_gap_calculator.py` — compute confidence-outcome calibration gap.

## R calculators

- `decay_risk_score.R` — combine drift, decay, calibration, subgroup gap, and override rate.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
