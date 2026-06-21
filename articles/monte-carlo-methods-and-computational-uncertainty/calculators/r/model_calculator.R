#!/usr/bin/env Rscript
args <- commandArgs(trailingOnly = TRUE)
mode <- ifelse(length(args) >= 1, args[1], "pi")
samples <- 10000
seed <- 42
threshold <- 1250000

for (arg in args) {
  if (grepl("^--samples=", arg)) samples <- as.integer(sub("^--samples=", "", arg))
  if (grepl("^--seed=", arg)) seed <- as.integer(sub("^--seed=", "", arg))
  if (grepl("^--threshold=", arg)) threshold <- as.numeric(sub("^--threshold=", "", arg))
}

ci <- function(values) {
  estimate <- mean(values)
  se <- if (length(values) > 1) sd(values) / sqrt(length(values)) else 0
  c(estimate = estimate, standard_error = se, lower_95 = estimate - 1.96 * se, upper_95 = estimate + 1.96 * se)
}

set.seed(seed)

if (mode == "pi") {
  x <- runif(samples)
  y <- runif(samples)
  values <- ifelse(x * x + y * y <= 1, 4, 0)
  out <- ci(values)
  cat(sprintf("pi_estimate=%.8f\n", out["estimate"]))
  cat(sprintf("standard_error=%.8f\n", out["standard_error"]))
  cat(sprintf("lower_95=%.8f\n", out["lower_95"]))
  cat(sprintf("upper_95=%.8f\n", out["upper_95"]))
  cat(sprintf("absolute_error=%.8f\n", abs(out["estimate"] - pi)))
} else if (mode == "threshold") {
  base <- runif(samples, 900000, 1100000)
  labor <- pmax(0.75, rnorm(samples, 1.0, 0.08))
  delay <- pmax(0, rnorm(samples, 60000, 35000))
  contingency <- runif(samples, 20000, 120000)
  values <- ifelse(base * labor + delay + contingency > threshold, 1, 0)
  out <- ci(values)
  cat(sprintf("threshold_probability=%.6f\n", out["estimate"]))
  cat(sprintf("standard_error=%.6f\n", out["standard_error"]))
  cat(sprintf("lower_95=%.6f\n", out["lower_95"]))
  cat(sprintf("upper_95=%.6f\n", out["upper_95"]))
} else {
  stop("Mode must be pi or threshold")
}
