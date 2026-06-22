# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `expected_value_calculator.py` — probability-weighted benefit minus action cost.
- `expected_loss_calculator.py` — probability-weighted loss if no action.
- `threshold_action_calculator.py` — classify whether a score crosses an action threshold.
- `decision_readiness_calculator.py` — average calibration, uncertainty communication, human review, contestability, and governance.
- `multi_criteria_score_calculator.py` — weighted multi-criteria decision score.

## R calculators

- `decision_score.R` — compute expected value, expected loss, readiness, and threshold action.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
