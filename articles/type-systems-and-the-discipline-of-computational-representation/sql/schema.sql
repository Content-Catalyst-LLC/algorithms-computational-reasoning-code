DROP TABLE IF EXISTS type_representation_cases;
DROP TABLE IF EXISTS type_taxonomy;

CREATE TABLE type_representation_cases (
  case_name TEXT PRIMARY KEY,
  problem_context TEXT NOT NULL,
  type_design_choice TEXT NOT NULL,
  representation_clarity REAL NOT NULL,
  constraint_strength REAL NOT NULL,
  missingness_handling REAL NOT NULL,
  boundary_validation REAL NOT NULL,
  domain_fidelity REAL NOT NULL,
  error_specificity REAL NOT NULL,
  type_coverage REAL NOT NULL,
  interoperability REAL NOT NULL,
  testability REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

CREATE TABLE type_taxonomy (
  type_concept TEXT PRIMARY KEY,
  category TEXT NOT NULL,
  definition TEXT NOT NULL,
  example TEXT NOT NULL
);

INSERT INTO type_representation_cases VALUES
('Typed article metadata','A research library needs reliable titles slugs article-map positions image metadata references and repository links','Structured article metadata record with validated slug required fields status enum repository URL and reference list',0.92,0.88,0.86,0.90,0.90,0.86,0.90,0.86,0.90,0.88),
('Scientific measurement model','A scientific workflow needs to distinguish values units uncertainty timestamp source and measurement method','Measurement type with unit-aware quantity uncertainty field timestamp instrument source and validation status',0.90,0.92,0.84,0.88,0.94,0.86,0.88,0.82,0.88,0.90),
('AI decision-support workflow','A model output must not be confused with a final institutional decision','Separate types for input features retrieved context model score recommendation human review final decision and appeal record',0.88,0.90,0.88,0.90,0.86,0.88,0.88,0.82,0.86,0.94),
('API contract boundary','Two services exchange event records status updates and validation results','Typed request and response schemas with versioned events explicit errors required fields and compatibility tests',0.86,0.88,0.82,0.92,0.84,0.88,0.86,0.92,0.88,0.86);

INSERT INTO type_taxonomy VALUES
('primitive type','basic value','A basic value category','Integer'),
('product type','composite type','A type containing multiple fields','ArticleRecord'),
('sum type','composite type','A type representing one of several alternatives','Result'),
('enum','finite alternative','A fixed set of named values','PublicationStatus'),
('option type','missingness','A value that may be present or absent','Option Reviewer'),
('result type','error modeling','A computation that succeeds or fails','Result ValidatedRecord ValidationError'),
('generic type','abstraction','A reusable type parameterized by another type','List Article'),
('refinement type','constraint','A type plus a predicate','Probability 0 to 1'),
('phantom type','state discipline','A marker type distinguishing states without runtime data','RawRecord vs ValidatedRecord'),
('schema','boundary contract','A type-like structure for external data','JSON Schema');
