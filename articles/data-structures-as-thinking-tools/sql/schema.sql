DROP TABLE IF EXISTS data_structure_cases;

CREATE TABLE data_structure_cases (
  case_name TEXT PRIMARY KEY,
  problem_context TEXT NOT NULL,
  data_structure_choice TEXT NOT NULL,
  operation_fit REAL NOT NULL,
  structural_fidelity REAL NOT NULL,
  invariant_clarity REAL NOT NULL,
  complexity_awareness REAL NOT NULL,
  memory_awareness REAL NOT NULL,
  interpretability REAL NOT NULL,
  retrieval_support REAL NOT NULL,
  transformation_support REAL NOT NULL,
  representation_risk_documentation REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

INSERT INTO data_structure_cases VALUES
('Task scheduling priority queue','Work items must be processed by priority while preserving audit metadata','Priority queue backed by a heap with timestamp and provenance records',0.90,0.82,0.84,0.86,0.78,0.76,0.84,0.78,0.80,0.82),
('Relationship analysis graph','Entities and dependencies must be traversed and analyzed as relationships','Typed weighted graph with edge provenance and traversal constraints',0.88,0.86,0.78,0.80,0.74,0.78,0.82,0.84,0.84,0.84),
('Case records table','Institutional cases must be stored queried joined and audited','Relational table with keys constraints indexes controlled vocabulary and provenance fields',0.84,0.78,0.86,0.78,0.72,0.88,0.86,0.78,0.86,0.90),
('Document similarity vector index','Documents must be retrieved by semantic similarity and filtered by source metadata','Vector index paired with metadata table and retrieval logs',0.86,0.74,0.70,0.80,0.78,0.62,0.92,0.84,0.82,0.84);
