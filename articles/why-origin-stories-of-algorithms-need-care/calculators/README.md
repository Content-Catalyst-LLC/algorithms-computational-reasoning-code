# Calculators

These small calculators support article concepts without external packages. They are educational conceptual scaffolds, not historical proof tools.

## Python calculators

- `origin_care_score_calculator.py` — average origin-story care dimensions.
- `layer_confusion_calculator.py` — flag confusion among word, concept, practice, institution, and modern formalization.
- `etymology_risk_calculator.py` — flag etymology-as-invention phrases.
- `anachronism_risk_calculator.py` — flag modern computing projected backward.
- `network_credit_calculator.py` — score inclusion of translators, scribes, teachers, users, institutions, and tools.
- `evidence_scope_calculator.py` — score whether claims include evidence and scope.
- `origin_story_rewrite_helper.py` — return safer phrasing for common risky claims.

## R calculators

- `origin_care_score.R` — compute origin-story care score.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
