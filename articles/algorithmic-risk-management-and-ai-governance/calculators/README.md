# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `inherent_risk_calculator.py` — severity × likelihood × weak detectability.
- `governance_readiness_calculator.py` — average ownership, documentation, monitoring, contestability, remediation, and stop authority.
- `residual_risk_calculator.py` — inherent risk after control effectiveness.
- `control_effectiveness_calculator.py` — average prevention, detection, mitigation, and response controls.

## R calculators

- `risk_governance_score.R` — compute inherent risk, governance readiness, and residual risk.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
