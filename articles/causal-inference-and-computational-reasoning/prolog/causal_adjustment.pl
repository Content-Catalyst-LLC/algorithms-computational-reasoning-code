% Simple teaching facts for a causal graph.
edge(prior_risk, treatment).
edge(institutional_access, treatment).
edge(baseline_capacity, treatment).
edge(prior_risk, observed_outcome).
edge(institutional_access, observed_outcome).
edge(baseline_capacity, observed_outcome).
edge(treatment, observed_outcome).

confounder(X) :- edge(X, treatment), edge(X, observed_outcome), X \= treatment.
