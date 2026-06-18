.headers on
.mode column
SELECT claim_name, claimed_growth,
ROUND(100.0*(0.12*input_definition_clarity+0.10*resource_scope_clarity+0.10*case_assumption_clarity+0.12*derivation_quality+0.10*tightness_clarity+0.12*benchmark_support+0.10*threshold_reporting+0.08*hidden_cost_review+0.08*governance_readiness+0.08*communication_clarity),2) AS big_o_claim_quality
FROM big_o_claims ORDER BY big_o_claim_quality DESC;
