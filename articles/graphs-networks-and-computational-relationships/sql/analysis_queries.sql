.headers on
.mode column

SELECT
  case_name,
  ROUND(100.0 * (
    0.12 * edge_meaning_clarity +
    0.10 * node_definition_clarity +
    0.10 * direction_clarity +
    0.08 * weight_interpretability +
    0.10 * path_validity +
    0.10 * connectivity_evidence +
    0.10 * metadata_provenance +
    0.10 * algorithm_fit +
    0.10 * representation_risk_documentation +
    0.10 * governance_readiness
  ), 2) AS graph_reasoning_quality
FROM graph_relationship_cases
ORDER BY graph_reasoning_quality DESC;

SELECT source, target, relationship, weight FROM graph_edges ORDER BY source, target;
