DROP TABLE IF EXISTS algorithm_scenarios;
DROP TABLE IF EXISTS algorithm_governance_notes;

CREATE TABLE algorithm_scenarios (
  scenario TEXT PRIMARY KEY,
  representation_quality REAL NOT NULL,
  indexing_strength REAL NOT NULL,
  decomposition_strength REAL NOT NULL,
  correctness_evidence REAL NOT NULL,
  interpretability REAL NOT NULL,
  robustness REAL NOT NULL,
  governance_readiness REAL NOT NULL,
  data_quality REAL NOT NULL,
  objective_alignment REAL NOT NULL,
  brute_force_pressure REAL NOT NULL,
  memory_efficiency REAL NOT NULL,
  monitoring_strength REAL NOT NULL
);

INSERT INTO algorithm_scenarios VALUES
('Brute-force procedure',0.40,0.10,0.18,0.28,0.54,0.32,0.20,0.46,0.38,0.92,0.22,0.18),
('Indexed search design',0.62,0.76,0.48,0.52,0.60,0.52,0.38,0.62,0.54,0.42,0.56,0.34),
('Graph-aware reasoning',0.76,0.64,0.72,0.68,0.66,0.62,0.54,0.70,0.66,0.30,0.64,0.50),
('Governed computational reasoning',0.86,0.80,0.82,0.82,0.78,0.76,0.86,0.82,0.84,0.18,0.76,0.84);

CREATE TABLE algorithm_governance_notes (
  note_key TEXT PRIMARY KEY,
  note_text TEXT NOT NULL
);

INSERT INTO algorithm_governance_notes VALUES
('problem_formulation','Separate the real-world concern from the computational task.'),
('representation','Document the data structure schema graph features or state representation.'),
('correctness','Record tests proofs invariants and known failure modes.'),
('complexity','Estimate growth in time memory maintenance and monitoring cost.'),
('accountability','Document review appeal monitoring incident response and retirement conditions.');
