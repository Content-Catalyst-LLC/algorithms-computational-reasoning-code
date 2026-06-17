DROP TABLE IF EXISTS verification_cases;

CREATE TABLE verification_cases (
  case_name TEXT PRIMARY KEY,
  computational_context TEXT NOT NULL,
  correctness_claim TEXT NOT NULL,
  specification_clarity REAL NOT NULL,
  precondition_definition REAL NOT NULL,
  postcondition_definition REAL NOT NULL,
  invariant_coverage REAL NOT NULL,
  termination_evidence REAL NOT NULL,
  test_coverage REAL NOT NULL,
  counterexample_handling REAL NOT NULL,
  static_check_support REAL NOT NULL,
  traceability REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

INSERT INTO verification_cases VALUES
('Sorting procedure','Algorithm returns an ordered sequence from a finite input list','Output is sorted and preserves all input elements',0.88,0.82,0.88,0.84,0.86,0.78,0.76,0.68,0.78,0.64),
('Database transaction rule','Transaction system preserves account and referential integrity','Every committed transaction satisfies schema and balance constraints',0.82,0.80,0.84,0.86,0.72,0.80,0.74,0.72,0.82,0.78),
('Distributed coordination protocol','Nodes coordinate under message delay and partial failure','No two nodes commit conflicting decisions',0.78,0.72,0.76,0.82,0.62,0.66,0.80,0.74,0.84,0.76),
('Decision-rule workflow','Institutional routing system assigns cases to review categories','Outputs follow documented rules thresholds exceptions and review requirements',0.74,0.70,0.72,0.66,0.70,0.72,0.68,0.60,0.78,0.84);
