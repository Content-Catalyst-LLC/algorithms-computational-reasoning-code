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

metrics_path <- file.path(tables_dir, "bias_history_group_metrics.csv")
summary_path <- file.path(tables_dir, "bias_history_audit_summary.csv")

if (!file.exists(metrics_path)) {
  stop(paste("Missing", metrics_path, "Run the Python workflow first."))
}

metrics <- read.csv(metrics_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "bias_history_group_components.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(metrics[, c("data_share", "deployment_share", "selection_rate", "representation_gap", "label_gap", "historical_risk_score")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = metrics$group_id,
        ylim = c(0, 1),
        ylab = "Score",
        main = "Algorithmic Bias, Data, and Institutional History Components")
legend("topright",
       legend = rownames(score_matrix),
       cex = 0.72,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "historical_risk_by_group.png"), width = 1000, height = 750)
barplot(metrics$historical_risk_score,
        names.arg = metrics$group_id,
        ylim = c(0, 1),
        ylab = "Historical Risk Score",
        main = "Historical Risk by Group")
grid()
dev.off()

r_summary <- data.frame(
  groups_reviewed = summary$groups_reviewed[1],
  status = summary$status[1],
  selection_gap = summary$selection_gap[1],
  total_representation_gap = summary$total_representation_gap[1],
  max_label_gap = summary$max_label_gap[1],
  mean_historical_risk_score = summary$mean_historical_risk_score[1],
  max_historical_risk_score = summary$max_historical_risk_score[1],
  governance_items = summary$governance_items[1],
  diagnostic_note = "Bias review should connect data provenance, institutional history, representation, labels, proxies, measurement validity, fairness, contestability, remediation, and governance."
)

write.csv(r_summary, file.path(tables_dir, "r_bias_history_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
