CREATE TABLE IF NOT EXISTS feature_register (
  feature_name TEXT PRIMARY KEY,
  construct_role TEXT,
  source_process TEXT,
  proxy_risk TEXT,
  review_question TEXT
);

CREATE TABLE IF NOT EXISTS measurement_metrics_by_group (
  group_name TEXT PRIMARY KEY,
  n INTEGER,
  label_positive_rate REAL,
  construct_positive_rate REAL,
  label_disagreement_rate REAL,
  sensitivity REAL,
  specificity REAL,
  false_positive_rate REAL,
  false_negative_rate REAL,
  missing_prior_access_rate REAL,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS measurement_governance_checklist (
  check_name TEXT PRIMARY KEY,
  status TEXT,
  review_question TEXT
);
