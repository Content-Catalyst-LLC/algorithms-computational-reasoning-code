DROP TABLE IF EXISTS optimization_cases;
CREATE TABLE optimization_cases (
  case_name TEXT PRIMARY KEY,
  objective_clarity REAL,
  constraint_documentation REAL,
  feasible_set_clarity REAL,
  data_quality REAL,
  uncertainty_handling REAL,
  sensitivity_review REAL,
  tradeoff_transparency REAL,
  fairness_review REAL,
  robustness_review REAL,
  traceability REAL,
  governance_review REAL,
  communication_clarity REAL
);

DROP TABLE IF EXISTS optimization_metrics;
CREATE TABLE optimization_metrics (
  case_name TEXT PRIMARY KEY,
  c1 REAL,
  c2 REAL,
  c3 REAL,
  x1 REAL,
  x2 REAL,
  x3 REAL,
  limit_value REAL,
  observed_value REAL,
  base_objective REAL,
  penalty REAL,
  penalty_weight REAL,
  cost_score REAL,
  quality_score REAL,
  risk_score REAL
);

INSERT INTO optimization_cases VALUES
('Route optimization',0.86,0.84,0.82,0.78,0.70,0.72,0.78,0.62,0.74,0.80,0.70,0.76),
('Resource allocation',0.82,0.88,0.80,0.76,0.68,0.70,0.84,0.86,0.72,0.78,0.82,0.80),
('Machine learning training',0.78,0.62,0.66,0.70,0.58,0.64,0.60,0.54,0.62,0.70,0.60,0.66),
('Opaque engagement maximization',0.52,0.28,0.34,0.60,0.26,0.24,0.18,0.20,0.30,0.34,0.28,0.36);

INSERT INTO optimization_metrics VALUES
('allocation_example',4.0,2.0,1.5,10.0,20.0,5.0,100.0,86.5,42.0,8.0,2.5,0.30,0.82,0.25),
('routing_example',1.2,0.8,3.0,20.0,35.0,2.0,75.0,62.0,58.0,5.0,1.8,0.40,0.76,0.30),
('model_training_example',0.6,0.3,0.1,0.72,0.18,0.10,1.0,0.94,0.28,0.12,0.75,0.25,0.84,0.42);
