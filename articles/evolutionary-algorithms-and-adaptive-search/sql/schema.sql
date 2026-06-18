DROP TABLE IF EXISTS evolutionary_cases;
DROP TABLE IF EXISTS generation_records;

CREATE TABLE evolutionary_cases (
  case_name TEXT PRIMARY KEY, problem_context TEXT, evolutionary_strategy TEXT,
  representation_clarity REAL, fitness_alignment REAL, variation_design REAL,
  diversity_tracking REAL, parameter_documentation REAL, benchmark_evidence REAL,
  robustness_testing REAL, traceability REAL, safety_review REAL, governance_readiness REAL
);

CREATE TABLE generation_records (
  generation INTEGER,
  best_fitness REAL,
  average_fitness REAL,
  diversity REAL,
  seed INTEGER,
  notes TEXT
);

INSERT INTO evolutionary_cases VALUES
('Genetic route optimization','Search for shorter routes across many locations','Permutation encoding with swap mutation and ordered crossover',0.88,0.86,0.84,0.80,0.82,0.78,0.76,0.84,0.76,0.78),
('Symbolic regression','Discover interpretable mathematical expressions from data','Tree-based genetic programming with parsimony pressure',0.84,0.82,0.80,0.78,0.80,0.82,0.78,0.82,0.74,0.76),
('Multi-objective design search','Explore cost reliability and sustainability trade-offs','Population-based Pareto search with diversity preservation',0.86,0.86,0.82,0.86,0.80,0.80,0.82,0.84,0.82,0.84),
('Opaque evolved ranking rule','Evolve ranking rules using engagement-only fitness','Tree-based rule evolution without held-out fairness review',0.46,0.28,0.40,0.32,0.34,0.30,0.26,0.34,0.22,0.26);

INSERT INTO generation_records VALUES
(0,7,5.10,0.51,20260617,'initial random population'),
(5,10,7.80,0.39,20260617,'selection begins concentrating population'),
(10,11,8.85,0.31,20260617,'fitness improving diversity falling'),
(20,12,10.70,0.18,20260617,'near maximum fitness with lower diversity'),
(30,12,11.20,0.11,20260617,'possible convergence');
