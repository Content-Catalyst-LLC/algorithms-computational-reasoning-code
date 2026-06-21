# scientific_computing_calculator.R
# Self-contained educational calculators for algorithms in scientific computing.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  root <- normalizePath(file.path(dirname(script_path), "..", ".."), mustWork = TRUE)
} else {
  root <- getwd()
}

out_dir <- file.path(root, "calculators", "outputs")
if (!dir.exists(out_dir)) dir.create(out_dir, recursive = TRUE)

finite_difference_derivative <- function(x = 1, h = 1e-4) {
  estimate <- (sin(x + h) - sin(x - h)) / (2 * h)
  true_value <- cos(x)
  data.frame(calculator = "finite_difference_derivative", metric = c("estimate", "true_value", "absolute_error"), value = c(estimate, true_value, abs(estimate - true_value)))
}

trapezoid_integral <- function(n = 200) {
  a <- 0
  b <- pi
  h <- (b - a) / n
  xs <- seq(a, b, length.out = n + 1)
  ys <- sin(xs)
  estimate <- h * (0.5 * ys[1] + sum(ys[2:n]) + 0.5 * ys[n + 1])
  data.frame(calculator = "trapezoid_integral", metric = c("estimate", "true_value", "absolute_error"), value = c(estimate, 2, abs(estimate - 2)))
}

monte_carlo_pi <- function(samples = 10000, seed = 42) {
  set.seed(seed)
  x <- runif(samples)
  y <- runif(samples)
  estimate <- 4 * mean(x * x + y * y <= 1)
  data.frame(calculator = "monte_carlo_pi", metric = c("estimate", "true_value", "absolute_error"), value = c(estimate, pi, abs(estimate - pi)))
}

results <- rbind(finite_difference_derivative(), trapezoid_integral(), monte_carlo_pi())
write.csv(results, file.path(out_dir, "r_scientific_computing_calculator_results.csv"), row.names = FALSE)
print(results)
