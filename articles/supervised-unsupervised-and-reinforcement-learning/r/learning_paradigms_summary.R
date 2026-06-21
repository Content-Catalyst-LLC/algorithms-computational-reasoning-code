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
metrics_path <- file.path(tables_dir, "supervised_metrics.csv")
if (!file.exists(metrics_path)) stop(paste("Missing", metrics_path, "Run Python workflow first."))
metrics <- read.csv(metrics_path, stringsAsFactors = FALSE)
png(file.path(figures_dir, "supervised_accuracy_by_split.png"), width = 1100, height = 800)
barplot(metrics$accuracy, names.arg = metrics$split, las = 2, ylab = "Accuracy", main = "Supervised Learning Accuracy by Split")
grid()
dev.off()
cluster_path <- file.path(tables_dir, "unsupervised_cluster_summary.csv")
clusters <- read.csv(cluster_path, stringsAsFactors = FALSE)
png(file.path(figures_dir, "unsupervised_cluster_sizes.png"), width = 1100, height = 800)
barplot(clusters$n, names.arg = clusters$cluster, ylab = "Observations", main = "Unsupervised Cluster Sizes")
grid()
dev.off()
rl_path <- file.path(tables_dir, "reinforcement_learning_summary.csv")
rl <- read.csv(rl_path, stringsAsFactors = FALSE)
png(file.path(figures_dir, "reinforcement_learning_arm_rewards.png"), width = 1100, height = 800)
barplot(rl$observed_mean_reward, names.arg = rl$arm, las = 2, ylab = "Observed mean reward", main = "Reinforcement Learning Rewards by Arm")
grid()
dev.off()
r_summary <- data.frame(
  supervised_rows = nrow(metrics),
  cluster_count = nrow(clusters),
  rl_arms = nrow(rl),
  test_accuracy = metrics$accuracy[metrics$split == "test"][1],
  best_observed_reward = max(rl$observed_mean_reward)
)
write.csv(r_summary, file.path(tables_dir, "r_learning_paradigms_summary.csv"), row.names = FALSE)
print(r_summary)
