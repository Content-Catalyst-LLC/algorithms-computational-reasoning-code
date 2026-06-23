CREATE TABLE IF NOT EXISTS architecture_themes (
  theme_id TEXT PRIMARY KEY,
  stored_program REAL NOT NULL,
  memory_organization REAL NOT NULL,
  control_structure REAL NOT NULL,
  program_as_data REAL NOT NULL,
  implementation_influence REAL NOT NULL,
  bottleneck_awareness REAL NOT NULL,
  collaboration_context REAL NOT NULL,
  software_relevance REAL NOT NULL,
  ai_infrastructure REAL NOT NULL,
  governance_caution REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS von_neumann_architecture_map (
  theme_id TEXT PRIMARY KEY,
  stored_program REAL NOT NULL,
  memory_organization REAL NOT NULL,
  control_structure REAL NOT NULL,
  program_as_data REAL NOT NULL,
  implementation_influence REAL NOT NULL,
  bottleneck_awareness REAL NOT NULL,
  collaboration_context REAL NOT NULL,
  software_relevance REAL NOT NULL,
  ai_infrastructure REAL NOT NULL,
  governance_caution REAL NOT NULL,
  architecture_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
