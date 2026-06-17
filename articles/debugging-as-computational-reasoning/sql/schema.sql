DROP TABLE IF EXISTS debugging_reasoning_cases;
DROP TABLE IF EXISTS debugging_governance_notes;

CREATE TABLE debugging_reasoning_cases (
  case_name TEXT PRIMARY KEY,
  system_context TEXT NOT NULL,
  failure_description TEXT NOT NULL,
  expected_behavior TEXT NOT NULL,
  observed_behavior TEXT NOT NULL,
  reproducibility REAL NOT NULL,
  expected_behavior_clarity REAL NOT NULL,
  trace_quality REAL NOT NULL,
  hypothesis_strength REAL NOT NULL,
  isolation_quality REAL NOT NULL,
  edge_case_awareness REAL NOT NULL,
  fix_verification REAL NOT NULL,
  regression_testing REAL NOT NULL,
  documentation_quality REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

INSERT INTO debugging_reasoning_cases VALUES
('Graph traversal infinite loop','Recursive graph search with cycles','Search fails to terminate on cyclic graphs','Return a path when target exists or no-solution status when exhausted','Procedure repeatedly revisits nodes and does not halt',0.88,0.84,0.78,0.82,0.80,0.76,0.82,0.78,0.70,0.62),
('Data pipeline missing-value bug','Synthetic data-cleaning workflow','Valid zero values are treated as missing','Missing values should be flagged while valid zeros remain valid','Records with zero values are removed from the dataset',0.84,0.78,0.74,0.76,0.72,0.80,0.76,0.74,0.68,0.70),
('Simulation instability','Discrete-time numerical simulation','State values oscillate unrealistically','State trajectory should remain within plausible range under documented parameters','Large time step causes unstable updates',0.80,0.72,0.78,0.74,0.70,0.72,0.74,0.66,0.64,0.68),
('Recommendation ranking tie bug','Ranking system with scored candidates','Tied candidates appear in unstable order','Ties should be resolved by documented secondary criteria','Rank order changes between runs',0.76,0.70,0.68,0.72,0.70,0.74,0.72,0.70,0.62,0.58);

CREATE TABLE debugging_governance_notes (
  note_key TEXT PRIMARY KEY,
  note_text TEXT NOT NULL
);

INSERT INTO debugging_governance_notes VALUES
('expected_behavior','State expected behavior before changing code.'),
('reproduce','Reproduce the problem with the smallest useful case.'),
('evidence','Preserve inputs environment versions logs traces and observed behavior.'),
('hypothesis','Form a testable hypothesis before applying a fix.'),
('verify','Verify that the fix addresses the cause not merely the symptom.'),
('regression','Add regression tests for every meaningful bug.');
