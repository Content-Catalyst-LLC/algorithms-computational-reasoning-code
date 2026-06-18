DROP TABLE IF EXISTS search_strategy_cases;
DROP TABLE IF EXISTS candidate_records;

CREATE TABLE search_strategy_cases (
  case_name TEXT PRIMARY KEY, problem_context TEXT, search_strategy TEXT,
  search_space_clarity REAL, candidate_generation_completeness REAL, constraint_quality REAL,
  pruning_soundness REAL, bound_validity REAL, objective_clarity REAL,
  edge_case_coverage REAL, traceability REAL, complexity_awareness REAL, governance_readiness REAL
);

CREATE TABLE candidate_records (
  candidate_id TEXT PRIMARY KEY,
  search_family TEXT,
  depth INTEGER,
  feasible TEXT,
  objective_value REAL,
  pruned TEXT,
  prune_reason TEXT
);

INSERT INTO search_strategy_cases VALUES
('Backtracking graph coloring','Assign colors to graph nodes without adjacent conflicts','Recursive backtracking with constraint pruning and variable ordering',0.90,0.88,0.90,0.88,0.70,0.82,0.84,0.84,0.88,0.80),
('Branch and bound knapsack','Maximize value under a capacity constraint','Branch on include/exclude decisions and prune using upper-bound estimates',0.90,0.90,0.88,0.86,0.88,0.90,0.84,0.86,0.90,0.82),
('Exhaustive small-case validation','Validate a heuristic by checking all small candidate solutions','Enumerate all feasible candidates and compare heuristic output to exact optimum',0.92,0.94,0.86,0.80,0.72,0.88,0.90,0.88,0.90,0.84),
('Opaque eligibility search','A decision system searches eligible configurations using undocumented pruning rules','Partial search with hidden exclusions and unclear stopping criteria',0.42,0.38,0.44,0.30,0.28,0.46,0.40,0.32,0.50,0.36);

INSERT INTO candidate_records VALUES
('C-001','exhaustive_subset',0,'true',0,'false','none'),
('C-002','exhaustive_subset',1,'true',3,'false','none'),
('C-003','backtracking_coloring',2,'false',0,'true','constraint_violation'),
('C-004','branch_bound_knapsack',3,'true',22,'false','incumbent_update'),
('C-005','branch_bound_knapsack',4,'false',18,'true','bound_worse_than_incumbent');
