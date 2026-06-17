DROP TABLE IF EXISTS abstraction_cases;
DROP TABLE IF EXISTS abstraction_governance_notes;

CREATE TABLE abstraction_cases (
  case_name TEXT PRIMARY KEY,
  real_system TEXT NOT NULL,
  abstraction TEXT NOT NULL,
  representation_clarity REAL NOT NULL,
  scope_definition REAL NOT NULL,
  detail_preservation REAL NOT NULL,
  assumption_documentation REAL NOT NULL,
  testability REAL NOT NULL,
  interpretability REAL NOT NULL,
  reuse_safety REAL NOT NULL,
  uncertainty_visibility REAL NOT NULL,
  governance_readiness REAL NOT NULL,
  risk_awareness REAL NOT NULL
);

INSERT INTO abstraction_cases VALUES
('Search ranking','People seeking useful information in a large document collection','Documents queries tokens embeddings metadata scores and ranked results',0.82,0.70,0.62,0.58,0.72,0.60,0.58,0.50,0.56,0.64),
('Transit model','Mobility access cost safety time neighborhood effects and service quality','Network graph route segments travel times stations demand estimates and constraints',0.78,0.72,0.66,0.68,0.70,0.72,0.64,0.62,0.66,0.74),
('Database schema','Institutional knowledge people processes documents events and responsibilities','Tables fields keys constraints provenance fields and relationships',0.84,0.78,0.70,0.72,0.76,0.74,0.72,0.60,0.70,0.68),
('Decision-support score','Complex case evidence policy constraints human judgment and affected people','Input fields weighted criteria score threshold recommendation and review queue',0.70,0.60,0.48,0.50,0.64,0.52,0.46,0.44,0.66,0.78);

CREATE TABLE abstraction_governance_notes (
  note_key TEXT PRIMARY KEY,
  note_text TEXT NOT NULL
);

INSERT INTO abstraction_governance_notes VALUES
('referent','Name the real system process or concern being abstracted.'),
('representation','Define the computational form the abstraction takes.'),
('scope','Document where the abstraction applies and where it fails.'),
('loss','Identify what has been simplified hidden or excluded.'),
('interpretation','Explain how outputs should and should not be understood.'),
('reuse','Validate reuse before applying the abstraction in a new context.');
