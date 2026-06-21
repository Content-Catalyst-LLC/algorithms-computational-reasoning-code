#!/usr/bin/env Rscript
# Self-contained uncertainty quantification calculator in base R.

args <- commandArgs(trailingOnly = TRUE)
mode <- ifelse(length(args) >= 1, args[1], "ensemble")
runs <- ifelse(length(args) >= 2, as.integer(args[2]), 1000L)
threshold <- ifelse(length(args) >= 3, as.numeric(args[3]), 0.62)
seed <- ifelse(length(args) >= 4, as.integer(args[4]), 2026L)

bounded_normal <- function(center, spread) {
  max(0, min(1, rnorm(1, center, spread)))
}

risk_model <- function(demand, capacity, failure_rate, adaptation_rate, noise = 0) {
  max(0, min(1, 0.42 + 0.38 * demand - 0.31 * capacity + 0.27 * failure_rate - 0.18 * adaptation_rate + noise))
}

set.seed(seed)
if (mode == "single") {
  result <- data.frame(risk_score = risk_model(0.55, 0.50, 0.22, 0.30))
} else {
  values <- numeric(runs)
  for (i in seq_len(runs)) {
    values[i] <- risk_model(
      bounded_normal(0.55, 0.12),
      bounded_normal(0.50, 0.10),
      bounded_normal(0.22, 0.08),
      bounded_normal(0.30, 0.10),
      rnorm(1, 0, 0.035)
    )
  }
  result <- data.frame(
    runs = runs,
    threshold = threshold,
    mean = mean(values),
    sd = sd(values),
    min = min(values),
    max = max(values),
    exceedance_probability = mean(values >= threshold)
  )
}

out_dir <- file.path(getwd(), "calculators", "outputs")
if (!dir.exists(out_dir)) dir.create(out_dir, recursive = TRUE)
write.csv(result, file.path(out_dir, "r_calculator_result.csv"), row.names = FALSE)
print(result)
