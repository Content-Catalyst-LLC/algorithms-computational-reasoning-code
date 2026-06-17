.headers on
.mode column

SELECT
  case_name,
  ROUND(100.0 * (
    0.12 * metadata_completeness +
    0.10 * source_clarity +
    0.12 * lineage_coverage +
    0.10 * version_control +
    0.08 * timestamp_quality +
    0.10 * schema_clarity +
    0.10 * integrity_checks +
    0.10 * access_governance +
    0.10 * reproducibility_support +
    0.08 * stewardship_readiness
  ), 2) AS traceability_quality
FROM traceability_cases
ORDER BY traceability_quality DESC;

SELECT from_id, relation, to_id, actor, timestamp
FROM provenance_edges
ORDER BY timestamp;
