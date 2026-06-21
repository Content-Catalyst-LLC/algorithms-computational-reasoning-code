# Base R workflow for summarizing probabilistic algorithm audit outputs.

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

summary_path <- file.path(tables_dir, "probabilistic_sampling_summary.csv")
if (!file.exists(summary_path)) {
  stop(paste("Missing", summary_path, "Run the Python workflow first."))
}

sampling_summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "sample_size_vs_mean_absolute_error.png"), width = 1300, height = 850)
plot(sampling_summary$sample_size, sampling_summary$mean_absolute_error, type = "b", pch = 19,
     xlab = "Sample size", ylab = "Mean absolute error",
     main = "Sample Size and Probabilistic Estimation Error")
grid()
dev.off()

png(file.path(figures_dir, "sample_size_vs_estimate_variability.png"), width = 1300, height = 850)
plot(sampling_summary$sample_size, sampling_summary$std_estimate, type = "b", pch = 19,
     xlab = "Sample size", ylab = "Standard deviation of estimates",
     main = "Sample Size and Estimate Variability")
grid()
dev.off()

sampling_trials_path <- file.path(tables_dir, "probabilistic_sampling_trials.csv")
if (file.exists(sampling_trials_path)) {
  sampling_trials <- read.csv(sampling_trials_path, stringsAsFactors = FALSE)
  largest_n <- max(sampling_trials$sample_size)
  largest_trials <- subset(sampling_trials, sample_size == largest_n)
  png(file.path(figures_dir, "largest_sample_estimate_distribution.png"), width = 1300, height = 850)
  hist(largest_trials$estimate, breaks = 25, xlab = "Probability estimate",
       main = "Distribution of Probability Estimates at Largest Sample Size")
  abline(v = largest_trials$true_probability[1], lty = 2)
  abline(v = largest_trials$threshold[1], lty = 3)
  grid()
  dev.off()
}

sort_path <- file.path(tables_dir, "randomized_sort_audit.csv")
if (file.exists(sort_path)) {
  sort_data <- read.csv(sort_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "randomized_sort_comparisons_distribution.png"), width = 1300, height = 850)
  hist(sort_data$comparisons, breaks = 25, xlab = "Comparisons",
       main = "Randomized Quicksort Comparison Counts")
  grid()
  dev.off()
}

loss_path <- file.path(tables_dir, "expected_loss_decisions.csv")
if (file.exists(loss_path)) {
  loss_data <- read.csv(loss_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "expected_loss_decision_comparison.png"), width = 1300, height = 850)
  plot(loss_data$event_probability, loss_data$expected_loss_if_act, type = "b", pch = 19,
       ylim = range(c(loss_data$expected_loss_if_act, loss_data$expected_loss_if_do_not_act)),
       xlab = "Event probability", ylab = "Expected loss",
       main = "Expected Loss Under Uncertain Action")
  lines(loss_data$event_probability, loss_data$expected_loss_if_do_not_act, type = "b", pch = 17)
  legend("topright", legend = c("Act", "Do not act"), pch = c(19, 17), lty = 1, bty = "n")
  grid()
  dev.off()
}

checklist_path <- file.path(tables_dir, "probability_review_checklist.csv")
if (file.exists(checklist_path)) {
  checklist_data <- read.csv(checklist_path, stringsAsFactors = FALSE)
  status_counts <- table(checklist_data$status)
  png(file.path(figures_dir, "probability_review_checklist_status.png"), width = 1000, height = 750)
  barplot(status_counts, ylim = c(0, max(status_counts) + 1), ylab = "Count",
          main = "Probability Review Checklist Status")
  grid()
  dev.off()
}

audit_path <- file.path(tables_dir, "probabilistic_algorithm_audit_summary.csv")
audit_data <- read.csv(audit_path, stringsAsFactors = FALSE)

r_summary <- data.frame(
  workflow_summary_rows = nrow(audit_data),
  true_probability = audit_data$true_probability[1],
  decision_threshold = audit_data$decision_threshold[1],
  smallest_sample_mean_absolute_error = audit_data$smallest_sample_mean_absolute_error[1],
  largest_sample_mean_absolute_error = audit_data$largest_sample_mean_absolute_error[1],
  randomized_sort_all_runs_correct = audit_data$randomized_sort_all_runs_correct[1],
  review_items_needing_attention = audit_data$review_items_needing_attention[1]
)

write.csv(r_summary, file.path(tables_dir, "r_probabilistic_algorithm_summary.csv"), row.names = FALSE)
print(r_summary)
