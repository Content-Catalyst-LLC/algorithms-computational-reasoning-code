DROP TABLE IF EXISTS computability_boundary_cases;

CREATE TABLE computability_boundary_cases (
  case_name TEXT PRIMARY KEY,
  computational_context TEXT NOT NULL,
  procedural_claim TEXT NOT NULL,
  procedure_definition REAL NOT NULL,
  input_domain_clarity REAL NOT NULL,
  decision_status_clarity REAL NOT NULL,
  termination_guarantee REAL NOT NULL,
  recognizability_status REAL NOT NULL,
  reduction_awareness REAL NOT NULL,
  approximation_honesty REAL NOT NULL,
  automation_scope_clarity REAL NOT NULL,
  traceability REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

INSERT INTO computability_boundary_cases VALUES
('Static analyzer','Tool checks code for selected classes of errors','The analyzer detects specified patterns but does not decide all program behavior',0.84,0.82,0.78,0.82,0.72,0.66,0.80,0.84,0.78,0.74),
('General program verifier','Verification tool attempts to prove properties of arbitrary programs','Verification is sound for specified properties and restricted models not universal for all behavior',0.78,0.74,0.70,0.62,0.68,0.78,0.74,0.72,0.76,0.76),
('AI reasoning assistant','Generative system supports reasoning code review explanation and search','The system assists reasoning but does not provide a universal decision procedure',0.66,0.62,0.58,0.64,0.56,0.50,0.68,0.62,0.58,0.72),
('Institutional rule engine','Rule system assigns cases to categories under documented policies','Rules decide in-scope cases and route ambiguous or out-of-domain cases for review',0.82,0.78,0.76,0.80,0.70,0.54,0.76,0.82,0.84,0.86);
