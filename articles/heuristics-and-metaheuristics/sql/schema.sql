DROP TABLE IF EXISTS heuristic_cases;
DROP TABLE IF EXISTS benchmark_records;

CREATE TABLE heuristic_cases (
  case_name TEXT PRIMARY KEY, problem_context TEXT, heuristic_strategy TEXT,
  purpose_clarity REAL, rule_transparency REAL, benchmark_evidence REAL,
  parameter_documentation REAL, robustness_testing REAL, edge_case_coverage REAL,
  fairness_review REAL, traceability REAL, monitoring_readiness REAL, governance_readiness REAL
);

CREATE TABLE benchmark_records (
  record_id TEXT PRIMARY KEY,
  case_name TEXT,
  baseline_score REAL,
  heuristic_score REAL,
  score_direction TEXT,
  seed INTEGER,
  notes TEXT
);

INSERT INTO heuristic_cases VALUES
('Nearest-neighbor route heuristic','Construct a fast route through multiple locations','Repeatedly visit the nearest unvisited location',0.88,0.92,0.74,0.84,0.72,0.68,0.70,0.88,0.76,0.78),
('Simulated annealing schedule repair','Improve a schedule with conflicts delays and competing constraints','Use neighborhood swaps and probabilistic acceptance under a cooling schedule',0.86,0.82,0.82,0.78,0.80,0.76,0.72,0.84,0.80,0.78),
('Tabu allocation search','Allocate resources while avoiding repeated local patterns','Use local moves and tabu memory to discourage cycling',0.84,0.80,0.78,0.76,0.78,0.72,0.74,0.82,0.78,0.80),
('Opaque ranking heuristic','Rank candidates using hidden weights and untested proxy signals','Combines engagement authority and recency signals without documented validation',0.42,0.26,0.34,0.24,0.30,0.28,0.22,0.30,0.36,0.28);

INSERT INTO benchmark_records VALUES
('B-001','Nearest-neighbor route heuristic',34.0,27.0,'minimize',20260617,'nearest neighbor beats simple listed order'),
('B-002','Simulated annealing schedule repair',18.5,12.2,'minimize',20260617,'annealing improves conflict-weighted cost'),
('B-003','Tabu allocation search',21.0,15.4,'minimize',20260617,'tabu memory reduces cycling'),
('B-004','Opaque ranking heuristic',0.0,0.0,'unknown',20260617,'requires governance review');
