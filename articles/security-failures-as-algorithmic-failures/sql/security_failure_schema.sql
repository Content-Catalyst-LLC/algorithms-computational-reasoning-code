-- security_failure_schema.sql
-- Minimal SQL schema for algorithmic security failure review.

CREATE TABLE IF NOT EXISTS security_failure_cases (
  case_id INTEGER PRIMARY KEY,
  case_name TEXT NOT NULL,
  system_context TEXT NOT NULL,
  failure_pattern TEXT NOT NULL,
  assumption_quality REAL NOT NULL,
  threat_model_coverage REAL NOT NULL,
  input_boundary_control REAL NOT NULL,
  authorization_control REAL NOT NULL,
  logging_traceability REAL NOT NULL,
  monitoring_detection REAL NOT NULL,
  governance_ownership REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS control_gaps (
  control_id INTEGER PRIMARY KEY,
  control_name TEXT NOT NULL,
  coverage REAL NOT NULL,
  importance REAL NOT NULL,
  detectability REAL NOT NULL,
  priority TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS assumption_stress_tests (
  test_id INTEGER PRIMARY KEY,
  assumption TEXT NOT NULL,
  stress_condition TEXT NOT NULL,
  expected_control TEXT NOT NULL,
  result TEXT NOT NULL
);
