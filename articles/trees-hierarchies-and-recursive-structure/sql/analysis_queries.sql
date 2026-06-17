.headers on
.mode column

SELECT
  case_name,
  ROUND(100.0 * (
    0.12 * hierarchy_fit +
    0.12 * recursive_clarity +
    0.10 * invariant_documentation +
    0.10 * traversal_support +
    0.08 * balance_awareness +
    0.10 * path_interpretability +
    0.10 * relationship_loss_control +
    0.08 * complexity_awareness +
    0.10 * representation_risk_documentation +
    0.10 * governance_readiness
  ), 2) AS tree_structure_quality
FROM tree_structure_cases
ORDER BY tree_structure_quality DESC;
