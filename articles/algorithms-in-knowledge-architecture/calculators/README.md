# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `metadata_completeness_calculator.py` — required fields present divided by required fields.
- `architecture_readiness_calculator.py` — average metadata, taxonomy, search, link, recommendation, provenance, and editorial review readiness.
- `maintenance_risk_calculator.py` — average weak metadata, weak links, weak freshness, and weak provenance.
- `weighted_relevance_calculator.py` — weighted text, semantic, authority, and freshness relevance.
- `cosine_similarity_calculator.py` — vector similarity.
- `link_recommendation_calculator.py` — semantic, prerequisite, and graph value link score.

## R calculators

- `knowledge_architecture_score.R` — compute readiness, maintenance risk, and governance readiness.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
