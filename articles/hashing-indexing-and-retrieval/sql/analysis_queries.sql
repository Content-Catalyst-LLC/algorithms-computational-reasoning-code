.headers on
.mode column

SELECT
  case_name,
  ROUND(100.0 * (
    0.12 * key_clarity +
    0.08 * hash_suitability +
    0.10 * collision_handling +
    0.12 * index_coverage +
    0.10 * retrieval_speed_fit +
    0.10 * freshness_control +
    0.10 * ranking_transparency +
    0.10 * metadata_provenance +
    0.08 * security_boundary_clarity +
    0.10 * governance_readiness
  ), 2) AS retrieval_quality
FROM hashing_retrieval_cases
ORDER BY retrieval_quality DESC;

SELECT term, GROUP_CONCAT(doc_id, ',') AS documents
FROM inverted_index_terms
GROUP BY term
ORDER BY term;
