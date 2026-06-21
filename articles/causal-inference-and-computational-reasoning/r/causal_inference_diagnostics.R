args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  article_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
} else {
  article_root <- getwd()
}
setwd(article_root)

tables_dir <- file.path(article_root, "outputs", "tables")
figures_dir <- file.path(article_root, "outputs", "figures")
dir.create(tables_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(figures_dir, recursive = TRUE, showWarnings = FALSE)

estimates_path <- file.path(tables_dir, "causal_effect_estimates.csv")
if (!file.exists(estimates_path)) stop("Run the Python causal workflow first.")

estimates <- read.csv(estimates_path, stringsAsFactors = FALSE)
png(file.path(figures_dir, "causal_effect_estimates.png"), width = 1400, height = 900)
barplot(estimates$estimated_effect, names.arg = estimates$estimate_type, las = 2,
        ylab = "Estimated effect", main = "Causal Effect Estimates by Method")
grid()
dev.off()

balance_path <- file.path(tables_dir, "covariate_balance_diagnostics.csv")
if (file.exists(balance_path)) {
  balance <- read.csv(balance_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "covariate_balance_diagnostics.png"), width = 1300, height = 850)
  barplot(balance$absolute_standardized_difference, names.arg = balance$covariate, las = 2,
          ylab = "Absolute standardized difference", main = "Pre-Adjustment Covariate Imbalance")
  abline(h = 0.10, lty = 2)
  grid()
  dev.off()
}

sensitivity_path <- file.path(tables_dir, "tipping_point_sensitivity.csv")
if (file.exists(sensitivity_path)) {
  sensitivity <- read.csv(sensitivity_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "tipping_point_sensitivity.png"), width = 1300, height = 850)
  barplot(sensitivity$unmeasured_bias_needed_to_nullify, names.arg = sensitivity$estimate_type, las = 2,
          ylab = "Bias needed to reduce estimate to zero", main = "Tipping-Point Sensitivity")
  grid()
  dev.off()
}

summary <- data.frame(
  estimates = nrow(estimates),
  largest_reported_effect = max(estimates$estimated_effect),
  smallest_reported_effect = min(estimates$estimated_effect)
)
write.csv(summary, file.path(tables_dir, "r_diagnostic_summary.csv"), row.names = FALSE)
print(summary)
