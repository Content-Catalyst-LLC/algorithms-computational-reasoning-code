# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `permission_gate_calculator.py` — check whether a proposed tool action should pass, escalate, or be blocked.
- `autonomy_level_calculator.py` — recommend autonomy level from blocked/escalated action counts.

## R calculators

- `agent_risk_score.R` — combine action risk and observation quality into a simple review score.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
