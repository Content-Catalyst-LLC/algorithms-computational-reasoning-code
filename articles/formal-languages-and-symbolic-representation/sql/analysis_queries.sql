.headers on
.mode column

SELECT
  case_name,
  ROUND(100.0 * (
    0.10 * alphabet_clarity +
    0.12 * grammar_explicitness +
    0.12 * syntax_validation +
    0.12 * semantic_clarity +
    0.10 * parser_readiness +
    0.10 * schema_support +
    0.10 * error_reporting +
    0.08 * testability +
    0.08 * interoperability +
    0.08 * governance_readiness
  ), 2) AS representation_quality
FROM formal_language_cases
ORDER BY representation_quality DESC;
