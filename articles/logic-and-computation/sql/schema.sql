DROP TABLE IF EXISTS logic_computation_cases;
DROP TABLE IF EXISTS logic_governance_notes;

CREATE TABLE logic_computation_cases (
  case_name TEXT PRIMARY KEY,
  system_context TEXT NOT NULL,
  logical_structure TEXT NOT NULL,
  rule_clarity REAL NOT NULL,
  predicate_definition REAL NOT NULL,
  input_validity REAL NOT NULL,
  contradiction_control REAL NOT NULL,
  inference_traceability REAL NOT NULL,
  constraint_coverage REAL NOT NULL,
  testability REAL NOT NULL,
  verification_readiness REAL NOT NULL,
  explainability REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

INSERT INTO logic_computation_cases VALUES
('Input validation rules','Form validation and data-quality gate','Predicates over required fields formats and allowed ranges',0.82,0.84,0.80,0.76,0.68,0.78,0.82,0.62,0.78,0.70),
('Database query constraints','Relational database with joins and integrity constraints','Selection predicates foreign keys uniqueness and check constraints',0.78,0.80,0.76,0.74,0.72,0.82,0.76,0.66,0.70,0.72),
('Decision-rule workflow','Institutional routing workflow using explicit rules','If-then rules exceptions review states and escalation paths',0.74,0.70,0.72,0.62,0.68,0.66,0.72,0.58,0.76,0.78),
('Program invariant checks','Algorithm with state transitions and runtime assertions','Preconditions postconditions loop invariants and assertions',0.80,0.78,0.74,0.76,0.74,0.72,0.80,0.76,0.68,0.66);

CREATE TABLE logic_governance_notes (
  note_key TEXT PRIMARY KEY,
  note_text TEXT NOT NULL
);

INSERT INTO logic_governance_notes VALUES
('predicates','Define every predicate used in validation routing or decision logic.'),
('contradictions','Check for contradictory rules and unsafe defaults.'),
('traceability','Preserve inference traces where consequences matter.'),
('limits','Distinguish formal validity from responsible use.'),
('monitoring','Monitor rules for drift context changes and unintended effects.'),
('versioning','Version rule sets schemas and verification assumptions.');
