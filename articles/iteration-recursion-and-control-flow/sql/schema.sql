DROP TABLE IF EXISTS control_flow_cases;
CREATE TABLE control_flow_cases (
  case_name TEXT PRIMARY KEY, problem_context TEXT, control_flow_choice TEXT,
  path_clarity REAL, loop_structure REAL, recursion_structure REAL, state_update_discipline REAL,
  termination_evidence REAL, invariant_evidence REAL, edge_case_coverage REAL, error_handling REAL, traceability REAL, governance_readiness REAL
);
INSERT INTO control_flow_cases VALUES
('Dataset validation loop','A workflow validates many records and separates valid records from errors','Collection loop with guard clauses accumulators error table and audit trail',0.90,0.90,0.70,0.88,0.90,0.86,0.90,0.90,0.88,0.88),
('Recursive tree traversal','A knowledge taxonomy must be traversed from root to nested leaves','Recursive traversal with base case for leaves depth checks and visited-path evidence',0.88,0.76,0.92,0.84,0.90,0.88,0.84,0.78,0.86,0.82),
('Asynchronous review workflow','High-risk model outputs should route through automated checks and human review','Event-driven control with status states timeout handling review queue and correlation IDs',0.84,0.78,0.64,0.86,0.82,0.82,0.84,0.88,0.90,0.92),
('Unbounded retry loop','A script retries failed external calls without a timeout maximum count or audit record','Condition loop with unclear failure behavior',0.46,0.42,0.50,0.44,0.22,0.34,0.36,0.28,0.30,0.28);
