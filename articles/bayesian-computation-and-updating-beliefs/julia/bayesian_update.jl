alpha = 2.0; beta = 2.0; successes = 113.0; failures = 72.0
post_alpha = alpha + successes; post_beta = beta + failures
println("posterior_mean=", post_alpha / (post_alpha + post_beta))
