# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `mastery_probability_calculator.py` — simple mastery probability from evidence and prior.
- `alert_threshold_calculator.py` — classify support action from risk score and threshold.
- `recommendation_score_calculator.py` — weighted score from relevance, readiness, interest, and support need.
- `learning_gain_calculator.py` — posttest minus pretest.
- `governance_readiness_calculator.py` — average equity, privacy, pedagogical validity, human review, accessibility, monitoring, and governance.
- `learning_system_risk_calculator.py` — average impact, weak equity, weak pedagogy, and weak governance.

## R calculators

- `learning_system_score.R` — compute learning-system indicators.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
