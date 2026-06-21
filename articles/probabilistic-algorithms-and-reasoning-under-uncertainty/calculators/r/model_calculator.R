#!/usr/bin/env Rscript
# Reusable probability calculators for probabilistic algorithm examples.

expected_value <- function(values, probabilities) {
  if (length(values) != length(probabilities)) stop("values and probabilities must have the same length")
  probabilities <- probabilities / sum(probabilities)
  sum(values * probabilities)
}

prob_variance <- function(values, probabilities) {
  mu <- expected_value(values, probabilities)
  probabilities <- probabilities / sum(probabilities)
  sum(((values - mu) ^ 2) * probabilities)
}

bernoulli_standard_error <- function(p_hat, n) {
  sqrt(max(p_hat * (1 - p_hat), 0) / n)
}

confidence_interval <- function(p_hat, n, z = 1.96) {
  se <- bernoulli_standard_error(p_hat, n)
  c(lower = max(0, p_hat - z * se), upper = min(1, p_hat + z * se))
}

repeated_failure_probability <- function(p, k) {
  p ^ k
}

expected_loss <- function(probability, loss_false_positive = 1, loss_false_negative = 3) {
  act_loss <- (1 - probability) * loss_false_positive
  no_act_loss <- probability * loss_false_negative
  data.frame(
    expected_loss_if_act = act_loss,
    expected_loss_if_do_not_act = no_act_loss,
    choose_action = as.integer(act_loss <= no_act_loss)
  )
}

p_hat <- 0.57
n <- 1000
ci <- confidence_interval(p_hat, n)

result <- data.frame(
  p_hat = p_hat,
  n = n,
  standard_error = bernoulli_standard_error(p_hat, n),
  ci_lower = ci["lower"],
  ci_upper = ci["upper"],
  repeated_failure_probability = repeated_failure_probability(0.10, 5),
  example_expected_value = expected_value(c(0, 1, 2), c(0.2, 0.5, 0.3)),
  example_variance = prob_variance(c(0, 1, 2), c(0.2, 0.5, 0.3))
)

print(result)
print(expected_loss(0.60))
