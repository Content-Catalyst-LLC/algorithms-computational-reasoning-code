DROP TABLE IF EXISTS sequence_structure_cases;

CREATE TABLE sequence_structure_cases (
  case_name TEXT PRIMARY KEY,
  problem_context TEXT NOT NULL,
  structure_choice TEXT NOT NULL,
  operation_fit REAL NOT NULL,
  order_semantics REAL NOT NULL,
  invariant_clarity REAL NOT NULL,
  complexity_awareness REAL NOT NULL,
  memory_behavior REAL NOT NULL,
  overflow_handling REAL NOT NULL,
  interpretability REAL NOT NULL,
  traversal_support REAL NOT NULL,
  representation_risk_documentation REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

INSERT INTO sequence_structure_cases VALUES
('Numerical time series array','A simulation stores observations at fixed time indexes','Array indexed by time step with metadata for units and time origin',0.90,0.86,0.82,0.86,0.88,0.72,0.84,0.90,0.78,0.80),
('Undo action stack','A user interface supports reversible editing actions','Stack of action records with inverse operations and provenance',0.88,0.92,0.86,0.82,0.76,0.78,0.86,0.72,0.82,0.84),
('Case review queue','Institutional cases wait for review in arrival order','FIFO queue with timestamp status escalation and audit metadata',0.88,0.90,0.84,0.78,0.76,0.82,0.88,0.78,0.88,0.90),
('Streaming circular buffer','Sensor readings arrive continuously and only recent readings are retained','Bounded circular buffer with explicit overwrite and retention policy',0.86,0.82,0.84,0.84,0.90,0.88,0.76,0.74,0.86,0.84);
