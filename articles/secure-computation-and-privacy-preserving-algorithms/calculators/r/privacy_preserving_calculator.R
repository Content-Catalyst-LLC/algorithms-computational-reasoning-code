# privacy_preserving_calculator.R
# Educational calculator for privacy-preserving computation examples.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)

if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  article_root <- normalizePath(file.path(dirname(script_path), "..", ".."), mustWork = TRUE)
} else {
  article_root <- getwd()
}

outputs_dir <- file.path(article_root, "calculators", "outputs")
if (!dir.exists(outputs_dir)) {
  dir.create(outputs_dir, recursive = TRUE)
}

laplace_noise <- function(scale, seed) {
  set.seed(seed)
  u <- runif(1) - 0.5
  -scale * sign(u) * log(1 - 2 * abs(u))
}

dp_count <- function(true_count, epsilon, sensitivity = 1, seed = 7) {
  scale <- sensitivity / epsilon
  noise <- laplace_noise(scale, seed)
  data.frame(
    calculator = "dp_count",
    true_count = true_count,
    epsilon = epsilon,
    sensitivity = sensitivity,
    scale = scale,
    noise = noise,
    noisy_count = true_count + noise
  )
}

rows <- do.call(rbind, lapply(c(0.25, 0.5, 1.0, 2.0), function(eps) dp_count(248, eps)))

write.csv(
  rows,
  file.path(outputs_dir, "r_privacy_preserving_calculator.csv"),
  row.names = FALSE
)

print(file.path(outputs_dir, "r_privacy_preserving_calculator.csv"))
