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

time_path <- file.path(tables_dir, "agent_based_time_series.csv")
if (!file.exists(time_path)) stop(paste("Missing", time_path, "Run the Python workflow first."))

time_data <- read.csv(time_path, stringsAsFactors = FALSE)
sample_run <- subset(time_data, seed == 1 & tolerance == min(time_data$tolerance))

png(file.path(figures_dir, "agent_based_clustering_over_time.png"), width = 1300, height = 850)
plot(sample_run$step, sample_run$clustering_score, type = "l", lwd = 2,
     xlab = "Step", ylab = "Clustering score", main = "Agent-Based Clustering Over Time")
grid()
dev.off()

png(file.path(figures_dir, "agent_based_satisfaction_over_time.png"), width = 1300, height = 850)
plot(sample_run$step, sample_run$satisfaction_rate, type = "l", lwd = 2,
     xlab = "Step", ylab = "Satisfaction rate", main = "Agent Satisfaction Over Time")
grid()
dev.off()

ensemble_path <- file.path(tables_dir, "agent_based_ensemble_summary.csv")
if (file.exists(ensemble_path)) {
  ensemble_data <- read.csv(ensemble_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "agent_based_tolerance_vs_clustering.png"), width = 1300, height = 850)
  plot(ensemble_data$tolerance, ensemble_data$mean_final_clustering_score, type = "b", pch = 19,
       xlab = "Tolerance", ylab = "Mean final clustering score", main = "Tolerance and Emergent Clustering")
  grid()
  dev.off()
}

run_summary_path <- file.path(tables_dir, "agent_based_run_summaries.csv")
if (file.exists(run_summary_path)) {
  run_data <- read.csv(run_summary_path, stringsAsFactors = FALSE)
  png(file.path(figures_dir, "agent_based_final_clustering_distribution.png"), width = 1300, height = 850)
  hist(run_data$final_clustering_score, breaks = 30,
       xlab = "Final clustering score", main = "Distribution of Final Clustering Across Runs")
  grid()
  dev.off()
}

checklist_path <- file.path(tables_dir, "agent_based_review_checklist.csv")
if (file.exists(checklist_path)) {
  checklist_data <- read.csv(checklist_path, stringsAsFactors = FALSE)
  status_counts <- table(checklist_data$status)
  png(file.path(figures_dir, "agent_based_review_checklist_status.png"), width = 1000, height = 750)
  barplot(status_counts, ylim = c(0, max(status_counts) + 1), ylab = "Count",
          main = "Agent-Based Review Checklist Status")
  grid()
  dev.off()
}

summary_path <- file.path(tables_dir, "agent_based_emergence_audit_summary.csv")
summary_data <- read.csv(summary_path, stringsAsFactors = FALSE)
r_summary <- data.frame(
  workflow_summary_rows = nrow(summary_data),
  simulation_runs = summary_data$simulation_runs[1],
  tolerance_levels = summary_data$tolerance_levels[1],
  highest_observed_clustering_score = summary_data$highest_observed_clustering_score[1],
  review_items_needing_attention = summary_data$review_items_needing_attention[1]
)
write.csv(r_summary, file.path(tables_dir, "r_agent_based_emergence_summary.csv"), row.names = FALSE)
print(r_summary)
