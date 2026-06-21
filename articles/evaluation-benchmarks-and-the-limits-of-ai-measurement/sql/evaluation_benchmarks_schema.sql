CREATE TABLE IF NOT EXISTS benchmark_items (
  item_id INTEGER PRIMARY KEY,
  model TEXT NOT NULL,
  task TEXT NOT NULL,
  group_name TEXT NOT NULL,
  correct INTEGER NOT NULL,
  confidence REAL NOT NULL,
  safety_flag INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS model_evaluation_summary (
  model TEXT PRIMARY KEY,
  n INTEGER,
  accuracy REAL,
  avg_confidence REAL,
  calibration_gap REAL,
  safety_flag_rate REAL,
  saturated INTEGER,
  status TEXT
);

CREATE TABLE IF NOT EXISTS benchmark_limit_register (
  limit_name TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);

CREATE TABLE IF NOT EXISTS evaluation_governance_register (
  item TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
