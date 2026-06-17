DROP TABLE IF EXISTS pseudocode_translation_cases;
DROP TABLE IF EXISTS translation_governance_notes;

CREATE TABLE pseudocode_translation_cases (
  case_name TEXT PRIMARY KEY,
  pseudocode_goal TEXT NOT NULL,
  program_context TEXT NOT NULL,
  intent_clarity REAL NOT NULL,
  input_specification REAL NOT NULL,
  output_specification REAL NOT NULL,
  state_handling REAL NOT NULL,
  control_flow_fidelity REAL NOT NULL,
  edge_case_coverage REAL NOT NULL,
  error_handling REAL NOT NULL,
  test_coverage REAL NOT NULL,
  readability REAL NOT NULL,
  maintainability REAL NOT NULL
);

INSERT INTO pseudocode_translation_cases VALUES
('Search ranking prototype','Retrieve candidates score documents rank results and return top matches','Python search-ranking workflow with synthetic records',0.82,0.74,0.78,0.70,0.80,0.64,0.62,0.68,0.78,0.72),
('Decision-rule implementation','Apply eligibility rules flag incomplete records and route review cases','Rule-based institutional workflow with review states',0.76,0.70,0.72,0.78,0.74,0.66,0.70,0.62,0.72,0.68),
('Simulation loop','Update state variables over time until horizon or convergence condition','Numerical simulation with time steps and generated outputs',0.84,0.82,0.78,0.86,0.82,0.72,0.68,0.70,0.76,0.74),
('Data-cleaning procedure','Validate records remove duplicates handle missing values and output clean data','Data pipeline step using synthetic tabular data',0.78,0.76,0.74,0.68,0.76,0.70,0.64,0.66,0.80,0.72);

CREATE TABLE translation_governance_notes (
  note_key TEXT PRIMARY KEY,
  note_text TEXT NOT NULL
);

INSERT INTO translation_governance_notes VALUES
('purpose','State the procedure purpose clearly.'),
('inputs','Define accepted and rejected inputs.'),
('outputs','Define outputs warnings errors and interpretation limits.'),
('representations','Choose data structures types schemas and interfaces deliberately.'),
('tests','Write ordinary edge failure invariant regression and integration tests.'),
('documentation','Document assumptions examples limits dependencies and runtime requirements.');
