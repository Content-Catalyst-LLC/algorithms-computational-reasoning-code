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
if (!file.exists(estimates_path)) stop(paste("Missing", estimates_path, "Run the Python workflow first."))
estimates <- read.csv(estimates_path, stringsAsFactors = FALSE)
png(file.path(figures_dir, "causal_effect_estimates.png"), width = 1300, height = 850)
barplot(estimates$estimated_effect, names.arg = estimates$estimate_type, las = 2, ylab = "Estimated effect", main = "Causal Effect Estimates by Method")
grid()
dev.off()
balance_path <- file.path(tables_dir, "causal_balance_diagnostics.csv")
if (file.exists(balance_path)) {
  balance <- read.csv(balance_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "causal_covariate_imbalance.png"), width = 1300, height = 850)
  barplot(balance$absolute_standardized_difference, names.arg = balance$covariate, las = 2, ylab = "Absolute standardized difference", main = "Covariate Imbalance Before Adjustment")
  abline(h = 0.10, lty = 2)
  grid()
  dev.off()
}
sensitivity_path <- file.path(tables_dir, "causal_estimator_sensitivity.csv")
if (file.exists(sensitivity_path)) {
  sensitivity <- read.csv(sensitivity_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "causal_estimator_error_from_synthetic_truth.png"), width = 1300, height = 850)
  barplot(sensitivity$absolute_error_from_synthetic_truth, names.arg = sensitivity$estimate_type, las = 2, ylab = "Absolute error from synthetic truth", main = "Estimator Sensitivity in Synthetic Causal Audit")
  grid()
  dev.off()
}
assumption_path <- file.path(tables_dir, "causal_assumption_register.csv")
if (file.exists(assumption_path)) {
  assumptions <- read.csv(assumption_path, stringsAsFactors = FALSE)
  status_counts <- table(assumptions$status)
  png(file.path(figures_dir, "causal_assumption_review_status.png"), width = 1000, height = 750)
  barplot(status_counts, ylim = c(0, max(status_counts) + 1), ylab = "Count", main = "Causal Assumption Review Status")
  grid()
  dev.off()
}
audit_path <- file.path(tables_dir, "causal_inference_audit_summary.csv")
audit_data <- read.csv(audit_path, stringsAsFactors = FALSE)
r_summary <- data.frame(
  workflow_summary_rows = nrow(audit_data),
  n = audit_data$n[1],
  treated_count = audit_data$treated_count[1],
  control_count = audit_data$control_count[1],
  true_synthetic_effect = audit_data$true_synthetic_effect[1],
  naive_estimate = audit_data$naive_estimate[1],
  stratified_estimate = audit_data$stratified_estimate[1],
  weighted_estimate = audit_data$weighted_estimate[1],
  assumption_items_needing_review = audit_data$assumption_items_needing_review[1]
)
write.csv(r_summary, file.path(tables_dir, "r_causal_inference_summary.csv"), row.names = FALSE)
print(r_summary)
