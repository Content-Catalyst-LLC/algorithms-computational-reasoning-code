# Calculators

These small calculators support article concepts without external packages. They are educational conceptual scaffolds, not formal proof tools.

## Python calculators

- `formal_score_calculator.py` — average Church formal-computation dimensions.
- `beta_reduction_calculator.py` — reduce simple identity/constant patterns.
- `alpha_conversion_calculator.py` — safely rename a simple bound variable.
- `church_numeral_calculator.py` — build a Church numeral string and apply repeated function notation.
- `normal_form_helper.py` — classify simple terms as reducible or already normal.
- `capture_risk_calculator.py` — flag simple variable-capture risks.
- `decidability_scope_helper.py` — classify example problem families.
- `ai_formal_reasoning_caution_calculator.py` — flag AI/formal-reasoning overclaims.

## R calculators

- `church_formal_score.R` — compute formal-computation score.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
