-- privacy_preserving_governance_schema.sql
-- Educational schema for documenting privacy-preserving computation governance.

CREATE TABLE IF NOT EXISTS privacy_governance_cases (
  case_id INTEGER PRIMARY KEY,
  case_name TEXT NOT NULL,
  privacy_goal TEXT NOT NULL,
  method TEXT NOT NULL,
  threat_model TEXT NOT NULL,
  privacy_budget REAL,
  output_review_required INTEGER NOT NULL DEFAULT 1,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS privacy_releases (
  release_id INTEGER PRIMARY KEY,
  case_id INTEGER NOT NULL,
  release_name TEXT NOT NULL,
  epsilon REAL,
  purpose TEXT NOT NULL,
  small_cell_review INTEGER NOT NULL DEFAULT 1,
  FOREIGN KEY (case_id) REFERENCES privacy_governance_cases(case_id)
);

INSERT INTO privacy_governance_cases (case_name, privacy_goal, method, threat_model, privacy_budget)
VALUES
('Differentially private public statistics', 'reduce individual disclosure risk', 'differential privacy', 'external analyst with auxiliary data', 1.0),
('Federated learning with secure aggregation', 'reduce raw-data centralization', 'federated learning plus secure aggregation', 'honest-but-curious aggregator', NULL);

INSERT INTO privacy_releases (case_id, release_name, epsilon, purpose)
VALUES
(1, 'aggregate_count_by_region', 0.25, 'public reporting'),
(1, 'aggregate_count_by_age_band', 0.20, 'equity analysis');
