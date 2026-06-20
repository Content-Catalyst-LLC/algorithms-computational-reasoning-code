-- Example query: identify weakest governance dimensions.
SELECT
  case_name,
  MIN(variable_clarity, objective_documentation, constraint_documentation, data_provenance,
      feasibility_logic, sensitivity_review, robustness_review, fairness_review,
      traceability, governance_review, communication_clarity) AS weakest_score
FROM optimization_cases
ORDER BY weakest_score ASC;
