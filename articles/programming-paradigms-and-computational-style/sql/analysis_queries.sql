.headers on
.mode column

SELECT
  case_name,
  ROUND(100.0 * (
    0.12 * style_clarity +
    0.10 * state_visibility +
    0.10 * abstraction_fit +
    0.10 * composability +
    0.10 * testability +
    0.10 * error_handling +
    0.10 * traceability +
    0.08 * performance_fit +
    0.10 * team_readability +
    0.10 * governance_readiness
  ), 2) AS style_quality
FROM programming_style_cases
ORDER BY style_quality DESC;

SELECT paradigm, central_unit, reasoning_emphasis, example_language_or_context
FROM paradigm_taxonomy
ORDER BY paradigm;
