# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `selection_gap_calculator.py` — compute max minus min selection-rate gap.
- `error_rate_calculator.py` — compute false-positive, false-negative, and true-positive rates.
- `calibration_gap_calculator.py` — compute absolute score/outcome calibration gap.
- `justice_capacity_calculator.py` — average fairness evidence, measurement validity, contestability, and remediation.

## R calculators

- `fairness_justice_score.R` — compute selection-rate, error-rate, calibration, and justice-capacity indicators.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
