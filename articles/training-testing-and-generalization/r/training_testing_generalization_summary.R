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
dir.create(figures_dir, recursive = TRUE, showWarnings = FALSE)
metrics_path <- file.path(tables_dir, "split_performance_metrics.csv")
if (!file.exists(metrics_path)) stop(paste("Missing", metrics_path, "Run the Python workflow first."))
metrics <- read.csv(metrics_path, stringsAsFactors = FALSE)
png(file.path(figures_dir, "split_accuracy_comparison.png"), width = 1200, height = 800)
barplot(metrics$accuracy, names.arg = metrics$split, las = 2, ylab = "Accuracy", main = "Training, Test, and Shifted-Test Accuracy")
grid()
dev.off()
cv_path <- file.path(tables_dir, "cross_validation_metrics.csv")
if (file.exists(cv_path)) {
  cv <- read.csv(cv_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "cross_validation_accuracy.png"), width = 1200, height = 800)
  plot(cv$fold, cv$accuracy, type = "b", xlab = "Fold", ylab = "Accuracy", main = "Cross-Validation Accuracy by Fold")
  grid()
  dev.off()
}
summary_path <- file.path(tables_dir, "training_testing_generalization_audit_summary.csv")
summary_data <- read.csv(summary_path, stringsAsFactors = FALSE)
r_summary <- data.frame(
  train_accuracy = summary_data$train_accuracy[1],
  test_accuracy = summary_data$test_accuracy[1],
  shifted_test_accuracy = summary_data$shifted_test_accuracy[1],
  generalization_gap_accuracy = summary_data$generalization_gap_accuracy[1],
  distribution_shift_gap_accuracy = summary_data$distribution_shift_gap_accuracy[1],
  risks_needing_review = summary_data$risks_needing_review[1]
)
write.csv(r_summary, file.path(tables_dir, "r_training_testing_generalization_summary.csv"), row.names = FALSE)
print(r_summary)
