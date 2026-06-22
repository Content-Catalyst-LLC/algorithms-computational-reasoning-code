# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `documentation_completeness_calculator.py` — completed required fields divided by total required fields.
- `documentation_quality_calculator.py` — average accuracy, completeness, specificity, timeliness, accessibility, and actionability.
- `documentation_risk_calculator.py` — stakes multiplied by weak documentation quality.
- `freshness_calculator.py` — freshness based on days since update and required review interval.

## R calculators

- `documentation_score.R` — compute documentation completeness, quality, artifact coverage, and documentation risk.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
