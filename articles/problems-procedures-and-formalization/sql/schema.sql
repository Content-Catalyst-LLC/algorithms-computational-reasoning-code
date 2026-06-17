DROP TABLE IF EXISTS formalization_cases;
DROP TABLE IF EXISTS formalization_governance_notes;

CREATE TABLE formalization_cases (
  case_name TEXT PRIMARY KEY,
  real_world_concern TEXT NOT NULL,
  formal_task TEXT NOT NULL,
  input_clarity REAL NOT NULL,
  output_clarity REAL NOT NULL,
  constraint_clarity REAL NOT NULL,
  state_definition REAL NOT NULL,
  objective_alignment REAL NOT NULL,
  assumption_documentation REAL NOT NULL,
  edge_case_handling REAL NOT NULL,
  stopping_condition_clarity REAL NOT NULL,
  evaluation_quality REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

INSERT INTO formalization_cases VALUES
('Document search','Help people find useful information','Retrieve and rank documents for a query',0.82,0.78,0.62,0.60,0.70,0.58,0.62,0.74,0.70,0.56),
('Worker scheduling','Coordinate labor demand skill and wellbeing','Assign workers to shifts under coverage and availability constraints',0.72,0.76,0.82,0.70,0.58,0.54,0.56,0.68,0.60,0.62),
('Public service triage','Prioritize cases while preserving fairness and accountability','Classify cases into priority levels using administrative data',0.60,0.72,0.68,0.58,0.52,0.46,0.48,0.60,0.54,0.66),
('Scientific simulation','Explore how a system changes under scenarios','Simulate state transitions under parameterized assumptions',0.86,0.80,0.78,0.88,0.76,0.84,0.72,0.82,0.78,0.70);

CREATE TABLE formalization_governance_notes (
  note_key TEXT PRIMARY KEY,
  note_text TEXT NOT NULL
);

INSERT INTO formalization_governance_notes VALUES
('concern','Separate the real-world concern from the formal computational task.'),
('representation','Document inputs outputs constraints states objectives and assumptions.'),
('edge_cases','Test invalid input ties missingness no-solution cases and stopping conditions.'),
('interpretation','Explain how outputs should and should not be used.'),
('governance','Define review appeal monitoring revision and retirement criteria.');
