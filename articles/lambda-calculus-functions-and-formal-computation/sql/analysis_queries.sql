.headers on
.mode column

SELECT
  case_name,
  ROUND(100.0 * (
    0.10 * expression_clarity +
    0.12 * binding_safety +
    0.12 * substitution_discipline +
    0.10 * reduction_traceability +
    0.10 * evaluation_strategy_clarity +
    0.08 * recursion_awareness +
    0.12 * type_discipline_clarity +
    0.08 * proof_connection +
    0.08 * implementation_relevance +
    0.10 * governance_readiness
  ), 2) AS lambda_reasoning_quality
FROM lambda_expression_cases
ORDER BY lambda_reasoning_quality DESC;
