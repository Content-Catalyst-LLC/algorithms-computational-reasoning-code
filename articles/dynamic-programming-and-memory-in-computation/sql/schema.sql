DROP TABLE IF EXISTS dynamic_programming_cases;
DROP TABLE IF EXISTS state_tables;

CREATE TABLE dynamic_programming_cases (
  case_name TEXT PRIMARY KEY, problem_context TEXT, memory_strategy TEXT,
  state_clarity REAL, recurrence_validity REAL, base_case_clarity REAL,
  overlapping_subproblem_evidence REAL, optimal_substructure_evidence REAL,
  transition_clarity REAL, storage_strategy_quality REAL, edge_case_coverage REAL,
  traceability REAL, governance_readiness REAL
);

CREATE TABLE state_tables (
  state_id TEXT PRIMARY KEY,
  state_family TEXT,
  dimension_count INTEGER,
  storage_strategy TEXT,
  backpointer_required TEXT,
  staleness_risk TEXT
);

INSERT INTO dynamic_programming_cases VALUES
('Edit distance table','Compare two strings by insertions deletions and substitutions','Bottom-up table over string prefixes with boundary rows and columns',0.92,0.92,0.90,0.90,0.88,0.90,0.88,0.86,0.84,0.80),
('Knapsack optimization','Choose items under a capacity constraint to maximize value','Tabulation over item index and remaining capacity with include/exclude comparison',0.90,0.90,0.88,0.88,0.90,0.88,0.86,0.84,0.84,0.82),
('Reinforcement learning value table','Estimate future value of states under actions and rewards','Iterative value updates with state-action records and discounting',0.82,0.78,0.74,0.84,0.80,0.76,0.82,0.70,0.78,0.86),
('Opaque staged decision model','A decision-support system stores values across eligibility states without clear rationale','Undocumented state table with unclear value function and limited traceability',0.44,0.40,0.42,0.58,0.46,0.38,0.52,0.44,0.36,0.42);

INSERT INTO state_tables VALUES
('S-001','edit_distance_prefix',2,'full_matrix','true','low'),
('S-002','knapsack_capacity',2,'table_with_reconstruction','true','medium'),
('S-003','value_iteration_state',2,'value_table','false','high'),
('S-004','rolling_sequence_row',2,'rolling_array','false','medium'),
('S-005','sparse_policy_state',3,'sparse_map','true','high');
