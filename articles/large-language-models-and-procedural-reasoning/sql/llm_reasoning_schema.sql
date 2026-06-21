CREATE TABLE IF NOT EXISTS llm_sample_outputs (
  case_id TEXT PRIMARY KEY,
  task TEXT,
  output TEXT,
  expected_sources TEXT,
  stakes TEXT,
  requires_factual_support INTEGER,
  tool_used TEXT
);

CREATE TABLE IF NOT EXISTS llm_reasoning_audit (
  case_id TEXT PRIMARY KEY,
  task TEXT,
  stakes TEXT,
  tool_used TEXT,
  requires_factual_support INTEGER,
  steps_found INTEGER,
  procedural_score REAL,
  source_score REAL,
  risk_score REAL,
  overall_score REAL,
  missing_sources TEXT,
  risk_flags TEXT,
  status TEXT,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS llm_governance_register (
  item TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);

CREATE TABLE IF NOT EXISTS llm_tool_permission_matrix (
  tool_type TEXT PRIMARY KEY,
  allowed_without_approval INTEGER,
  risk TEXT,
  control TEXT
);
