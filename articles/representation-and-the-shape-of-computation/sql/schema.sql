DROP TABLE IF EXISTS representation_cases;

CREATE TABLE representation_cases (
  case_name TEXT PRIMARY KEY,
  representation_context TEXT NOT NULL,
  representation_choice TEXT NOT NULL,
  structural_fidelity REAL NOT NULL,
  operation_fit REAL NOT NULL,
  validation_discipline REAL NOT NULL,
  information_loss_control REAL NOT NULL,
  traceability REAL NOT NULL,
  interpretability REAL NOT NULL,
  retrieval_support REAL NOT NULL,
  transformation_readiness REAL NOT NULL,
  risk_documentation REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

INSERT INTO representation_cases VALUES
('Route planning graph','City travel is represented as a weighted graph of intersections and paths','Weighted graph with nodes edges travel-time weights and closure metadata',0.86,0.90,0.78,0.74,0.78,0.82,0.84,0.80,0.76,0.76),
('Institutional records table','Public-service cases are represented as structured rows and fields','Relational table with keys statuses timestamps controlled vocabulary and provenance fields',0.78,0.82,0.86,0.70,0.88,0.84,0.82,0.78,0.82,0.86),
('Document embedding index','Documents are represented as learned vectors for similarity search','Embedding vectors combined with metadata source records and retrieval logs',0.74,0.86,0.72,0.66,0.76,0.60,0.90,0.82,0.78,0.80),
('Simulation state model','A dynamic system is represented with states transitions parameters and assumptions','State-space model with explicit variables transition rules parameter records and scenario metadata',0.82,0.84,0.80,0.78,0.86,0.78,0.74,0.84,0.86,0.84);
