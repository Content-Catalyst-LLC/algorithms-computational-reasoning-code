# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `harm_risk_calculator.py` — compute error likelihood × severity × exposure × weak contestability.
- `responsibility_capacity_calculator.py` — average ownership, monitoring, appeals, repair, and governance.
- `remediation_gap_calculator.py` — compare severity with repair capacity.
- `harm_escalation_trigger.py` — flag high-harm, low-responsibility escalation.

## R calculators

- `harm_responsibility_score.R` — compute harm risk and responsibility capacity.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
