CREATE TABLE IF NOT EXISTS candidate_use_cases (
  use_case TEXT PRIMARY KEY,
  target_legitimacy REAL NOT NULL,
  data_legitimacy REAL NOT NULL,
  contestability REAL NOT NULL,
  human_judgment REAL NOT NULL,
  governance_capacity REAL NOT NULL,
  repairability REAL NOT NULL,
  stakes REAL NOT NULL,
  irreversibility REAL NOT NULL,
  proxy_illegitimacy REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS algorithmic_non_use_audit (
  use_case TEXT PRIMARY KEY,
  responsible_use_readiness_score REAL NOT NULL,
  non_use_pressure_score REAL NOT NULL,
  recommendation TEXT NOT NULL,
  status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS algorithmic_non_use_register (
  criterion TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
