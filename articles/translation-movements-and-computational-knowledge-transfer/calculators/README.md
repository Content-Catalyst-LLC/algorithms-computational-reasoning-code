# Calculators

These small calculators support article concepts without external packages. They are educational conceptual scaffolds, not philological or manuscript-analysis tools.

## Python calculators

- `procedural_fidelity_calculator.py` — average step, example, diagram, table, and context preservation.
- `vocabulary_mapping_calculator.py` — score technical-term mapping coverage.
- `table_error_rate_calculator.py` — calculate mismatched values over total checked values.
- `relay_depth_calculator.py` — count language-transfer stages.
- `knowledge_object_completeness_calculator.py` — score whether terms, steps, examples, diagrams, tables, and context are present.
- `transfer_score_calculator.py` — average transfer-dimension scores.
- `origin_story_risk_calculator.py` — flag oversimplified origin-story patterns in a phrase.

## R calculators

- `transfer_score.R` — compute computational knowledge transfer score.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
