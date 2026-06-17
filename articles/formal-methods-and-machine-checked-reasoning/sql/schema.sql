DROP TABLE IF EXISTS formal_methods_cases;

CREATE TABLE formal_methods_cases (
  case_name TEXT PRIMARY KEY,
  verification_context TEXT NOT NULL,
  formal_claim TEXT NOT NULL,
  specification_clarity REAL NOT NULL,
  assumption_documentation REAL NOT NULL,
  invariant_strength REAL NOT NULL,
  proof_obligation_traceability REAL NOT NULL,
  machine_check_status REAL NOT NULL,
  counterexample_handling REAL NOT NULL,
  model_scope_clarity REAL NOT NULL,
  refinement_evidence REAL NOT NULL,
  unknown_status_handling REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

INSERT INTO formal_methods_cases VALUES
('Verified sorting function','Function is checked against sortedness and permutation properties','The output is sorted and contains the same elements as the input',0.88,0.80,0.84,0.86,0.84,0.78,0.80,0.76,0.74,0.78),
('Protocol model checking','A distributed protocol model is checked for unsafe reachable states','No modeled execution path reaches an unsafe agreement state',0.82,0.78,0.80,0.78,0.86,0.90,0.76,0.70,0.78,0.80),
('SMT backed contract check','A solver checks whether function contracts can be violated','No satisfying assignment violates the encoded contract within the supported theory',0.84,0.76,0.74,0.82,0.86,0.84,0.78,0.72,0.76,0.76),
('Institutional rule verification','A rule governed workflow is checked for consistency and escalation behavior','Clear cases are classified consistently and ambiguous cases are routed for review',0.78,0.74,0.70,0.76,0.70,0.76,0.78,0.68,0.86,0.88);
