CREATE TABLE IF NOT EXISTS origin_story_themes (
  theme_id TEXT PRIMARY KEY,
  evidence_grounding REAL NOT NULL,
  scope_clarity REAL NOT NULL,
  anachronism_control REAL NOT NULL,
  network_awareness REAL NOT NULL,
  etymology_caution REAL NOT NULL,
  transmission_depth REAL NOT NULL,
  credit_distribution REAL NOT NULL,
  public_usefulness REAL NOT NULL,
  historical_significance REAL NOT NULL,
  modern_resonance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS origin_story_care_map (
  theme_id TEXT PRIMARY KEY,
  evidence_grounding REAL NOT NULL,
  scope_clarity REAL NOT NULL,
  anachronism_control REAL NOT NULL,
  network_awareness REAL NOT NULL,
  etymology_caution REAL NOT NULL,
  transmission_depth REAL NOT NULL,
  credit_distribution REAL NOT NULL,
  public_usefulness REAL NOT NULL,
  historical_significance REAL NOT NULL,
  modern_resonance REAL NOT NULL,
  origin_care_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
