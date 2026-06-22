# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `proxy_validity_gap_calculator.py` — compute 1 minus proxy validity.
- `measurement_risk_calculator.py` — combine validity gap, missingness, differential error, and label error.
- `misclassification_rates_calculator.py` — compute sensitivity and specificity from counts.

## R calculators

- `attenuation_factor.R` — compute a simple attenuation factor from measurement-error variance.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
