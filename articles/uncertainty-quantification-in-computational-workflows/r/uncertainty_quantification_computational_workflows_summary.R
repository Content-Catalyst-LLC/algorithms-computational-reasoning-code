#!/usr/bin/env Rscript
# Base R workflow for summarizing uncertainty quantification outputs and diagnostics.

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

if (!dir.exists(tables_dir)) dir.create(tables_dir, recursive = TRUE)
if (!dir.exists(figures_dir)) dir.create(figures_dir, recursive = TRUE)

ensemble_path <- file.path(tables_dir, "uncertainty_ensemble_runs.csv")
if (!file.exists(ensemble_path)) stop(paste("Missing", ensemble_path, "Run the Python workflow first."))

ensemble_data <- read.csv(ensemble_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "uncertainty_output_distribution.png"), width = 1300, height = 850)
hist(ensemble_data$risk_score, breaks = 35, xlab = "Risk score", main = "Uncertainty Ensemble Output Distribution")
abline(v = ensemble_data$threshold[1], lty = 2)
grid()
dev.off()

summary_path <- file.path(tables_dir, "uncertainty_output_summary.csv")
if (file.exists(summary_path)) {
  summary_data <- read.csv(summary_path, stringsAsFactors = FALSE)
  interval_values <- c(summary_data$p05_risk_score[1], summary_data$p25_risk_score[1], summary_data$median_risk_score[1], summary_data$p75_risk_score[1], summary_data$p95_risk_score[1])
  png(file.path(figures_dir, "uncertainty_interval_landmarks.png"), width = 1200, height = 800)
  plot(1:5, interval_values, type = "b", pch = 19, xaxt = "n", xlab = "Quantile landmark", ylab = "Risk score", main = "Uncertainty Interval Landmarks")
  axis(1, at = 1:5, labels = c("P05", "P25", "Median", "P75", "P95"))
  grid()
  dev.off()
}

influence_path <- file.path(tables_dir, "uncertainty_source_influence.csv")
if (file.exists(influence_path)) {
  influence_data <- read.csv(influence_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "uncertainty_source_influence.png"), width = 1300, height = 850)
  barplot(influence_data$absolute_correlation, names.arg = influence_data$uncertainty_source, las = 2, ylab = "Absolute correlation with output", main = "Uncertainty Source Influence")
  grid()
  dev.off()
}

checklist_path <- file.path(tables_dir, "uncertainty_review_checklist.csv")
if (file.exists(checklist_path)) {
  checklist_data <- read.csv(checklist_path, stringsAsFactors = FALSE)
  status_counts <- table(checklist_data$status)
  png(file.path(figures_dir, "uncertainty_review_checklist_status.png"), width = 1000, height = 750)
  barplot(status_counts, ylim = c(0, max(status_counts) + 1), ylab = "Count", main = "Uncertainty Review Checklist Status")
  grid()
  dev.off()
}

audit_path <- file.path(tables_dir, "uncertainty_quantification_audit_summary.csv")
audit_data <- read.csv(audit_path, stringsAsFactors = FALSE)

r_summary <- data.frame(
  workflow_summary_rows = nrow(audit_data),
  ensemble_size = audit_data$ensemble_size[1],
  mean_risk_score = audit_data$mean_risk_score[1],
  p05_risk_score = audit_data$p05_risk_score[1],
  p95_risk_score = audit_data$p95_risk_score[1],
  threshold_exceedance_probability = audit_data$threshold_exceedance_probability[1],
  most_influential_uncertainty_source = audit_data$most_influential_uncertainty_source[1],
  review_items_needing_attention = audit_data$review_items_needing_attention[1]
)

write.csv(r_summary, file.path(tables_dir, "r_uncertainty_quantification_summary.csv"), row.names = FALSE)
print(r_summary)
