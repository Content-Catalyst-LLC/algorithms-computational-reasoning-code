DROP TABLE IF EXISTS tractability_cases;
CREATE TABLE tractability_cases (
  case_name TEXT PRIMARY KEY, problem_context TEXT, problem_form TEXT, expected_difficulty TEXT,
  input_definition_clarity REAL, complexity_evidence REAL, structure_exploitation REAL,
  exact_method_feasibility REAL, approximation_readiness REAL, heuristic_validation REAL,
  benchmark_evidence REAL, timeout_handling REAL, governance_readiness REAL, communication_clarity REAL
);
.import --csv data/synthetic_tractability_cases.csv tractability_cases
