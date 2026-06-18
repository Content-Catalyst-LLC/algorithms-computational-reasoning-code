DROP TABLE IF EXISTS approximation_cases;
DROP TABLE IF EXISTS gap_records;

CREATE TABLE approximation_cases (
  case_name TEXT PRIMARY KEY, problem_context TEXT, approximation_strategy TEXT,
  objective_clarity REAL, feasibility_preservation REAL, guarantee_clarity REAL,
  assumption_validity REAL, bound_evidence REAL, runtime_practicality REAL,
  gap_reporting REAL, edge_case_coverage REAL, traceability REAL, governance_readiness REAL
);

CREATE TABLE gap_records (
  record_id TEXT PRIMARY KEY,
  case_name TEXT,
  algorithm_value REAL,
  bound_value REAL,
  problem_type TEXT,
  reported_gap TEXT,
  acceptable_gap TEXT,
  decision TEXT
);

INSERT INTO approximation_cases VALUES
('Vertex cover 2-approximation','Find a small vertex set touching every edge in a graph','Select both endpoints of uncovered edges until all edges are covered',0.92,0.92,0.90,0.88,0.88,0.92,0.84,0.82,0.86,0.82),
('Greedy set cover','Cover all required elements using low-cost sets','Repeatedly choose the set with best uncovered coverage per cost',0.88,0.90,0.84,0.82,0.82,0.90,0.82,0.78,0.86,0.84),
('Knapsack FPTAS-style scaling','Maximize value under a capacity constraint','Scale values and run dynamic programming on reduced value range',0.90,0.88,0.86,0.84,0.84,0.82,0.86,0.82,0.84,0.82),
('Opaque approximate allocation','Allocate scarce resources using a fast approximation with unclear objective','Uses undocumented scoring and stops at an unknown optimality gap',0.38,0.62,0.26,0.34,0.24,0.78,0.22,0.36,0.30,0.32);

INSERT INTO gap_records VALUES
('G-001','Vertex cover 2-approximation',6,3,'minimization','1.000','1.000','accepted'),
('G-002','Greedy set cover',4,3,'minimization','0.333','0.500','accepted'),
('G-003','Knapsack FPTAS-style scaling',95,100,'maximization','0.050','0.100','accepted'),
('G-004','Opaque approximate allocation',0,0,'unknown','NA','NA','review_required');
