CREATE TABLE IF NOT EXISTS symbolic_facts (
  fact_id INTEGER PRIMARY KEY,
  fact TEXT NOT NULL UNIQUE,
  source TEXT,
  status TEXT
);

CREATE TABLE IF NOT EXISTS symbolic_rules (
  rule_id TEXT PRIMARY KEY,
  premises TEXT NOT NULL,
  conclusion TEXT NOT NULL,
  provenance TEXT NOT NULL,
  status TEXT DEFAULT 'active'
);

CREATE TABLE IF NOT EXISTS symbolic_inference_trace (
  trace_id INTEGER PRIMARY KEY,
  rule_id TEXT,
  premises TEXT,
  conclusion TEXT,
  provenance TEXT,
  trace_note TEXT
);

CREATE TABLE IF NOT EXISTS symbolic_constraint_review (
  constraint_name TEXT PRIMARY KEY,
  satisfied INTEGER,
  interpretation TEXT
);

CREATE TABLE IF NOT EXISTS symbolic_hybrid_interface_register (
  interface_item TEXT PRIMARY KEY,
  example TEXT,
  review_question TEXT,
  risk TEXT
);
