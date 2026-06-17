DROP TABLE IF EXISTS boundary_reliability_cases;

CREATE TABLE boundary_reliability_cases (
  case_name TEXT PRIMARY KEY,
  computational_context TEXT NOT NULL,
  reliability_claim TEXT NOT NULL,
  stopping_condition_clarity REAL NOT NULL,
  progress_measure_definition REAL NOT NULL,
  invariant_coverage REAL NOT NULL,
  boundary_case_coverage REAL NOT NULL,
  invalid_input_handling REAL NOT NULL,
  recursion_safety REAL NOT NULL,
  numerical_edge_handling REAL NOT NULL,
  concurrency_edge_awareness REAL NOT NULL,
  counterexample_traceability REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

INSERT INTO boundary_reliability_cases VALUES
('Graph traversal','Traversal over nodes and edges in a possibly cyclic graph','Traversal terminates and visits each reachable node at most once',0.84,0.82,0.80,0.76,0.70,0.74,0.54,0.58,0.78,0.66),
('Recursive parser','Parser processes nested symbolic expressions','Parser terminates on valid finite input and returns structured parse results or clear errors',0.82,0.80,0.76,0.80,0.78,0.82,0.50,0.52,0.76,0.70),
('Numerical simulation step','Simulation updates state values under documented numerical constraints','State updates remain within modeled bounds and report convergence failure clearly',0.76,0.74,0.78,0.74,0.72,0.60,0.82,0.56,0.72,0.74),
('Distributed request workflow','Service request moves through retries timeout success failure or escalation','Every request reaches success failure timeout or review without duplicate unsafe action',0.78,0.72,0.76,0.76,0.70,0.52,0.56,0.84,0.80,0.82);
