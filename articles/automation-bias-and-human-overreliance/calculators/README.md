# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `overreliance_gap_calculator.py` — compute acceptance minus model quality when positive.
- `trust_calibration_calculator.py` — compute absolute gap between reliance and model quality.
- `oversight_risk_calculator.py` — combine reliance, uncertainty, review-time deficit, override friction, and contestability.

## R calculators

- `reliance_quality_gap.R` — compute trust-calibration and overreliance gaps.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
