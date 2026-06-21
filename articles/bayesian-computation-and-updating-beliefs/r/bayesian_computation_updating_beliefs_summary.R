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
updates_path <- file.path(tables_dir, "bayesian_sequential_updates.csv")
if (!file.exists(updates_path)) stop(paste("Missing", updates_path, "Run the Python workflow first."))
updates <- read.csv(updates_path, stringsAsFactors = FALSE)
updates$stage_order <- ave(seq_len(nrow(updates)), updates$scenario, FUN = seq_along)
png(file.path(figures_dir, "bayesian_sequential_posterior_means.png"), width = 1300, height = 850)
plot(NULL, xlim = range(updates$stage_order), ylim = range(updates$posterior_mean), xlab = "Update stage", ylab = "Posterior mean", main = "Sequential Bayesian Updating Across Priors")
for (scenario in unique(updates$scenario)) {
  subset_data <- subset(updates, scenario == scenario)
  lines(subset_data$stage_order, subset_data$posterior_mean, type = "b", pch = 19)
}
legend("bottomright", legend = unique(updates$scenario), lty = 1, pch = 19, bty = "n")
grid(); dev.off()
final_path <- file.path(tables_dir, "bayesian_final_posteriors.csv")
if (file.exists(final_path)) {
  final_data <- read.csv(final_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "bayesian_final_posterior_means_by_prior.png"), width = 1300, height = 850)
  barplot(final_data$posterior_mean, names.arg = final_data$scenario, las = 2, ylim = c(0, max(final_data$p95)), ylab = "Posterior mean", main = "Final Posterior Mean by Prior Scenario")
  grid(); dev.off()
  png(file.path(figures_dir, "bayesian_threshold_probabilities_by_prior.png"), width = 1300, height = 850)
  barplot(final_data$probability_above_threshold, names.arg = final_data$scenario, las = 2, ylim = c(0, 1), ylab = "Posterior probability above threshold", main = "Threshold Probability by Prior Scenario")
  grid(); dev.off()
}
decision_path <- file.path(tables_dir, "bayesian_posterior_decisions.csv")
if (file.exists(decision_path)) {
  decision_data <- read.csv(decision_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "bayesian_expected_loss_comparison.png"), width = 1300, height = 850)
  plot(seq_len(nrow(decision_data)), decision_data$expected_loss_if_act, type = "b", pch = 19, xaxt = "n", ylim = range(c(decision_data$expected_loss_if_act, decision_data$expected_loss_if_wait)), xlab = "Prior scenario", ylab = "Expected loss", main = "Expected Loss Under Posterior Decision Rule")
  lines(seq_len(nrow(decision_data)), decision_data$expected_loss_if_wait, type = "b", pch = 17)
  axis(1, at = seq_len(nrow(decision_data)), labels = decision_data$scenario, las = 2)
  legend("topright", legend = c("Act", "Wait"), pch = c(19, 17), lty = 1, bty = "n")
  grid(); dev.off()
}
checklist_path <- file.path(tables_dir, "bayesian_review_checklist.csv")
if (file.exists(checklist_path)) {
  checklist_data <- read.csv(checklist_path, stringsAsFactors = FALSE)
  status_counts <- table(checklist_data$status)
  png(file.path(figures_dir, "bayesian_review_checklist_status.png"), width = 1000, height = 750)
  barplot(status_counts, ylim = c(0, max(status_counts) + 1), ylab = "Count", main = "Bayesian Review Checklist Status")
  grid(); dev.off()
}
audit_path <- file.path(tables_dir, "bayesian_computation_audit_summary.csv")
audit_data <- read.csv(audit_path, stringsAsFactors = FALSE)
r_summary <- data.frame(
  workflow_summary_rows = nrow(audit_data),
  prior_scenarios = audit_data$prior_scenarios[1],
  evidence_batches = audit_data$evidence_batches[1],
  total_observations = audit_data$total_observations[1],
  total_successes = audit_data$total_successes[1],
  posterior_mean_range_across_priors = audit_data$posterior_mean_range_across_priors[1],
  threshold_probability_range_across_priors = audit_data$threshold_probability_range_across_priors[1],
  review_items_needing_attention = audit_data$review_items_needing_attention[1]
)
write.csv(r_summary, file.path(tables_dir, "r_bayesian_computation_summary.csv"), row.names = FALSE)
print(r_summary)
