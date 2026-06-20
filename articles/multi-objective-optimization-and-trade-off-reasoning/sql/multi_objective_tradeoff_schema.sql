-- Schema for multi-objective optimization and trade-off reasoning audit records.
CREATE TABLE IF NOT EXISTS tradeoff_alternatives (
  alternative TEXT PRIMARY KEY,
  cost REAL NOT NULL,
  risk REAL NOT NULL,
  emissions REAL NOT NULL,
  service_quality REAL NOT NULL,
  access REAL NOT NULL,
  robustness REAL NOT NULL,
  burden REAL NOT NULL,
  pareto_efficient INTEGER NOT NULL DEFAULT 0,
  weighted_score REAL
);

CREATE TABLE IF NOT EXISTS tradeoff_governance_audit (
  case_name TEXT PRIMARY KEY,
  objective_inventory REAL,
  metric_validity REAL,
  weight_documentation REAL,
  constraint_clarity REAL,
  pareto_analysis REAL,
  sensitivity_review REAL,
  robustness_review REAL,
  fairness_review REAL,
  stakeholder_review REAL,
  traceability REAL,
  governance_review REAL,
  communication_clarity REAL,
  tradeoff_governance_score REAL,
  tradeoff_governance_risk REAL,
  diagnostic TEXT
);
