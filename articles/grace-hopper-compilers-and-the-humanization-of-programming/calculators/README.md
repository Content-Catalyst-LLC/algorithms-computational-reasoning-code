# Calculators

These small calculators support article concepts without external packages. They are educational conceptual scaffolds, not compiler validation or code-safety tools.

## Python calculators

- `humanization_score_calculator.py` — average Hopper compiler-humanization dimensions.
- `compiler_pipeline_helper.py` — walk through a simplified compiler pipeline.
- `portability_score_calculator.py` — estimate source portability across target systems.
- `diagnostic_quality_calculator.py` — estimate diagnostic helpfulness.
- `standards_conformance_helper.py` — classify standard/conformance coverage.
- `maintenance_burden_calculator.py` — estimate readability and documentation burden.
- `ai_code_generation_caution_calculator.py` — flag AI code-generation overclaims.
- `translation_trust_calculator.py` — combine specification, tests, diagnostics, and review.

## R calculators

- `humanization_score.R` — compute compiler-humanization score.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
