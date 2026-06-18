DROP TABLE IF EXISTS randomized_algorithm_cases;
DROP TABLE IF EXISTS random_trials;

CREATE TABLE randomized_algorithm_cases (
  case_name TEXT PRIMARY KEY, problem_context TEXT, randomized_procedure TEXT,
  randomness_clarity REAL, distribution_validity REAL, seed_control REAL,
  error_bound_clarity REAL, sample_adequacy REAL, repeatability REAL,
  edge_case_coverage REAL, variance_analysis REAL, traceability REAL, governance_readiness REAL
);

CREATE TABLE random_trials (
  trial_id TEXT PRIMARY KEY,
  procedure TEXT,
  seed INTEGER,
  sample_size INTEGER,
  estimate REAL,
  error_bound REAL,
  notes TEXT
);

INSERT INTO randomized_algorithm_cases VALUES
('Randomized quicksort','Sort records while reducing dependence on input order','Randomly choose pivots and record seed for reproducibility',0.90,0.88,0.90,0.78,0.82,0.90,0.84,0.82,0.86,0.80),
('Monte Carlo risk estimate','Estimate probability of exceeding a policy threshold under uncertain inputs','Sample uncertain parameters across repeated simulation trials',0.88,0.82,0.88,0.84,0.86,0.88,0.78,0.86,0.88,0.86),
('Sampled data audit','Estimate error rate in a large review dataset','Draw stratified random samples and report uncertainty intervals',0.84,0.80,0.86,0.82,0.80,0.86,0.72,0.78,0.90,0.88),
('Opaque stochastic ranking','A ranking system injects random exploration without documenting exposure effects','Randomly promote candidates but does not record seeds rates or group outcomes',0.42,0.36,0.28,0.30,0.44,0.24,0.36,0.32,0.30,0.34);

INSERT INTO random_trials VALUES
('T-001','monte_carlo_pi',20260617,5000,3.1424,0.025,'reproducible seeded run'),
('T-002','sampled_audit',20260617,400,0.074,0.018,'stratified synthetic audit'),
('T-003','randomized_quicksort',20260617,6,0,0,'correct sorted output with randomized pivots'),
('T-004','load_balancing',20260617,1000,0.503,0.032,'two-server split estimate');
