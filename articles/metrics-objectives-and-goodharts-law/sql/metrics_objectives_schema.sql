CREATE TABLE IF NOT EXISTS metric_objective_cases (
  case_id TEXT PRIMARY KEY,
  objective TEXT NOT NULL,
  metric TEXT NOT NULL,
  proxy_alignment REAL NOT NULL,
  optimization_pressure REAL NOT NULL,
  gaming_risk REAL NOT NULL,
  guardrails INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS goodhart_risk_audit (
  case_id TEXT PRIMARY KEY,
  objective TEXT,
  metric TEXT,
  proxy_gap REAL,
  optimization_pressure REAL,
  gaming_risk REAL,
  guardrails INTEGER,
  goodhart_risk_score REAL,
  status TEXT
);

CREATE TABLE IF NOT EXISTS guardrail_metric_register (
  guardrail TEXT PRIMARY KEY,
  purpose TEXT,
  status TEXT
);

CREATE TABLE IF NOT EXISTS metric_governance_register (
  item TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
