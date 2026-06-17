.headers on
.mode column

SELECT
  case_name,
  ROUND(100.0 * (
    0.12 * representation_fit +
    0.10 * model_documentation +
    0.10 * vector_compatibility +
    0.10 * similarity_interpretability +
    0.10 * retrieval_evidence +
    0.10 * metadata_provenance +
    0.10 * bias_review +
    0.08 * drift_monitoring +
    0.10 * access_boundary_clarity +
    0.10 * governance_readiness
  ), 2) AS embedding_quality
FROM embedding_system_cases
ORDER BY embedding_quality DESC;

SELECT item_id, model_version, source, dimension_1, dimension_2, dimension_3, dimension_4
FROM synthetic_vectors
ORDER BY item_id;
