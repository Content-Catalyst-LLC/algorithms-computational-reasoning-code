# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `audit_completeness_calculator.py` — compute available required records divided by required records.
- `accountability_capacity_calculator.py` — average documentation, provenance, reviewability, contestability, remediation, and governance.
- `reconstruction_risk_calculator.py` — compute stakes multiplied by weak audit completeness.
- `incident_recurrence_calculator.py` — compute repeated incidents divided by total incidents.

## R calculators

- `accountability_score.R` — compute audit completeness, accountability capacity, and reconstruction risk.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
