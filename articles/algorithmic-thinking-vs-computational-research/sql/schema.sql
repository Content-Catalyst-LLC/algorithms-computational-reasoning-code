DROP TABLE IF EXISTS reasoning_profiles;
DROP TABLE IF EXISTS reasoning_governance_notes;

CREATE TABLE reasoning_profiles (
  name TEXT PRIMARY KEY,
  step_clarity REAL NOT NULL,
  decomposition REAL NOT NULL,
  control_flow REAL NOT NULL,
  testability REAL NOT NULL,
  representation_quality REAL NOT NULL,
  data_context REAL NOT NULL,
  complexity_awareness REAL NOT NULL,
  interpretability REAL NOT NULL,
  governance_readiness REAL NOT NULL,
  stakeholder_awareness REAL NOT NULL
);

INSERT INTO reasoning_profiles VALUES
('Recipe-like procedure',0.86,0.72,0.70,0.62,0.42,0.34,0.30,0.48,0.20,0.28),
('Classroom algorithm exercise',0.90,0.82,0.84,0.78,0.62,0.46,0.62,0.58,0.32,0.36),
('Search and ranking system',0.72,0.70,0.76,0.66,0.78,0.76,0.72,0.62,0.70,0.72),
('Public decision-support workflow',0.68,0.66,0.64,0.72,0.80,0.84,0.66,0.78,0.86,0.88),
('Scientific modeling workflow',0.74,0.78,0.76,0.82,0.86,0.80,0.84,0.78,0.74,0.68);

CREATE TABLE reasoning_governance_notes (
  note_key TEXT PRIMARY KEY,
  note_text TEXT NOT NULL
);

INSERT INTO reasoning_governance_notes VALUES
('procedure','Algorithmic thinking emphasizes procedural clarity.'),
('representation','Computational reasoning asks what the representation makes visible and invisible.'),
('context','Computational reasoning links procedure to data, scale, interpretation, stakeholders, and governance.'),
('responsibility','Consequential systems require documentation, monitoring, appeal, and revision.');
