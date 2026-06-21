# Base R workflow for summarizing sensitivity analysis outputs and diagnostics.

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

ranking_path <- file.path(tables_dir, "parameter_influence_ranking.csv")
if (!file.exists(ranking_path)) {
  stop(paste("Missing", ranking_path, "Run the Python workflow first."))
}

ranking_data <- read.csv(ranking_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "parameter_influence_ranking.png"), width = 1300, height = 850)
barplot(ranking_data$risk_range, names.arg = ranking_data$parameter, las = 2, ylab = "Risk range", main = "Parameter Influence Ranking")
grid()
dev.off()

scenario_path <- file.path(tables_dir, "scenario_sensitivity.csv")
if (file.exists(scenario_path)) {
  scenario_data <- read.csv(scenario_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "scenario_average_risk.png"), width = 1300, height = 850)
  barplot(scenario_data$average_risk, names.arg = scenario_data$name, las = 2, ylab = "Average risk", main = "Scenario Sensitivity: Average Risk")
  grid()
  dev.off()
}

threshold_path <- file.path(tables_dir, "threshold_sensitivity.csv")
if (file.exists(threshold_path)) {
  threshold_data <- read.csv(threshold_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "threshold_crossings_by_cutoff.png"), width = 1300, height = 850)
  plot(threshold_data$threshold, threshold_data$threshold_crossings, type = "b", pch = 19, xlab = "Threshold", ylab = "Threshold crossings", main = "Threshold Sensitivity")
  grid()
  dev.off()
}

seed_path <- file.path(tables_dir, "seed_sensitivity.csv")
if (file.exists(seed_path)) {
  seed_data <- read.csv(seed_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "seed_sensitivity_distribution.png"), width = 1300, height = 850)
  hist(seed_data$average_risk, breaks = 20, xlab = "Average risk", main = "Seed Sensitivity Distribution")
  grid()
  dev.off()
}

checklist_path <- file.path(tables_dir, "sensitivity_review_checklist.csv")
if (file.exists(checklist_path)) {
  checklist_data <- read.csv(checklist_path, stringsAsFactors = FALSE)
  status_counts <- table(checklist_data$status)
  png(file.path(figures_dir, "sensitivity_review_checklist_status.png"), width = 1000, height = 750)
  barplot(status_counts, ylim = c(0, max(status_counts) + 1), ylab = "Count", main = "Sensitivity Review Checklist Status")
  grid()
  dev.off()
}

audit_path <- file.path(tables_dir, "sensitivity_analysis_audit_summary.csv")
audit_data <- read.csv(audit_path, stringsAsFactors = FALSE)

r_summary <- data.frame(
  workflow_summary_rows = nrow(audit_data),
  baseline_average_risk = audit_data$baseline_average_risk[1],
  most_influential_parameter = audit_data$most_influential_parameter[1],
  most_influential_parameter_risk_range = audit_data$most_influential_parameter_risk_range[1],
  runs_reviewed = audit_data$runs_reviewed[1],
  review_items_needing_attention = audit_data$review_items_needing_attention[1]
)

write.csv(r_summary, file.path(tables_dir, "r_sensitivity_analysis_summary.csv"), row.names = FALSE)
print(r_summary)
