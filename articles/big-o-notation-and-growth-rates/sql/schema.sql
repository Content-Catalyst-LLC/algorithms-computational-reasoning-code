DROP TABLE IF EXISTS big_o_claims;
CREATE TABLE big_o_claims (
  claim_name TEXT PRIMARY KEY, system_context TEXT, claimed_growth TEXT,
  input_definition_clarity REAL, resource_scope_clarity REAL, case_assumption_clarity REAL,
  derivation_quality REAL, tightness_clarity REAL, benchmark_support REAL, threshold_reporting REAL,
  hidden_cost_review REAL, governance_readiness REAL, communication_clarity REAL
);
.import --csv data/synthetic_big_o_claims.csv big_o_claims
