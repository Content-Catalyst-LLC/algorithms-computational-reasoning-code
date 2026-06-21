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

pi_path <- file.path(tables_dir, "monte_carlo_pi_estimates.csv")
if (!file.exists(pi_path)) {
  stop(paste("Missing", pi_path, "Run the Python workflow first."))
}

pi_data <- read.csv(pi_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "monte_carlo_pi_error_by_samples.png"), width = 1300, height = 850)
plot(pi_data$samples, pi_data$absolute_error, log = "xy", type = "b", pch = 19,
     xlab = "Samples", ylab = "Absolute error", main = "Monte Carlo Pi Error by Sample Size")
grid()
dev.off()

cost_trials_path <- file.path(tables_dir, "project_cost_risk_trial_sample.csv")
if (file.exists(cost_trials_path)) {
  cost_trials <- read.csv(cost_trials_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "project_cost_trial_distribution.png"), width = 1300, height = 850)
  hist(cost_trials$cost, breaks = 30, xlab = "Simulated cost", main = "Monte Carlo Project Cost Trial Distribution")
  grid()
  dev.off()
}

propagation_path <- file.path(tables_dir, "uncertainty_propagation_trial_sample.csv")
if (file.exists(propagation_path)) {
  propagation_trials <- read.csv(propagation_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "uncertainty_propagation_output_distribution.png"), width = 1300, height = 850)
  hist(propagation_trials$output, breaks = 30, xlab = "Output", main = "Uncertainty Propagation Output Distribution")
  grid()
  dev.off()
}

convergence_path <- file.path(tables_dir, "monte_carlo_convergence_study.csv")
if (file.exists(convergence_path)) {
  convergence_data <- read.csv(convergence_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "monte_carlo_convergence_diagnostics.png"), width = 1300, height = 850)
  plot(convergence_data$samples, convergence_data$pi_mean_absolute_error, log = "xy", type = "b", pch = 19,
       xlab = "Samples", ylab = "Mean absolute error", main = "Monte Carlo Convergence Diagnostic")
  grid()
  dev.off()
}

checklist_path <- file.path(tables_dir, "monte_carlo_review_checklist.csv")
if (file.exists(checklist_path)) {
  checklist_data <- read.csv(checklist_path, stringsAsFactors = FALSE)
  status_counts <- table(checklist_data$status)
  png(file.path(figures_dir, "monte_carlo_review_checklist_status.png"), width = 1000, height = 750)
  barplot(status_counts, ylim = c(0, max(status_counts) + 1), ylab = "Count", main = "Monte Carlo Review Checklist Status")
  grid()
  dev.off()
}

summary_path <- file.path(tables_dir, "monte_carlo_uncertainty_audit_summary.csv")
summary_data <- read.csv(summary_path, stringsAsFactors = FALSE)

r_summary <- data.frame(
  workflow_summary_rows = nrow(summary_data),
  largest_convergence_sample_size = summary_data$largest_convergence_sample_size[1],
  project_cost_threshold_probability = summary_data$project_cost_threshold_probability[1],
  uncertainty_propagation_mean_output = summary_data$uncertainty_propagation_mean_output[1],
  review_items_needing_attention = summary_data$review_items_needing_attention[1]
)

write.csv(r_summary, file.path(tables_dir, "r_monte_carlo_uncertainty_summary.csv"), row.names = FALSE)
print(r_summary)
