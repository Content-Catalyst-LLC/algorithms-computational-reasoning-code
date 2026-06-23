CREATE TABLE IF NOT EXISTS lovelace_themes (
  theme_id TEXT PRIMARY KEY,
  programming_structure REAL NOT NULL,
  symbolic_generality REAL NOT NULL,
  machine_orientation REAL NOT NULL,
  mathematical_grounding REAL NOT NULL,
  imaginative_reach REAL NOT NULL,
  limit_awareness REAL NOT NULL,
  collaboration REAL NOT NULL,
  authorship REAL NOT NULL,
  modern_resonance REAL NOT NULL,
  ai_caution REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS lovelace_computation_imagination_map (
  theme_id TEXT PRIMARY KEY,
  programming_structure REAL NOT NULL,
  symbolic_generality REAL NOT NULL,
  machine_orientation REAL NOT NULL,
  mathematical_grounding REAL NOT NULL,
  imaginative_reach REAL NOT NULL,
  limit_awareness REAL NOT NULL,
  collaboration REAL NOT NULL,
  authorship REAL NOT NULL,
  modern_resonance REAL NOT NULL,
  ai_caution REAL NOT NULL,
  imagination_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
