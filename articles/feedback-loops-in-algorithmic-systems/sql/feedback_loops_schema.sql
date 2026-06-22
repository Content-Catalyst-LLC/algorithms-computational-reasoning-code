CREATE TABLE IF NOT EXISTS feedback_loop_cases (
  case_id TEXT PRIMARY KEY,
  system TEXT NOT NULL,
  feedback_path TEXT NOT NULL,
  amplification REAL NOT NULL,
  exposure_concentration REAL NOT NULL,
  intervention_influence REAL NOT NULL,
  drift REAL NOT NULL,
  recursive_data REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS feedback_loop_audit (
  case_id TEXT PRIMARY KEY,
  system TEXT,
  feedback_path TEXT,
  amplification REAL,
  exposure_concentration REAL,
  intervention_influence REAL,
  drift REAL,
  recursive_data REAL,
  feedback_risk_score REAL,
  status TEXT
);

CREATE TABLE IF NOT EXISTS feedback_governance_register (
  item TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
