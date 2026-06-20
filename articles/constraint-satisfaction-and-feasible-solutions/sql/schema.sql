DROP TABLE IF EXISTS constraint_cases;
CREATE TABLE constraint_cases (
  case_name TEXT PRIMARY KEY,
  variable_clarity REAL,
  domain_clarity REAL,
  constraint_documentation REAL,
  feasibility_logic REAL,
  inconsistency_handling REAL,
  pruning_transparency REAL,
  propagation_transparency REAL,
  traceability REAL,
  exception_handling REAL,
  governance_review REAL,
  fairness_review REAL,
  communication_clarity REAL
);

INSERT INTO constraint_cases VALUES
('Course scheduling',0.86,0.84,0.88,0.84,0.78,0.74,0.70,0.80,0.72,0.76,0.66,0.78),
('Worker shift assignment',0.84,0.82,0.86,0.82,0.80,0.76,0.72,0.82,0.78,0.82,0.84,0.78),
('Product configuration',0.80,0.78,0.82,0.84,0.74,0.70,0.78,0.76,0.66,0.72,0.54,0.72),
('Opaque eligibility rules',0.42,0.36,0.24,0.40,0.28,0.20,0.18,0.24,0.22,0.26,0.28,0.34);
