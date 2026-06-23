CREATE TABLE IF NOT EXISTS turing_themes (
  theme_id TEXT PRIMARY KEY,
  formalization REAL NOT NULL,
  machine_abstraction REAL NOT NULL,
  symbolic_representation REAL NOT NULL,
  universality REAL NOT NULL,
  decidability REAL NOT NULL,
  limit_awareness REAL NOT NULL,
  reasoning_relevance REAL NOT NULL,
  ai_relevance REAL NOT NULL,
  governance_caution REAL NOT NULL,
  modern_resonance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS turing_machine_reasoning_map (
  theme_id TEXT PRIMARY KEY,
  formalization REAL NOT NULL,
  machine_abstraction REAL NOT NULL,
  symbolic_representation REAL NOT NULL,
  universality REAL NOT NULL,
  decidability REAL NOT NULL,
  limit_awareness REAL NOT NULL,
  reasoning_relevance REAL NOT NULL,
  ai_relevance REAL NOT NULL,
  governance_caution REAL NOT NULL,
  modern_resonance REAL NOT NULL,
  reasoning_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
