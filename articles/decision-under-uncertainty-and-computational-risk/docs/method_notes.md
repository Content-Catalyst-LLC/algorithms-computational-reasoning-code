# Method Notes

This companion folder treats decision under uncertainty as a structured reasoning workflow, not as a single formula.

The workflow separates six questions:

1. What decision options are available?
2. What outcomes, benefits, costs, and harms matter?
3. How uncertain are the probability estimates?
4. Which threshold turns evidence into action?
5. How sensitive is the recommendation to assumptions?
6. Who can review, override, or contest the decision?

## Core quantities

Expected net value is calculated as:

`expected_net_value = expected_benefit - expected_loss - intervention_cost`

A threshold decision compares risk or expected value against a stated action rule. Regret analysis compares the selected option with the best available option in the same synthetic case. Sensitivity analysis perturbs probabilities, costs, and uncertainty margins to see when decisions change.

## Why this matters

A computational system can produce a recommendation without making its uncertainty visible. This folder shows how to expose the decision rule, assumptions, thresholds, and fragility of a recommendation.
