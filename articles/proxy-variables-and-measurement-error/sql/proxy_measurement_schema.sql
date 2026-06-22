CREATE TABLE IF NOT EXISTS proxy_variable_cases (
  case_id TEXT PRIMARY KEY,
  construct TEXT NOT NULL,
  proxy TEXT NOT NULL,
  proxy_validity REAL NOT NULL,
  missingness_rate REAL NOT NULL,
  differential_error REAL NOT NULL,
  label_error REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS proxy_measurement_error_audit (
  case_id TEXT PRIMARY KEY,
  construct TEXT,
  proxy TEXT,
  proxy_validity REAL,
  validity_gap REAL,
  missingness_rate REAL,
  differential_error REAL,
  label_error REAL,
  measurement_risk_score REAL,
  status TEXT
);

CREATE TABLE IF NOT EXISTS measurement_governance_register (
  item TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
