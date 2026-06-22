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

metrics_path <- file.path(tables_dir, "fairness_group_metrics.csv")
summary_path <- file.path(tables_dir, "fairness_audit_summary.csv")

if (!file.exists(metrics_path)) {
  stop(paste("Missing", metrics_path, "Run the Python workflow first."))
}

metrics <- read.csv(metrics_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "fairness_group_metric_components.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(metrics[, c("selection_rate", "false_positive_rate", "false_negative_rate", "true_positive_rate", "calibration_gap", "justice_capacity_score")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = metrics$group,
        ylim = c(0, 1),
        ylab = "Score",
        main = "Algorithmic Fairness and Computational Justice Group Metrics")
legend("topright",
       legend = rownames(score_matrix),
       cex = 0.72,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "justice_capacity_by_group.png"), width = 1000, height = 750)
barplot(metrics$justice_capacity_score,
        names.arg = metrics$group,
        ylim = c(0, 1),
        ylab = "Justice Capacity Score",
        main = "Justice Capacity by Group")
grid()
dev.off()

r_summary <- data.frame(
  groups_reviewed = summary$groups_reviewed[1],
  status = summary$status[1],
  selection_gap = summary$selection_gap[1],
  false_positive_gap = summary$false_positive_gap[1],
  false_negative_gap = summary$false_negative_gap[1],
  max_calibration_gap = summary$max_calibration_gap[1],
  mean_justice_capacity_score = summary$mean_justice_capacity_score[1],
  governance_items = summary$governance_items[1],
  diagnostic_note = "Fairness review should connect selection, error rates, calibration, measurement validity, contestability, remediation, and governance."
)

write.csv(r_summary, file.path(tables_dir, "r_fairness_justice_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
