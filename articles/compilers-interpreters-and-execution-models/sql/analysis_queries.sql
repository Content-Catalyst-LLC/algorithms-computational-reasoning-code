.headers on
.mode column

SELECT
  case_name,
  ROUND(100.0 * (
    0.10 * translation_clarity +
    0.10 * semantic_checking +
    0.10 * optimization_traceability +
    0.10 * runtime_visibility +
    0.10 * diagnostics_quality +
    0.10 * portability +
    0.12 * reproducibility +
    0.12 * security_boundaries +
    0.08 * performance_fit +
    0.08 * governance_readiness
  ), 2) AS execution_quality
FROM execution_model_cases
ORDER BY execution_quality DESC;

SELECT stage, representation, purpose, example
FROM compiler_pipeline_taxonomy
ORDER BY rowid;
