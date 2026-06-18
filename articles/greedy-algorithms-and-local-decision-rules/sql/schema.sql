DROP TABLE IF EXISTS greedy_cases;
DROP TABLE IF EXISTS priority_queue_cases;

CREATE TABLE greedy_cases (
  case_name TEXT PRIMARY KEY, problem_context TEXT, local_decision_rule TEXT,
  local_rule_clarity REAL, global_objective_clarity REAL, greedy_choice_evidence REAL,
  optimal_substructure_evidence REAL, feasibility_check_quality REAL, edge_case_coverage REAL,
  counterexample_testing REAL, traceability REAL, robustness REAL, governance_readiness REAL
);

CREATE TABLE priority_queue_cases (
  case_id TEXT PRIMARY KEY,
  risk_score REAL,
  urgency_score REAL,
  eligibility TEXT,
  review_capacity TEXT,
  local_priority REAL
);

INSERT INTO greedy_cases VALUES
('Interval scheduling by earliest finish','Select the maximum number of non-overlapping intervals','Repeatedly choose the compatible interval with the earliest finish time',0.94,0.92,0.92,0.88,0.90,0.86,0.84,0.84,0.86,0.80),
('Dijkstra shortest path','Find shortest paths from a source in a graph with nonnegative edge weights','Finalize the unvisited node with the smallest tentative distance',0.92,0.92,0.90,0.90,0.88,0.84,0.86,0.88,0.84,0.82),
('Risk review priority queue','A workflow processes cases in order of current risk score','Select the highest current risk score subject to eligibility and review capacity',0.84,0.76,0.58,0.54,0.82,0.72,0.62,0.86,0.70,0.88),
('Nearest-neighbor route heuristic','A routing workflow chooses the nearest unvisited location at each step','Move to the nearest unvisited candidate',0.88,0.82,0.40,0.36,0.78,0.58,0.48,0.76,0.52,0.58);

INSERT INTO priority_queue_cases VALUES
('R-001',84,70,'true','available',84),
('R-002',92,50,'true','available',92),
('R-003',92,60,'true','available',92),
('R-004',71,95,'true','available',71),
('R-005',88,40,'false','blocked',88);
