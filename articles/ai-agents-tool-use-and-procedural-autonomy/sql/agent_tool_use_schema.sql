CREATE TABLE IF NOT EXISTS agent_tool_registry (
  tool TEXT PRIMARY KEY,
  action_type TEXT NOT NULL,
  risk REAL NOT NULL,
  approval_required INTEGER NOT NULL,
  permission_scope TEXT
);

CREATE TABLE IF NOT EXISTS agent_planned_actions (
  step INTEGER PRIMARY KEY,
  task TEXT NOT NULL,
  tool TEXT NOT NULL,
  approved INTEGER NOT NULL,
  observation_quality REAL,
  instruction_source TEXT
);

CREATE TABLE IF NOT EXISTS agent_tool_use_audit (
  step INTEGER PRIMARY KEY,
  task TEXT,
  tool TEXT,
  action_type TEXT,
  tool_risk REAL,
  approved INTEGER,
  approval_required INTEGER,
  approval_violation INTEGER,
  step_limit_violation INTEGER,
  untrusted_instruction INTEGER,
  escalation_required INTEGER,
  status TEXT
);

CREATE TABLE IF NOT EXISTS agent_governance_register (
  item TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
