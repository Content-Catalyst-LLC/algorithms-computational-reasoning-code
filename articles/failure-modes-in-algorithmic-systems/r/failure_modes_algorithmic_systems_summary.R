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

audit_path <- file.path(tables_dir, "failure_mode_audit.csv")
summary_path <- file.path(tables_dir, "failure_mode_summary.csv")

if (!file.exists(audit_path)) {
  stop(paste("Missing", audit_path, "Run the Python workflow first."))
}

audit <- read.csv(audit_path, stringsAsFactors = FALSE)
summary <- read.csv(summary_path, stringsAsFactors = FALSE)

png(file.path(figures_dir, "failure_mode_components.png"), width = 1200, height = 850)
score_matrix <- t(as.matrix(audit[, c("failure_risk_score", "priority_score", "resilience_capacity", "detectability", "controllability", "repair")]))
barplot(score_matrix,
        beside = TRUE,
        names.arg = audit$failure_id,
        las = 2,
        ylim = c(0, 1),
        ylab = "Score",
        main = "Failure Mode Risk and Resilience Components")
legend("bottomright", legend = rownames(score_matrix), cex = 0.68, bty = "n")
grid()
dev.off()

png(file.path(figures_dir, "failure_mode_status_counts.png"), width = 1000, height = 750)
status_counts <- table(audit$status)
barplot(status_counts, ylab = "Count", main = "Failure Mode Audit Status Counts")
grid()
dev.off()

r_summary <- data.frame(
  failure_modes_reviewed = summary$failure_modes_reviewed[1],
  failure_modes_passed = summary$failure_modes_passed[1],
  failure_modes_requiring_review = summary$failure_modes_requiring_review[1],
  failure_modes_escalated = summary$failure_modes_escalated[1],
  mean_failure_risk_score = summary$mean_failure_risk_score[1],
  mean_priority_score = summary$mean_priority_score[1],
  mean_resilience_capacity = summary$mean_resilience_capacity[1],
  failure_taxonomy_entries = summary$failure_taxonomy_entries[1],
  governance_items = summary$governance_items[1],
  diagnostic_note = "Failure-mode review should connect likelihood, severity, detectability, controllability, monitoring, fallback, rollback, escalation, repair, and governance."
)

write.csv(r_summary, file.path(tables_dir, "r_failure_mode_diagnostic_summary.csv"), row.names = FALSE)
print(r_summary)
