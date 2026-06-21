# Base R workflow for summarizing model validation, testing, and computational evidence outputs.
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

summary_path <- file.path(tables_dir, "model_validation_summary.csv")
if (!file.exists(summary_path)) {
  stop(paste("Missing", summary_path, "Run the Python workflow first."))
}
summary_data <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "model_validation_rmse_comparison.png"), width = 1200, height = 800)
barplot(summary_data$rmse, names.arg = summary_data$model_name, las = 2, ylab = "RMSE", main = "Model Validation RMSE Comparison")
grid()
dev.off()

png(file.path(figures_dir, "model_validation_mae_comparison.png"), width = 1200, height = 800)
barplot(summary_data$mae, names.arg = summary_data$model_name, las = 2, ylab = "MAE", main = "Model Validation MAE Comparison")
grid()
dev.off()

subgroup_path <- file.path(tables_dir, "candidate_subgroup_diagnostics.csv")
if (file.exists(subgroup_path)) {
  subgroup_data <- read.csv(subgroup_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "candidate_subgroup_rmse.png"), width = 1000, height = 750)
  barplot(subgroup_data$rmse, names.arg = subgroup_data$segment, ylab = "RMSE", main = "Candidate Model RMSE by Segment")
  grid()
  dev.off()

  png(file.path(figures_dir, "candidate_subgroup_bias.png"), width = 1000, height = 750)
  barplot(subgroup_data$bias, names.arg = subgroup_data$segment, ylab = "Bias", main = "Candidate Model Bias by Segment")
  abline(h = 0, lty = 2)
  grid()
  dev.off()
}

threshold_path <- file.path(tables_dir, "threshold_sweep_diagnostics.csv")
if (file.exists(threshold_path)) {
  threshold_data <- read.csv(threshold_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "threshold_sweep_false_rates.png"), width = 1300, height = 850)
  plot(threshold_data$threshold, threshold_data$false_positive_rate, type = "b", pch = 19,
       ylim = range(c(threshold_data$false_positive_rate, threshold_data$false_negative_rate)),
       xlab = "Threshold", ylab = "Error rate", main = "Threshold Sweep: False Positive and False Negative Rates")
  lines(threshold_data$threshold, threshold_data$false_negative_rate, type = "b", pch = 17)
  legend("topright", legend = c("False positive rate", "False negative rate"), pch = c(19, 17), lty = 1, bty = "n")
  grid()
  dev.off()
}

audit_path <- file.path(tables_dir, "model_validation_evidence_audit_summary.csv")
audit_data <- read.csv(audit_path, stringsAsFactors = FALSE)
r_summary <- data.frame(
  workflow_summary_rows = nrow(audit_data),
  validation_rows = audit_data$validation_rows[1],
  candidate_rmse = audit_data$candidate_rmse[1],
  baseline_rmse = audit_data$baseline_rmse[1],
  implementation_test_failures = audit_data$implementation_test_failures[1],
  review_items_needing_attention = audit_data$review_items_needing_attention[1]
)
write.csv(r_summary, file.path(tables_dir, "r_model_validation_evidence_summary.csv"), row.names = FALSE)
print(r_summary)
