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

summary_path <- file.path(tables_dir, "decision_risk_audit_summary.csv")
if (!file.exists(summary_path)) stop("Run make run before R diagnostics.")
summary_data <- read.csv(summary_path, stringsAsFactors = FALSE)
print(summary_data)

threshold_path <- file.path(tables_dir, "threshold_grid.csv")
if (file.exists(threshold_path)) {
  threshold_data <- read.csv(threshold_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "threshold_act_rate.png"), width = 1200, height = 800)
  plot(threshold_data$action_threshold, threshold_data$act_rate, type = "b", xlab = "Action threshold", ylab = "Act rate", main = "Action Rate by Threshold")
  grid()
  dev.off()
}

metrics_path <- file.path(tables_dir, "decision_metrics.csv")
if (file.exists(metrics_path)) {
  metrics <- read.csv(metrics_path, stringsAsFactors = FALSE)
  agg <- aggregate(expected_net_value ~ option_name, metrics, mean)
  png(file.path(figures_dir, "expected_net_value_by_option.png"), width = 1300, height = 850)
  barplot(agg$expected_net_value, names.arg = agg$option_name, las = 2, ylab = "Mean expected net value", main = "Mean Expected Net Value by Option")
  grid()
  dev.off()
}

sensitivity_path <- file.path(tables_dir, "uncertainty_sensitivity_grid.csv")
if (file.exists(sensitivity_path)) {
  sensitivity <- read.csv(sensitivity_path, stringsAsFactors = FALSE)
  write.csv(sensitivity, file.path(tables_dir, "r_uncertainty_sensitivity_summary.csv"), row.names = FALSE)
}
