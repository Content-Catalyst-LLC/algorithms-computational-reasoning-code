.headers on
.mode column

SELECT
  case_name,
  ROUND(100.0 * (
    0.12 * representation_clarity +
    0.12 * constraint_strength +
    0.10 * missingness_handling +
    0.10 * boundary_validation +
    0.10 * domain_fidelity +
    0.10 * error_specificity +
    0.10 * type_coverage +
    0.08 * interoperability +
    0.10 * testability +
    0.08 * governance_readiness
  ), 2) AS type_quality
FROM type_representation_cases
ORDER BY type_quality DESC;

SELECT type_concept, category, definition, example
FROM type_taxonomy
ORDER BY type_concept;
