# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `sensitivity_calculator.py` — sensitivity from true positives and false negatives.
- `specificity_calculator.py` — specificity from true negatives and false positives.
- `risk_threshold_calculator.py` — classify action from risk score and threshold.
- `sir_population_calculator.py` — simple population accounting for susceptible, infected, and recovered states.
- `governance_readiness_calculator.py` — average clinical validation, equity readiness, privacy readiness, human review, workflow integration, monitoring, and governance.
- `health_algorithm_risk_calculator.py` — health algorithm risk from impact, validation weakness, equity weakness, and governance weakness.

## R calculators

- `health_algorithm_score.R` — compute impact, governance readiness, and health algorithm risk.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
