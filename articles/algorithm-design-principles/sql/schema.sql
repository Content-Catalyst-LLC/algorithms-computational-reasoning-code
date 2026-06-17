DROP TABLE IF EXISTS algorithm_design_cases;
CREATE TABLE algorithm_design_cases (
  case_name TEXT PRIMARY KEY, problem_context TEXT, design_choice TEXT,
  problem_formulation REAL, input_output_clarity REAL, correctness_rationale REAL, termination_argument REAL,
  complexity_analysis REAL, data_structure_fit REAL, edge_case_coverage REAL, robustness REAL, interpretability REAL, governance_readiness REAL
);
INSERT INTO algorithm_design_cases VALUES
('Shortest-path procedure','A routing workflow needs the minimum-cost path through a nonnegative weighted graph','Use Dijkstra-style priority queue strategy with explicit nonnegative-weight precondition',0.92,0.90,0.90,0.88,0.88,0.90,0.84,0.82,0.86,0.84),
('Data validation pipeline','A workflow must reject malformed records before scoring and reporting','Use schema validation explicit errors audit records and edge-case tests',0.88,0.92,0.84,0.90,0.80,0.86,0.90,0.88,0.90,0.90),
('Approximate recommendation ranking','A large content system must rank many items under latency and diversity constraints','Use indexed retrieval scoring heuristics diversity constraints monitoring and human-review feedback',0.84,0.82,0.72,0.86,0.86,0.88,0.78,0.80,0.76,0.86),
('Unspecified optimization script','A script searches for a best option without defining objective constraints or error behavior','Ad hoc scoring and manual inspection',0.42,0.44,0.32,0.48,0.36,0.44,0.34,0.36,0.46,0.30);
