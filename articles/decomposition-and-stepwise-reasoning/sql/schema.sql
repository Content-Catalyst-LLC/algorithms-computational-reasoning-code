DROP TABLE IF EXISTS decomposition_cases;
DROP TABLE IF EXISTS decomposition_governance_notes;

CREATE TABLE decomposition_cases (
  case_name TEXT PRIMARY KEY,
  whole_problem TEXT NOT NULL,
  decomposition_strategy TEXT NOT NULL,
  subproblem_clarity REAL NOT NULL,
  boundary_definition REAL NOT NULL,
  input_output_clarity REAL NOT NULL,
  sequencing_quality REAL NOT NULL,
  dependency_visibility REAL NOT NULL,
  testability REAL NOT NULL,
  traceability REAL NOT NULL,
  recomposition_quality REAL NOT NULL,
  governance_readiness REAL NOT NULL,
  risk_awareness REAL NOT NULL
);

INSERT INTO decomposition_cases VALUES
('Search system','Help users find relevant information','Crawl parse index query rank filter evaluate',0.82,0.78,0.80,0.82,0.72,0.76,0.68,0.72,0.58,0.62),
('Public decision-support workflow','Prioritize cases while preserving fairness and accountability','Evidence checks scoring review appeal documentation monitoring',0.74,0.66,0.70,0.68,0.60,0.66,0.72,0.58,0.76,0.80),
('Scientific simulation','Explore how a dynamic system changes under scenarios','States parameters transition rules numerical method scenarios outputs',0.86,0.82,0.84,0.80,0.78,0.76,0.78,0.82,0.70,0.76),
('Knowledge architecture','Organize a research library for discovery navigation and reuse','Categories article maps metadata internal links search update workflow',0.80,0.76,0.72,0.74,0.70,0.64,0.72,0.80,0.68,0.70);

CREATE TABLE decomposition_governance_notes (
  note_key TEXT PRIMARY KEY,
  note_text TEXT NOT NULL
);

INSERT INTO decomposition_governance_notes VALUES
('whole_problem','Name the whole problem before splitting it.'),
('boundaries','Define component boundaries inputs outputs and assumptions.'),
('dependencies','Map dependencies and data flows across parts.'),
('tests','Use unit integration edge-case trace and governance tests.'),
('recomposition','Review whether the parts recombine into a meaningful whole.');
