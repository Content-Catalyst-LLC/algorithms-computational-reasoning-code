DROP TABLE IF EXISTS p_np_cases;
CREATE TABLE p_np_cases (
  case_name TEXT PRIMARY KEY, problem_context TEXT, claimed_class TEXT,
  problem_form_clarity REAL, input_definition_clarity REAL, certificate_clarity REAL,
  verifier_clarity REAL, reduction_evidence REAL, class_claim_evidence REAL,
  exact_method_feasibility REAL, approximation_readiness REAL, benchmark_support REAL,
  governance_readiness REAL, communication_clarity REAL
);
.import --csv data/synthetic_p_np_hardness_cases.csv p_np_cases
