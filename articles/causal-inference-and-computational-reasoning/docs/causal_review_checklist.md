# Causal Review Checklist

Use this checklist before interpreting a computational result as causal.

## Question design

- Is the treatment, exposure, rule, threshold, policy, or intervention clearly defined?
- Is the comparison condition explicit?
- Is the outcome measured in a way that matches the real question?
- Is the population or setting clearly bounded?

## Identification

- What assumptions are required for a causal interpretation?
- Are confounders measured before treatment?
- Are mediators accidentally being controlled for?
- Is there a plausible collider or selection problem?
- Is there sufficient overlap between treated and untreated units?

## Estimation

- What estimand is being targeted?
- Which estimator is used?
- How does the estimate compare with simpler baselines?
- Is uncertainty reported?
- Are alternative specifications checked?

## Governance

- Who can challenge the assumptions?
- What evidence is missing?
- Who could be harmed by overinterpreting the result?
- Where should the estimate not be applied?
- Is the causal claim documented separately from predictive performance?
