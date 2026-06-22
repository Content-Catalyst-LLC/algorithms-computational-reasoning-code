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

audit_path <- file.path(tables_dir, "drift_decay_audit.csv")
summary_path <- file.path(tables_dir, "drift_decay_summary.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

audit <- read.csv(audit_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "drift_decay_monitoring_signals.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(audit[, c("input_drift", "label_drift", "performance_decay", "calibration_gap", "subgroup_gap", "override_rate")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = audit$period,
        las = 2,
        ylim = c(0, 0.55),
        ylab = "Score",
        main = "Distribution Shift and Model Decay Signals")
legend("topleft",
       legend = rownames(score_matrix),
       cex = 0.72,
       bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "drift_decay_status_counts.png"), width = 1000, height = 750)
status_counts <- table(audit$status)
barplot(status_counts,
        ylab = "Count",
        main = "Drift and Decay Audit Status Counts")
grid()
dev.off()

r_summary <- data.frame(
  snapshots_reviewed = summary$snapshots_reviewed[1],
  snapshots_passed = summary$snapshots_passed[1],
  snapshots_requiring_review = summary$snapshots_requiring_review[1],
  snapshots_escalated = summary$snapshots_escalated[1],
  latest_status = summary$latest_status[1],
  latest_accuracy = summary$latest_accuracy[1],
  latest_performance_decay = summary$latest_performance_decay[1],
  mean_decay_risk_score = summary$mean_decay_risk_score[1],
  response_options = summary$response_options[1],
  governance_items = summary$governance_items[1],
  diagnostic_note = "Model decay should be monitored through data drift, label drift, performance loss, calibration drift, subgroup gaps, override rates, and rollback triggers."
)

write.csv(r_summary, file.path(tables_dir, "r_drift_decay_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
