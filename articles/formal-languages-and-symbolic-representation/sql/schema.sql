DROP TABLE IF EXISTS formal_language_cases;

CREATE TABLE formal_language_cases (
  case_name TEXT PRIMARY KEY,
  representation_context TEXT NOT NULL,
  symbolic_structure TEXT NOT NULL,
  alphabet_clarity REAL NOT NULL,
  grammar_explicitness REAL NOT NULL,
  syntax_validation REAL NOT NULL,
  semantic_clarity REAL NOT NULL,
  parser_readiness REAL NOT NULL,
  schema_support REAL NOT NULL,
  error_reporting REAL NOT NULL,
  testability REAL NOT NULL,
  interoperability REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

INSERT INTO formal_language_cases VALUES
('Expression grammar','Arithmetic expression evaluator','Tokens grammar rules parse trees and evaluation semantics',0.82,0.86,0.84,0.78,0.82,0.62,0.74,0.82,0.68,0.64),
('JSON configuration schema','Application configuration file','Keys values nested objects schema validation and defaults',0.76,0.78,0.84,0.72,0.80,0.86,0.72,0.78,0.82,0.70),
('SQL query layer','Relational data retrieval workflow','Query syntax predicates joins constraints and result schemas',0.74,0.76,0.78,0.70,0.74,0.82,0.68,0.74,0.78,0.72),
('Rule-language workflow','Institutional decision-routing rules','If-then rules predicates exceptions review states and traceable outputs',0.70,0.68,0.66,0.64,0.60,0.70,0.66,0.72,0.62,0.80);
