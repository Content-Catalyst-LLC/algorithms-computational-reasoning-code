.headers on
.mode column

SELECT case_name,
ROUND(100.0 * (0.11*graph_definition + 0.11*node_edge_clarity + 0.10*weight_documentation + 0.10*constraint_documentation + 0.10*traversal_traceability + 0.09*alternative_path_reporting + 0.09*failure_handling + 0.08*update_freshness + 0.08*distributional_review + 0.09*governance_review + 0.05*communication_clarity),2) AS graph_search_score
FROM graph_search_cases
ORDER BY graph_search_score DESC;

SELECT source, target, weight, risk_score
FROM graph_edges
ORDER BY weight ASC;

SELECT COUNT(DISTINCT node) AS node_count
FROM (
  SELECT source AS node FROM graph_edges
  UNION
  SELECT target AS node FROM graph_edges
);
