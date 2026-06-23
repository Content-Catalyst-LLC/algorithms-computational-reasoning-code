CREATE TABLE IF NOT EXISTS wiener_themes (
  theme_id TEXT PRIMARY KEY,
  feedback_centrality REAL NOT NULL,
  control_relevance REAL NOT NULL,
  communication_relevance REAL NOT NULL,
  prediction_relevance REAL NOT NULL,
  stability_relevance REAL NOT NULL,
  amplification_risk REAL NOT NULL,
  automation_ethics REAL NOT NULL,
  ai_relevance REAL NOT NULL,
  institutional_relevance REAL NOT NULL,
  governance_caution REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS wiener_cybernetic_feedback_map (
  theme_id TEXT PRIMARY KEY,
  feedback_centrality REAL NOT NULL,
  control_relevance REAL NOT NULL,
  communication_relevance REAL NOT NULL,
  prediction_relevance REAL NOT NULL,
  stability_relevance REAL NOT NULL,
  amplification_risk REAL NOT NULL,
  automation_ethics REAL NOT NULL,
  ai_relevance REAL NOT NULL,
  institutional_relevance REAL NOT NULL,
  governance_caution REAL NOT NULL,
  cybernetic_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
