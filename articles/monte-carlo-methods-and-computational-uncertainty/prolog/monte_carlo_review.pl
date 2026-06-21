check(quantity_of_interest_defined).
check(input_distributions_documented).
check(sample_size_justified).
check(seed_recorded).
check(sampling_error_reported).
check(interpretation_limits_stated).

responsible_monte_carlo_workflow :-
    check(quantity_of_interest_defined),
    check(input_distributions_documented),
    check(sample_size_justified),
    check(seed_recorded),
    check(sampling_error_reported),
    check(interpretation_limits_stated).
