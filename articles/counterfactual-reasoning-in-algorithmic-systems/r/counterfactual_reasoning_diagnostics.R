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

decisions_path <- file.path(tables_dir, "synthetic_algorithmic_decisions.csv")
if (!file.exists(decisions_path)) stop(paste("Missing", decisions_path, "Run the Python workflow first."))
decisions <- read.csv(decisions_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "decision_score_distribution.png"), width = 1200, height = 800)
hist(decisions$decision_score, breaks = 30, main = "Synthetic Decision Score Distribution", xlab = "Decision score")
abline(v = 0.62, lty = 2)
grid()
dev.off()

recourse_path <- file.path(tables_dir, "minimal_recourse_actions.csv")
if (file.exists(recourse_path)) {
  recourse <- read.csv(recourse_path, stringsAsFactors = FALSE)
  if (nrow(recourse) > 0) {
    png(file.path(figures_dir, "recourse_feature_counts.png"), width = 1200, height = 800)
    barplot(table(recourse$recommended_feature), las = 2, main = "Minimal Feasible Recourse by Feature", ylab = "Cases")
    grid()
    dev.off()

    png(file.path(figures_dir, "recourse_cost_distribution.png"), width = 1200, height = 800)
    hist(recourse$recourse_cost, breaks = 20, main = "Recourse Cost Distribution", xlab = "Synthetic recourse cost")
    grid()
    dev.off()
  }
}

threshold_path <- file.path(tables_dir, "threshold_sensitivity.csv")
if (file.exists(threshold_path)) {
  threshold <- read.csv(threshold_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "threshold_sensitivity.png"), width = 1200, height = 800)
  plot(threshold$threshold, threshold$favorable_share, type = "b", xlab = "Threshold", ylab = "Favorable share", main = "Decision Share Under Threshold Changes")
  grid()
  dev.off()
}

summary <- data.frame(
  rows = nrow(decisions),
  mean_score = mean(decisions$decision_score),
  favorable_count = sum(decisions$decision == "favorable"),
  review_count = sum(decisions$decision == "review"),
  unfavorable_count = sum(decisions$decision == "unfavorable")
)
write.csv(summary, file.path(tables_dir, "r_counterfactual_summary.csv"), row.names = FALSE)
print(summary)
