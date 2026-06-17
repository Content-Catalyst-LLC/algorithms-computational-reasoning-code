DROP TABLE IF EXISTS programming_style_cases;
DROP TABLE IF EXISTS paradigm_taxonomy;

CREATE TABLE programming_style_cases (
  case_name TEXT PRIMARY KEY,
  problem_context TEXT NOT NULL,
  style_choice TEXT NOT NULL,
  style_clarity REAL NOT NULL,
  state_visibility REAL NOT NULL,
  abstraction_fit REAL NOT NULL,
  composability REAL NOT NULL,
  testability REAL NOT NULL,
  error_handling REAL NOT NULL,
  traceability REAL NOT NULL,
  performance_fit REAL NOT NULL,
  team_readability REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

CREATE TABLE paradigm_taxonomy (
  paradigm TEXT PRIMARY KEY,
  central_unit TEXT NOT NULL,
  reasoning_emphasis TEXT NOT NULL,
  example_language_or_context TEXT NOT NULL
);

INSERT INTO programming_style_cases VALUES
('Functional data transformation','A reproducible data workflow maps raw records into validated derived outputs','Functional core with pure transformation functions and explicit effect boundaries',0.90,0.92,0.88,0.92,0.94,0.84,0.88,0.82,0.84,0.90),
('Object-oriented domain model','A case-management system organizes entities responsibilities states and lifecycle rules','Object-oriented model with explicit interfaces validation methods and audit events',0.86,0.80,0.90,0.82,0.84,0.86,0.88,0.80,0.86,0.88),
('Declarative query layer','A research library retrieves and aggregates records using relational queries','SQL-style declarative queries with documented schemas indexes and query plans',0.88,0.84,0.88,0.82,0.82,0.80,0.86,0.88,0.86,0.86),
('Event-driven platform workflow','A platform responds to uploads edits approvals publication events and notifications','Event-driven workflow with structured event records idempotent handlers retries and audit logs',0.80,0.78,0.82,0.80,0.78,0.86,0.90,0.84,0.78,0.88);

INSERT INTO paradigm_taxonomy VALUES
('Imperative','command','state mutation and sequence','C'),
('Procedural','procedure','stepwise decomposition','Python scripts'),
('Functional','function','input-output transformation','Haskell'),
('Object-oriented','object','responsibility and lifecycle','Java'),
('Logic','relation','inference and constraints','Prolog'),
('Declarative','specification','desired result and constraints','SQL'),
('Event-driven','event','response to triggers','JavaScript UI'),
('Concurrent','process or task','coordination timing and failure','Erlang or Go'),
('Array-oriented','array','whole-collection operations','R or Julia'),
('Scripting','script','automation and orchestration','Bash or Python');
