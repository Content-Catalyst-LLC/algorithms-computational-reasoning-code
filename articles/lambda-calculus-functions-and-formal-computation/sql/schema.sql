DROP TABLE IF EXISTS lambda_expression_cases;

CREATE TABLE lambda_expression_cases (
  case_name TEXT PRIMARY KEY,
  computation_context TEXT NOT NULL,
  formal_claim TEXT NOT NULL,
  expression_clarity REAL NOT NULL,
  binding_safety REAL NOT NULL,
  substitution_discipline REAL NOT NULL,
  reduction_traceability REAL NOT NULL,
  evaluation_strategy_clarity REAL NOT NULL,
  recursion_awareness REAL NOT NULL,
  type_discipline_clarity REAL NOT NULL,
  proof_connection REAL NOT NULL,
  implementation_relevance REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

INSERT INTO lambda_expression_cases VALUES
('Identity reduction','Basic beta reduction of an identity function','The expression lambda x dot x applied to a reduces to a',0.92,0.90,0.92,0.90,0.82,0.70,0.82,0.76,0.78,0.74),
('Capture avoiding substitution','Substitution where variable names must be managed carefully','Alpha conversion prevents free variables from becoming accidentally bound',0.84,0.90,0.88,0.82,0.74,0.64,0.76,0.78,0.82,0.78),
('Fixed point recursion','Recursive behavior represented through fixed points','A fixed point combinator enables self referential computation',0.76,0.76,0.78,0.74,0.80,0.90,0.68,0.76,0.82,0.74),
('Typed function abstraction','Typed lambda expression used to model safe function application','A function with type A to B may only be applied to values of type A',0.86,0.84,0.82,0.78,0.76,0.68,0.92,0.86,0.86,0.82);
