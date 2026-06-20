DROP TABLE IF EXISTS optimization_cases;
CREATE TABLE optimization_cases (
  case_name TEXT PRIMARY KEY,
  decision_context TEXT NOT NULL,
  optimization_goal TEXT NOT NULL,
  variable_clarity REAL NOT NULL,
  objective_documentation REAL NOT NULL,
  constraint_documentation REAL NOT NULL,
  data_provenance REAL NOT NULL,
  feasibility_logic REAL NOT NULL,
  sensitivity_review REAL NOT NULL,
  robustness_review REAL NOT NULL,
  fairness_review REAL NOT NULL,
  traceability REAL NOT NULL,
  governance_review REAL NOT NULL,
  communication_clarity REAL NOT NULL
);
