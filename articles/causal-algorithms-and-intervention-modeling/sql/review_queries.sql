-- Candidate interventions with positive modeled effects and positive net benefit.
SELECT intervention_name, mean_estimated_effect, mean_net_benefit, decision_change_rate
FROM intervention_effect_estimates
WHERE mean_estimated_effect > 0 AND mean_net_benefit > 0
ORDER BY mean_net_benefit DESC;

-- Effects requiring additional governance review.
SELECT intervention_name, feasibility_status, review_question
FROM intervention_feasibility_review
WHERE feasibility_status <> 'weak_or_uncertain';

-- Adjustment items that still need review.
SELECT target_effect, candidate_adjustment, review_status, collider_warning, mediator_warning
FROM adjustment_set_review
WHERE review_status LIKE '%review%';
