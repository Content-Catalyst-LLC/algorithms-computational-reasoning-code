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
metrics_path <- file.path(tables_dir, "model_complexity_metrics.csv")
if (!file.exists(metrics_path)) stop(paste("Missing", metrics_path, "Run the Python workflow first."))
metrics <- read.csv(metrics_path, stringsAsFactors = FALSE)
png(file.path(figures_dir, "model_complexity_train_test_mse.png"), width = 1300, height = 850)
barplot(rbind(metrics$train_mse, metrics$test_mse), beside = TRUE, names.arg = metrics$model_name, las = 2, ylab = "MSE", main = "Train and Test Error by Model Complexity")
legend("topright", legend = c("train", "test"), fill = gray.colors(2))
grid()
dev.off()
validation_path <- file.path(tables_dir, "model_error_validation_curve.csv")
if (file.exists(validation_path)) {
  validation <- read.csv(validation_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "model_error_validation_curve.png"), width = 1200, height = 800)
  plot(validation$degree, validation$train_mse, type = "b", xlab = "Polynomial degree", ylab = "MSE", main = "Validation Curve")
  lines(validation$degree, validation$test_mse, type = "b", lty = 2)
  legend("topright", legend = c("train", "test"), lty = c(1, 2))
  grid()
  dev.off()
}
summary_path <- file.path(tables_dir, "model_error_audit_summary.csv")
summary <- read.csv(summary_path, stringsAsFactors = FALSE)
r_summary <- data.frame(
  model_count = summary$model_count[1],
  best_test_model = summary$best_test_model[1],
  best_test_mse = summary$best_test_mse[1],
  largest_generalization_gap_model = summary$largest_generalization_gap_model[1],
  models_flagged_for_review = summary$models_flagged_for_review[1]
)
write.csv(r_summary, file.path(tables_dir, "r_model_error_summary.csv"), row.names = FALSE)
print(r_summary)
