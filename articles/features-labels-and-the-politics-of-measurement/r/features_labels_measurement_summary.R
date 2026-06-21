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
metrics_path <- file.path(tables_dir, "measurement_metrics_by_group.csv")
if (!file.exists(metrics_path)) stop(paste("Missing", metrics_path, "Run the Python workflow first."))
metrics <- read.csv(metrics_path, stringsAsFactors = FALSE)
png(file.path(figures_dir, "label_disagreement_by_group.png"), width = 1200, height = 800)
barplot(metrics$label_disagreement_rate, names.arg = metrics$group, ylab = "Label disagreement rate", main = "Observed Labels vs Synthetic Construct")
grid()
dev.off()
gaps_path <- file.path(tables_dir, "group_measurement_gaps.csv")
if (file.exists(gaps_path)) {
  gaps <- read.csv(gaps_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "group_measurement_gaps.png"), width = 1300, height = 850)
  barplot(gaps$absolute_gap, names.arg = gaps$metric, las = 2, ylab = "Absolute group gap", main = "Measurement Gaps by Metric")
  grid()
  dev.off()
}
features_path <- file.path(tables_dir, "feature_summary.csv")
if (file.exists(features_path)) {
  features <- read.csv(features_path, stringsAsFactors = FALSE)
  write.csv(features[, c("feature", "mean", "standard_deviation")], file.path(tables_dir, "r_feature_summary.csv"), row.names = FALSE)
}
r_summary <- data.frame(
  groups = paste(metrics$group, collapse = ";"),
  max_label_disagreement_rate = max(metrics$label_disagreement_rate),
  max_missing_prior_access_rate = max(metrics$missing_prior_access_rate)
)
write.csv(r_summary, file.path(tables_dir, "r_measurement_summary.csv"), row.names = FALSE)
print(r_summary)
