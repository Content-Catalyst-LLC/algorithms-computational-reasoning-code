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
metrics_path <- file.path(tables_dir, "ml_model_metrics.csv")
if (!file.exists(metrics_path)) stop(paste("Missing", metrics_path, "Run the Python workflow first."))
metrics <- read.csv(metrics_path, stringsAsFactors = FALSE)
png(file.path(figures_dir, "ml_accuracy_by_split.png"), width = 1200, height = 800)
barplot(metrics$accuracy, names.arg = metrics$split, ylim = c(0, 1), ylab = "Accuracy", main = "Machine-Learning Inference Accuracy by Split")
grid()
dev.off()
threshold_path <- file.path(tables_dir, "ml_threshold_sweep.csv")
if (file.exists(threshold_path)) {
  thresholds <- read.csv(threshold_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "ml_threshold_error_tradeoffs.png"), width = 1200, height = 800)
  plot(thresholds$threshold, thresholds$false_positive_rate, type = "l", ylim = c(0, 1), xlab = "Threshold", ylab = "Error rate", main = "Threshold Trade-Offs")
  lines(thresholds$threshold, thresholds$false_negative_rate, lty = 2)
  legend("topright", legend = c("False positive rate", "False negative rate"), lty = c(1, 2), bty = "n")
  grid()
  dev.off()
}
calibration_path <- file.path(tables_dir, "ml_calibration_bins.csv")
if (file.exists(calibration_path)) {
  calibration <- read.csv(calibration_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "ml_calibration_gap.png"), width = 1200, height = 800)
  barplot(calibration$absolute_calibration_gap, names.arg = calibration$bin, ylab = "Absolute calibration gap", xlab = "Score bin", main = "Calibration Gap by Score Bin")
  grid()
  dev.off()
}
summary <- data.frame(
  rows = nrow(metrics),
  test_accuracy = metrics$accuracy[metrics$split == "test"][1],
  test_false_positive_rate = metrics$false_positive_rate[metrics$split == "test"][1],
  test_false_negative_rate = metrics$false_negative_rate[metrics$split == "test"][1]
)
write.csv(summary, file.path(tables_dir, "r_ml_inference_summary.csv"), row.names = FALSE)
print(summary)
